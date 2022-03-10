from flask import Flask, request, jsonify, abort, Response
from json import dumps

from User.User import User
from Entry.Entry import Entry
from List.List import TodoList
import uuid 

# macht sachen
def default(o):
    return o._asdict()

# initialisiere Flask-Server
app = Flask(__name__)

# create unique id for lists, users, entries
user_id_johnny = uuid.uuid4()
user_id_bode = uuid.uuid4()
user_id_kevin = uuid.uuid4()
todo_list_1_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'
todo_list_2_id = '3062dc25-6b80-4315-bb1d-a7c86b014c65'
todo_list_3_id = '44b02e00-03bc-451d-8d01-0c67ea866fee'
todo_1_id = uuid.uuid4()
todo_2_id = uuid.uuid4()
todo_3_id = uuid.uuid4()
todo_4_id = uuid.uuid4()

user = [
    User("Hilberink", "Jonas", "jonas.hilberink@gsits.de"),
    User("Rieping", "Lea", "lea.rieping@gsits.de"),
    User("Bode", "Bode", "Bode.Bode@Bode.Bode")
    ]

list =  [
    TodoList("Trinken"),
    TodoList("Sport")
    ]


entry = [
    Entry("Bär", list[0], "Jonas"),
    Entry("Veltins", list[1], "Johnny"),
    Entry("Fußball", list[1], "Manuel")
    ]


# add some headers to allow cross origin access to the API on this server, necessary for using preview in Swagger Editor!
@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


# define endpoint for getting and deleting existing todo lists
@app.route('/list/<list_id>', methods=['GET', 'DELETE'])
def handle_list(list_id):
    # find todo list depending on given list id
    list_item = None
    for l in list:
        if list['id'] == list_id:
            list_item = l
            break
    # if the given list id is invalid, return status code 404
    if not list_item:
        abort(404)
    if request.method == 'GET':
        # find all todo entries for the todo list with the given id
        print('Returning todo list...')
        return jsonify([i for i in entry if i.id == list_id])
    elif request.method == 'DELETE':
        # delete list with given id
        print('Deleting todo list...')
        list.remove(list_item)
        return '', 200


# define endpoint for adding a new list
@app.route('/list', methods=['POST'])
def add_new_list():
    # make JSON from POST data (even if content type is not set correctly)
    new_list = request.get_json(force=True)
    print('Got new list to be added: {}'.format(new_list))
    # create id for new list, save it and return the list with id
    new_list['id'] = 4
    list.append(new_list)
    return Response(dumps(new_list, default=default),status=200, mimetype='appliaction/json')

# define endpoint for getting all lists
@app.route('/lists', methods=['GET'])
def get_all_lists():
    return Response(dumps(list, default=default),status=200, mimetype='appliaction/json')

# define endpoint for adding Entrys to a ToDo List 
@app.route('/list/<list_id>/entry', methods=['POST'])
def add_new_entry(entry_id):
    # make JSON from POST data (even if content type is not set correctly)
    new_entry = request.get_json(force=True)
    print('Got new entry to be added: {}'.format(new_entry))
    # create id for new list, save it and return the list with id
    new_entry['id'] = 3
    list.append(new_entry)
    return Response(dumps(new_entry, default=default),status=200, mimetype='appliaction/json')

# define endpoint for update Entrys 
@app.route('/list/{list_id}/entry/{entry_id}', methods=['POST', 'DELETE'])
def handle_entry(entry_id):
    entry_item = None
    # make JSON from POST data (even if content type is not set correctly)
    if request.method == 'POST':
        # find all todo entries for the todo list with the given id
        print('Returning todo list...')
        entry = request.get_json(force=True)
        entry_item = entry
        print('Updated Entry: {}'.format(entry))
        list.append(entry)
        return Response(dumps(entry, default=default),status=200, mimetype='appliaction/json')
    elif request.method == 'DELETE':
        # delete list with given id
        print('Deleting todo list...')
        list.remove(entry_item)
        return '', 200

# define endpoint for getting all user
@app.route('/users', methods=['GET'])
def get_all_users():
    return Response(dumps(user, default=default),status=200, mimetype='appliaction/json')

# define endpoint for adding a new user
@app.route('/user', methods=['POST'])
def add_new_user():
    # make JSON from POST data (even if content type is not set correctly)
    new_user = request.get_json(force=True)
    print('Got new user to be added: {}'.format(new_user))
    # create id for new list, save it and return the list with id
    new_user['id'] = 3
    user.append(new_user)
    return Response(dumps(new_user, default=default),status=200, mimetype='appliaction/json')

# define endpoint for delete user
@app.route('/user/{user_id}', methods=['DELETE'])
def delete_user(user_id):
    user_item = None
    for u in user:
        if user.id == user_id:
            user_item = u
            break
    # delete user with given id
        print('Deleting user...')
        user.remove(user_item)
        return '', 200


if __name__ == '__main__':
    # start Flask server
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

