import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data = json.loads(self.get_response_body())
            
        occupation_list = [
                {'name': entry.get("name", ""), 'occupation': entry.get("occupation", "")}
                for entry in data
            ]

        return occupation_list
    
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"







