from flask import Flask, jsonify, render_template, redirect, url_for, request
import pymongo
from pymongo import MongoClient
from forms import CourseForm, Employee


app = Flask(__name__)
app.config['SECRET_KEY'] = 'auiofhsghzdffjuvhbnjkbhsdfg'


def get_db(db_name):
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client[db_name]
    return db


@app.route('/')
def ping_server():
    return "Welcome to the world of DevOps."


@app.route('/devops')
def get_stored_devops():
    db = get_db("employees")
    _employees = db.devops.find()
    employees_list = []
    for employee in _employees:
        employees_list.append({"name": employee["f_name"], "last name": employee["l_name"],
                               "city": employee["city"], "address": employee["address"],
                               "phone_number": employee["phone_number"]})
    # return jsonify({"employees": employees})
    return render_template('employee.html', employees_list=employees_list)


@app.route("/search/<name>")
def search(name):
    db = get_db("employees")
    res = db.devops.find_one({"f_name": name})
    return f"result: {res}"


@app.route("/insert", methods=['POST'])
def insert():
    db = get_db("employees")
    data = request.form
    employee = {'f_name': data['f_name'],
                'l_name': data['l_name'],
                'city': data['city'],
                'address': data['address'],
                'phone_number': data['phone_number']
                }
    x = db.devops.insert_one(employee)
    return redirect(url_for('get_stored_devops'))


@app.route("/remove/<name>", methods=['DELETE'])
def remove(name):
    db = get_db("employees")
    x = db.devops.delete_one({"f_name": name})
    return str(x.raw_result)


@app.route("/update/<name>/<new_phone>", methods=['POST'])
def update(name, new_phone):
    db = get_db("employees")
    x = db.devops.update_one({"f_name": name}, {"$set": {"phone_number": new_phone}})
    return str(x)


@app.route("/check")
def x_incremator(x):
    return x + 1


courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]


@app.route('/get', methods=('GET', 'POST'))
def index():
    db = get_db("Develeap")
    form = CourseForm()
    if form.validate_on_submit():
        course = {'title': form.title.data, 'description': form.description.data,
                  'price': form.price.data,
                  'available': form.available.data,
                  'level': form.level.data
                  }
        x = db.courses.update_one(course)
        return redirect(url_for('courses'))
    return render_template('index.html', form=form)


@app.route('/courses/')
def courses():
    db = get_db("Develeap")
    _courses = db.courses.find()
    courses_list = []
    for course in _courses:
        courses_list.append({"id": course["id"], "title": course["title"], "description": course["description"],
                             "price": course["price"], "available": course["available"], "level": course["level"]})
    return render_template('courses.html', courses_list=courses_list)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
