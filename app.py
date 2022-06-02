from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)


def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client["employees"]
    return db


@app.route('/')
def ping_server():
    return "Welcome to the world of DevOps."


@app.route('/devops')
def get_stored_devops():
    db = get_db()
    _employees = db.devops.find()
    employees = [{"id": employee["id"], "name": employee["f_name"], "last name": employee["l_name"],
                 "city": employee["city"], "address": employee["address"], "phone_number": employee["phone_number"]}
                 for employee in _employees]
    return jsonify({"employees": employees})


@app.route("/insert")
def insert():
    db = get_db()
    employee = {"id": 4, "f_name": "Barak", "l_name": "Arzuan", "city": "Rishon", "address": "arishonim",
                "phone_number": "052-125-1211"}
    x = db.devops.insert_one(employee)
    return str(x.inserted_id)


@app.route("/remove/<name>")
def remove(name):
    db = get_db()
    x = db.devops.delete_one({"f_name": name})
    return x


@app.route("/search/<name>")
def search(name):
    db = get_db()
    res = db.devops.find_one({"f_name": name})
    return f"result: {res}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
