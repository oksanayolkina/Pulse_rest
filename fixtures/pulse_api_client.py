import requests

class PulseAPI:

    def __init__(self, resource):
        self.host = "pulse-rest-testing.herokuapp.com"
        self.resource = resource
        self.url = 'http://{}/{}/'.format(self.host, self.resource)

    def create_object(self, object):
        obj_data = object.get_dict_without_id()
        response = requests.post(self.url, data=obj_data)
        if response.status_code == 201:
            object.set_id(response.json()["id"])
        return response

    # def get_objects(self):
    #     response = requests.get(self.url)
    #     res = response.text()
    #     return res

    def get_object(self, object):
        id = object.get_id()
        response = requests.get(self.url + str(id) + "/")
        return response

    def modife_object(self, object):
        id = object.get_id()
        obj_data = object.get_dict_with_id()
        response = requests.put(self.url + str(id) + "/", data=obj_data)
        return response

    def delete_object(self, object):
        id = object.get_id()
        response = requests.delete(self.url + str(id) + "/")
        return response