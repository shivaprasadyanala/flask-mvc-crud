# import json
from flask import request, render_template, redirect, url_for, Flask, jsonify
from models.student import student, db
from services.student_service import create_logic


def index():
    users = student.query.all()
    # users = db.session.execute(db.select(student)).scalars()
    # for u in users:
    #     print(u.name)
    #     print(u.age)
    #     print(u.location)
    return render_template('index.html', students=users)


def create():
    create_logic()


# insert data into table.
def insert():
    if request.method == 'POST':
        s = student(
            name=request.form['name'],
            age=request.form['age'],
            location=request.form['location']
        )
        db.session.add(s)
        db.session.commit()
        return redirect(url_for("blueprint.index"))


def delete(id):
    user = db.get_or_404(student, id)
    # user = student.query.filter_by(id=id).first()
    # if request.method == "POST":
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("blueprint.index"))
    # return "delete succesfull"


def add():
    return render_template('add.html')


def edit(id):
    user = db.get_or_404(student, id)
    # cur.close()
    print(user)
    return render_template('edit.html', students=user)


def update(id):
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        location = request.form['location']
        stu = student.query.filter_by(id=id).first()

        name = request.form['name'],
        age = request.form['age'],
        location = request.form['location']
        stu.name = name
        stu.age = age
        stu.location = location
        db.session.add(stu)
        db.session.commit()
        return redirect(url_for("blueprint.index"))
