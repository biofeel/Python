from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from . import models_users, models_recipes # could be removed

DATABASE = 'recipes_schema'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cook_time = data['cook_time']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all_recipes(cls):
        query = "select * from recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name, description, instruction, cook_time, date_made, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(cook_time)s, %(date_made)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters.", 'error_recipe_name')
            is_valid = False
        if len(recipe['description']) < 3:
            flash("description must be at least 3 characters.", 'error_recipe_description')
            is_valid = False
        if len(recipe['instruction']) < 3:
            flash("instruction must be at least 3 characters.", 'error_recipe_instruction')
            is_valid = False
        if len(recipe['date_made']) < 3:
            flash("date_made must be at least 2 characters.", 'error_recipe_date_made')
            is_valid = False
        if len(recipe['cook_time']) < 2:
            flash("cook_time must be at least 3 characters.", 'error_recipe_cook_time')
            is_valid = False
        return is_valid
    
    @classmethod
    def get_one_recipe(cls, data):
        query = "select * from recipes where id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def delete(cls, data):
        query = "delete from recipes where id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def update_one_recipe(cls, data):
        query = "update recipes set name = %(name)s, cook_time = %(cook_time)s, description = %(description)s, instruction = %(instruction)s, date_made = %(date_made)s where id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)