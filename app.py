from flask import Flask,request,jsonify
import json,os,uuid
app=Flask(__name__)
DB='users.json'
def load():
    if not os.path.exists(DB):
        json.dump([],open(DB,'w'))
    return json.load(open(DB))
def save(u): json.dump(u,open(DB,'w'),indent=4)
@app.get('/')
def home(): return jsonify({'message':'Flask REST API'})
@app.get('/users')
def users(): return jsonify(load())
@app.get('/users/<uid>')
def one(uid):
    for u in load():
        if u['id']==uid:return jsonify(u)
    return jsonify({'error':'User not found'}),404
@app.post('/users')
def create():
    d=request.get_json()
    if not d:return jsonify({'error':'JSON required'}),400
    users=load()
    u={'id':str(uuid.uuid4()),'name':d['name'],'email':d['email'],'age':d['age']}
    users.append(u);save(users)
    return jsonify({'message':'Created','user':u}),201
@app.put('/users/<uid>')
def upd(uid):
    users=load();d=request.get_json() or {}
    for u in users:
        if u['id']==uid:
            u.update({k:v for k,v in d.items() if k in ['name','email','age']});save(users);return jsonify(u)
    return jsonify({'error':'User not found'}),404
@app.delete('/users/<uid>')
def dele(uid):
    users=load()
    for i,u in enumerate(users):
        if u['id']==uid:
            users.pop(i);save(users);return jsonify({'message':'Deleted'})
    return jsonify({'error':'User not found'}),404
if __name__=='__main__': app.run(debug=True)
