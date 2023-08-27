from flask import Blueprint, render_template, request, redirect
from . import db

todo = Blueprint("todo", __name__)

@todo.route("/", methods = ['POST', 'GET'])
def home():

    if request.method == 'POST':
        id = request.form.get("id")
        description = request.form.get('description')
        deadline = request.form.get('deadline')
        
        if id:
            db.cursor.execute(f"DELETE FROM todo WHERE id = {id}")
            db.conn.commit()
            print("Deleted record with id", id)
        else:
            db.cursor.execute("INSERT INTO todo (description, deadline) VALUES (%s, %s)", (description, deadline))
            db.conn.commit()
            print("Added todo")

        return redirect("/")
        
    if request.method == 'GET':
        db.cursor.execute("SELECT id, description, deadline deadline FROM todo")
        data = db.cursor.fetchall()
        print("Retrieved todos")
        return render_template("home.html", todos = data)     

    return render_template("home.html")