# jenkins admin - 9f6e626a65e54ffabdadbe2b1a64e250


# {% extends 'layout.html' %}
# {% block body %}
#         <h2>Users</h2>    
# {% endblock body %}
# {% block content %}
# {% for user in user %}
# {{ username.text }}
# <br>
# {% endfor %}
# {% endblock content %}


# @app.route('/update/<int:pk>', methods=['GET', 'POST'])
# def update(pk):
#     todo = Todo.query.get(pk)
#     projects = Project.query.all()
#     form = AddToDo()
#     form.proj_id.choices.extend([(project.pk, str(project)) for project in projects])
#     if request.method == 'POST':
#         todo.title = form.title.data
#         todo.desc = form.desc.data
#         todo.status = form.status.data
#         todo.proj_id = int(form.proj_id.data)
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template('add_todo.html', form = form, ptitle = "Update Item")

# @app.route('/delete/<int:i>')
# def delete(i):
#     todo = Todo.query.get(i)
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect(url_for('home'))
