from pymongo import MongoClient

class Breed:
    def __init__(self, key, name, info):
        self.key = key
        self.name = name
        self.info = info

    def save(self):
        client = MongoClient('localhost', 27017)
        db = client.dog_breed_db
        db.breeds.insert_one(self.__dict__)

    @staticmethod
    def get_breed_info(breed_name):
        client = MongoClient('localhost', 27017)
        db = client.dog_breed_db
        return db.breeds.find_one({"key": breed_name})
