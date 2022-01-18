from flask_app.config.mysqlconnection import connectToMySQL
from . import models_ninja 

DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "select * from dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def create_dojo(cls, data):
        query = 'insert into dojos (name) values (%(name)s);'
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def get_one_dojo(cls, data:dict):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    
    @classmethod
    def get_dojos_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id Where dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "dojo_id" : row_from_db["id"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( models_ninja.Ninja( ninja_data ) )
        return dojo
