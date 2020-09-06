from flask import render_template, url_for, request, redirect
from app import app, db
from datetime import datetime
from models import Todo

@app.route("/", methods=['POST','GET'])
def main():
  if request.method == "POST":
    task_content = request.form['content']
    new_task = Todo(content=task_content)
    try:
      db.session.add(new_task)
      db.session.commit()
      return redirect('/')
    except:
      return 'Oops! There was an issue adding your task'
  else:
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', tasks = tasks)

@app.route("/complete/<int:id>")
def complete(id):
  task_to_complete = Todo.query.get_or_404(id)
  try:
    task_to_complete.date_completed = datetime.now()
    db.session.commit()
    return redirect("/")
  except:
    return 'Oops! There was an issue completing your task'

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
  task = Todo.query.get_or_404(id)
  if request.method == "POST":
    task.content = request.form['content']
    try:
      db.session.commit()
      return redirect("/")
    except:
      return 'Oops! There was an issue updating your task'
  else:
    return render_template('update.html', task=task)

@app.route("/delete/<int:id>")
def delete(id):
  task_to_delete = Todo.query.get_or_404(id)
  try:
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')
  except:
    return 'Oops! There was an issue deleting your task'