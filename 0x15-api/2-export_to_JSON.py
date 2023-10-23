#!/usr/bin/python3
"""this model is my firt time using REST API"""
import json
from sys import argv
from urllib import request


def to_json(argv):
    tsks_id = request.urlopen(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv))
    user_name = request.urlopen(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv))

    res_body = tsks_id.read()
    user_body = user_name.read()

    json_dict = json.loads(res_body.decode("utf-8"))
    json_user = json.loads(user_body.decode("utf-8"))

    file_name = '{}.json'.format(argv)

    task_dict = {}
    line = []

    for idx in range(0, len(json_dict)):
        task_dict['task'] = json_dict[idx]['title']
        task_dict['completed'] = json_dict[idx]['completed']
        task_dict['username'] = json_user['username']
        line.append(task_dict)

    user_task = {}

    user_task[json_user['id']] = line
    object_json = json.dumps(user_task)

    with open(file_name, 'w') as json_f:
        json_f.write(object_json)
    json_f.close()


if __name__ == "__main__":
    if len(argv) == 2:
        to_json(argv=argv[1])
