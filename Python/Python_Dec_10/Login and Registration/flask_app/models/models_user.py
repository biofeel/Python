from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'user_login_schema'

class User:
    def __init__(self, data):
            self.id = data['id']
            self.first_name = data['first_name']
            self.lasst_name = data['last_name']
            self.email = data['email']
            self.password = data['password']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("Name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user['email']) < 2:
            flash("Email cannot be blank!", 'register')
            is_valid = False
        if len(user['password']) < 3:
            flash("password must be at least 3 characters.", 'register')
            is_valid = False
        if user['confirm password'] != user['password']:
            flash(" password does not match.", 'register')
            is_valid = False    
        return is_valid

#-------1----------
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

#-------2----------
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user(cls, data):
        query = "select * from users where id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        # Didn't find a matching user
        return cls(result[0])

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DATABASE = 'user_login_schema'

class User:
    def __init__(self, data):
            self.id = data['id']
            self.first_name = data['first_name']
            self.lasst_name = data['last_name']
            self.email = data['email']
            self.password = data['password']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("Name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user['email']) < 2:
            flash("Email cannot be blank!", 'register')
            is_valid = False
        if len(user['password']) < 3:
            flash("password must be at least 3 characters.", 'register')
            is_valid = False
        if user['confirm password'] != user['password']:
            flash(" password does not match.", 'register')
            is_valid = False    
        return is_valid

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user(cls, data):
        query = "select * from users where id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])
