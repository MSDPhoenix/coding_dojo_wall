from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
db = 'coding_dojo_wall'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts = []
        self.comments = []

    @classmethod
    def get_by_id(cls,data):
        query = 'SELECT * FROM users WHERE id=%(user_id)s;'
        result = connectToMySQL(db).query_db(query,data)
        user = cls(result[0])
        return user

    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM users WHERE email=%(email)s;'
        result = connectToMySQL(db).query_db(query,data)
        user = cls(result[0])
        return user

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        result = connectToMySQL(db).query_db(query)
        users = []
        for row in result:
            user = User(row)
            users.append(user)
        return users

    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO users (first_name,last_name,email,password)
                VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
                '''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = '''
                UPDATE users
                SET xxx=%()s,xxx=%()s,xxx=%()s,xxx=%()s
                WHERE id=%(user_id)s;
                '''
        result = connectToMySQL(db).query_db(query,data)
        xxxx = xxxx
        return xxxx

    @classmethod
    def delete(cls,data):
        query = '''
                DELETE * FROM users
                WHERE id=%(user_id)s;
                '''
        return connectToMySQL(db).query_db(query,data)

    # @staticmethod
    # def validate(cls,data):
    #     query = '''

    #             '''
    #     result = connectToMySQL(db).query_db(query,data)
    #     xxxx = xxxx
    #     return xxxx

    # @staticmethod
    # def xxx(cls,data):
    #     query = '''

    #             '''
    #     result = connectToMySQL(db).query_db(query,data)
    #     xxxx = xxxx
    #     return xxxx




        