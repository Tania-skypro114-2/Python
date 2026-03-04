import requests
from dotenv import load_dotenv
import os


class YouGile:
    def __init__(self):
        load_dotenv()
        self.url = "https://www.yougile.com/api-v2"

    def create_project(self, title):
        project = {
            'title': title
        }
        my_headers = {}
        my_headers['Authorization'] = 'Bearer ' + os.getenv("key")
        my_headers['Content-type'] = 'application/json'
        resp = requests.post(self.url + '/projects',
                             json=project, headers=my_headers)
        return resp

    def get_project_id(self, id):
        my_headers = {}
        my_headers['Authorization'] = 'Bearer ' + os.getenv("key")
        my_headers['Content-type'] = 'application/json'
        resp = requests.get(self.url + '/projects/' + str(id),
                            headers=my_headers)
        return resp

    def put_project_id(self, id, new_title):
        my_headers = {}
        my_headers['Authorization'] = 'Bearer ' + os.getenv("key")
        my_headers['Content-type'] = 'application/json'
        project = {
            'title': new_title
        }
        resp = requests.put(self.url + '/projects/' + str(id),
                            json=project, headers=my_headers)
        return resp
