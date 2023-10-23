#!/usr/bin/python3
"""this model is my firt time using REST API"""
import json
from sys import argv
from urllib import request


def to_json():
    """Using what you did in the task #0, extend your
    Python script to export data in the JSON format."""
    tsks_id = request.urlopen(
        'https://jsonplaceholder.typicode.com/todos/')
    user_name = request.urlopen(
        'https://jsonplaceholder.typicode.com/users/')

    res_body = tsks_id.read()
    user_body = user_name.read()

    json_dict = json.loads(res_body.decode("utf-8"))
    json_user = json.loads(user_body.decode("utf-8"))

    file_name = 'todo_all_employees.json'
    user_task = {}
    for idx in range(0, len(json_user)):
        line = []
        for jdx in range(0, len(json_dict)):
            task_dict = {}
            if json_dict[jdx]['userId'] == json_user[idx]['id']:
                task_dict['username'] = json_user[idx]['username']
                task_dict['task'] = json_dict[jdx]['title']
                task_dict['completed'] = json_dict[jdx]['completed']
                line.append(task_dict)
        user_task[json_user[idx]['id']] = line

    object_json = json.dumps(user_task, indent=4)

    with open(file_name, 'w') as json_f:
        json_f.write(object_json)
    json_f.close()


if __name__ == "__main__":
    to_json()
