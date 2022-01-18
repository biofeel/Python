from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from . import models_sightings, models_users # could be removed

DATABASE = 'sasquatch_schema'

class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.date_of_siting = data['date_of_siting']
        self.number_of_sasquatches = data['number_of_sasquatches']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all_sightings(cls):
        query = "select * from sightings;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO sightings (location, what_happened, date_of_siting, number_of_sasquatches, user_id) VALUES (%(location)s, %(what_happened)s, %(date_of_siting)s, %(number_of_sasquatches)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_sighting(sighting):
        is_valid = True
        if len(sighting['location']) < 3:
            flash("Location must be at least 3 characters.", 'error_sighting_location')
            is_valid = False
        if len(sighting['what_happened']) < 3:
            flash("what_happened must be at least 3 characters.", 'error_sighting_what_happened')
            is_valid = False
        if len(sighting['date_of_siting']) < 3:
            flash("date_of_siting must be at least 3 characters.", 'error_sighting_date_of_siting')
            is_valid = False
        return is_valid
    
    @classmethod
    def get_one_sighting(cls, data):
        query = "select * from sightings where id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def delete(cls, data):
        query = "delete from sightings where id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def update_one_sighting(cls, data):
        query = "update sightings set location = %(location)s, number_of_sasquatches = %(number_of_sasquatches)s, what_happened = %(what_happened)s, date_of_siting = %(date_of_siting)s where id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)