from flask import Flask, render_template, request, redirect, url_for
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

todos = []
todo_counter = Counter('todo_total', 'Total To-Do actions', ['action'])

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
        todo_counter.labels(action="add").inc()
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
        todo_counter.labels(action="delete").inc()
    return redirect(url_for('index'))

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
