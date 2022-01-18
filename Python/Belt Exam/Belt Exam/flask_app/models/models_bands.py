from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from . import models_users, models_bands # could be removed

DATABASE = 'band_schema'

class Band:
    def __init__(self, data):
        self.id = data['id']
        self.band_name = data['band_name']
        self.music_genre = data['music_genre']
        self.home_city = data['home_city']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all_bands(cls):
        query = "select * from bands;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO bands (band_name, music_genre, home_city, user_id) VALUES (%(band_name)s, %(music_genre)s, %(home_city)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_band(band):
        is_valid = True
        if len(band['band_name']) < 3:
            flash("band_name must be at least 3 characters.", 'error_band_band_name')
            is_valid = False
        if len(band['music_genre']) < 2:
            flash("music_genre must be at least 2 characters.", 'error_band_music_genre')
            is_valid = False
        if len(band['home_city']) < 3:
            flash("home_city must be at least 3 characters.", 'error_band_home_city')
            is_valid = False
        return is_valid
    
    @classmethod
    def get_one_band(cls, data):
        query = "select * from bands where id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def delete(cls, data):
        query = "delete from bands where id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def update_one_band(cls, data):
        query = "update bands set band_name = %(band_name)s, music_genre = %(music_genre)s, home_city = %(home_city)s where id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_user_with_bands( cls , data ):
        query = "SELECT * FROM users LEFT JOIN bands ON bands.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL('bands').query_db( query , data )
        # results will be a list of topping objects with the band attached to each row. 
        user = cls( results[0] )
        for row_from_db in results:
            # Now we parse the band data to make instances of bands and add them into our list.
            band_data = {
                "id" : row_from_db["bands.id"],
                "band_name" : row_from_db["bands.name"],
                "music_genre" : row_from_db["bands.music_genre"],
                "home_city" : row_from_db["bands.home_city"],
                "created_at" : row_from_db["bands.created_at"],
                "updated_at" : row_from_db["bands.updated_at"]
            }
            user.bands.append( models_bands.band( band_data ))
        return user