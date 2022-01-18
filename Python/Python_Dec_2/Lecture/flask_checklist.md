# One time events
```
pip install pipenv
```
# Flask App Checklist

1. Create assignment
2. In the terminal navigate to our assignment location
3. install flask
```
pipenv install flask
```
   - make sure you se pipfile and pipfile.lock
4. Launch our virtual environment
```
pipenv shell
or
python -m pipenv shell
or
python3 -m pipenv shell
```
5. server.py file
    ```py
    from flask_app import app

    #this should be at the bottom
    if __name__=="__main__":
        app.run(debug=True)
    ```
6. Test server.py file
    ```

7. create file structure
    - flask_app
        - config
            - mysqlconnection.py 
        - controllers
            - contoller_user.py 
        - models
            - model_user.py 
        - templates
            - index.html
            - [stylesheet](#html-page)
        - static
            - css
                - style.css
            - img
            - js
                - script.js
        - \_\_init__.py
    - pipfile
    - pipfile.lock
    - server.py   
8. Mysqlconnection.py
    ```py
    # a cursor is the object we use to interact with the database
    import pymysql.cursors
    # this class will give us an instance of a connection to our database
    class MySQLConnection:
        def __init__(self, db):
            # change the user and password as needed
            connection = pymysql.connect(host = 'localhost',
                                        user = 'root', 
                                        password = 'root', 
                                        db = db,
                                        charset = 'utf8mb4',
                                        cursorclass = pymysql.cursors.DictCursor,
                                        autocommit = True)
            # establish the connection to the database
            self.connection = connection
        # the method to query the database
        def query_db(self, query, data=None):
            with self.connection.cursor() as cursor:
                try:
                    query = cursor.mogrify(query, data)
                    print("Running Query:", query)
        
                    cursor.execute(query)
                    if query.lower().find("insert") >= 0:
                        # INSERT queries will return the ID NUMBER of the row inserted
                        self.connection.commit()
                        return cursor.lastrowid
                    elif query.lower().find("select") >= 0:
                        # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                        result = cursor.fetchall()
                        return result
                    else:
                        # UPDATE and DELETE queries will return nothing
                        self.connection.commit()
                except Exception as e:
                    # if the query fails the method will return FALSE
                    print("Something went wrong", e)
                    return False
                finally:
                    # close the connection
                    self.connection.close() 
    # connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
    def connectToMySQL(db):
    return MySQLConnection(db)
    ```
9.  models file
    ```py
    # import the function that will return an instance of a connection
    from mysqlconnection import connectToMySQL
    # model the class after the friend table from our database
    class User:
        def __init__( self , data ):
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.occupation = data['occupation']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query) # return a list of dictionaries
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for dict in results:
            users.append( cls(dict) )
        return friends
    ```
10. \_\_init__.py file
    ```py
    from flask import Flask
    app = Flask(__name__)
    app.secret_key = "something"
    ```
11. controllers file
    ```py
    from flask_app import app
    from flask import render_template, redirect, session, request

    @app.route('/')
    def hello_world():
        return 'Hello World!'
    @app.route('/success')
    def success();
        return 'success'
    ```
## html page
- link stylesheet

```py
results = [
    {'first_name': 'tyler'}
]

first_name = results[0]['first_name']

```
///////////////new_project_folder $ pipenv install PyMySQL flask
