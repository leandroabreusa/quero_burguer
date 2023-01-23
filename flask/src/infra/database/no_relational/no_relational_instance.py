import os
from src.infra.database.no_relational.mongo import Mongo


class MongoInstance:
    def __init__(self):
        self.mongo = None
        self.mongo_uri = "mongodb://localhost:27017"
        self.mongo_database = "burguer"

    def connect(self) -> None:
        self.mongo = Mongo(
            self.mongo_uri, self.mongo_database
        )
        self.mongo.connect()

    def close(self) -> None:
        if self.mongo:
            self.mongo.disconnect()
            self.mongo = None



mongo_instance = MongoInstance()
