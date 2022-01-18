from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def get_all(cls):
        query = "select * from user;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for i in results:
            users.append(cls(i))
        return users
    
    @classmethod
    def create_one(cls, data):
        query = "insert into user (first_name, last_name, email) values (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query = "select * from user where id = %(id)s"
        results = connectToMySQL('users_schema').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def delete_one(cls, data):
        query = "delete from user where user.id = %(id)s"
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def update_one(cls, data):
        query = "update user set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s where id = %(id)s"
        result = connectToMySQL('users_schema').query_db(query, data)
        return result