import requests

class AnimalDao:
    _instance = None
    API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AnimalDao, cls).__new__(cls)
        return cls._instance

    def get_animal_data(self, name):
        headers = {'X-Api-Key': 'qG3u4immV6Zg9pJdyM5LKT4VyJGLCoQ5YqwWyTEx'}
        response = requests.get(self.API_URL.format(name), headers=headers)
        if response.status_code == 200:
            return response.json()
        return None
