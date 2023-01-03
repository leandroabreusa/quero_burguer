from pymongo import MongoClient, database
from pymongo.server_api import ServerApi
from typing import Any
from src.infra.database.no_relational.no_relational_database import (
    NoRelationalDatabase,
)
import datetime


class Mongo(NoRelationalDatabase):
    def __init__(self, connection_uri: str, database: str):
        self.connection_uri = connection_uri
        self.database = database
        self.client = None
        self.connected_database = None

    def connect(self) -> database.Database:
        print("connecting to mongo")

        self.client = MongoClient(self.connection_uri)
        self.connected_database = self.client[self.database]

        return self.connected_database

    def disconnect(self) -> None:
        if self.client:
            self.client.close()
            self.client = None

    def retry_connection(self) -> None:
        if not self.client:
            self.connect()

        try:
            self.client.server_info()

        except Exception as error:
            print("Retry mongo error", error)
            self.connect()

    def insert(self, collection: str, data: dict) -> Any:
        self.retry_connection()

        mongo_collection = self.connected_database[collection]

        try:
            data["timestamp"] = datetime.datetime.utcnow()

            mongo_inserted = mongo_collection.insert_one(data).inserted_id
            return mongo_inserted

        except Exception as error:
            print("Mongo insert error", error)
            return False

    def insert_specific_database(
        self, database: str, collection: str, data: dict
    ) -> Any:
        self.retry_connection()

        try:
            mongo_collection = self.client[database][collection]

            data["timestamp"] = datetime.datetime.utcnow()

            mongo_inserted = mongo_collection.insert_one(data).inserted_id
            return mongo_inserted

        except Exception as error:
            print("Mongo insert error", error)
            return False

    def update(self, collection: str, query: dict, new_values: dict) -> Any:
        self.retry_connection()

        mongo_collection = self.connected_database[collection]

        try:
            mongo_updated = mongo_collection.update_one(query, new_values)
            return mongo_updated

        except Exception as error:
            print("Mongo update error", error)
            return False

    def update_specific_database(
        self, database: str, collection: str, query: dict, new_values: dict
    ) -> Any:
        self.retry_connection()

        try:
            mongo_collection = self.client[database][collection]

            mongo_updated = mongo_collection.update_one(query, new_values)
            return mongo_updated

        except Exception as error:
            print("Mongo update error", error)
            return False

    def find(
        self, collection: str, query: dict
    ) -> Any:
        self.retry_connection()

        mongo_collection = self.connected_database[collection]

        try:
            mongo_updated = mongo_collection.find_one(query)
            return mongo_updated

        except Exception as error:
            print("Mongo find error", error)
            return False

    def find_specific_database(
        self, database: str, collection: str, query: dict
    ) -> Any:
        self.retry_connection()

        try:
            mongo_collection = self.client[database][collection]

            mongo_finded = mongo_collection.find(query)
            return mongo_finded

        except Exception as error:
            print("Mongo find error", error)
            return False
