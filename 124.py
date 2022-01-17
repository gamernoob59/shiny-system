from telnetlib import STATUS
from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        "id":1,
        "contact": '1-800-222-1222',
        "name": 'Poison Control',
        "done":False
    },
    {
        "id":2,
        "contact": '911',
        "name":'Emergency Services',
        "done":False
    },
]
@app.route("/")
def hello_world():
    return "Hello world"
@app.route("/add-data",methods=["POST"])
def addtask():
    if not request.json():
        return jsonify({
            "status":"error",
            "message":"Please Provide the Data"
        },400)