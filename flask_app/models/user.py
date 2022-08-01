from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
db = 'coding_dojo_wall'
EMAIL_REGEX = re.compile(r'^[a-zA_Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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
        print("C")
        print(data)
        query = 'SELECT * FROM users WHERE id=%(user_id)s;'
        result = connectToMySQL(db).query_db(query,data)
        user = cls(result[0])
        return user

    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM users WHERE email=%(email)s;'
        result = connectToMySQL(db).query_db(query,data)
        if len(result) < 1:
            return False
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

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['first_name']) < 1:
            flash('First name required','register')
            is_valid = False
        elif len(data['first_name']) < 2:
            flash('First name must be at least 2 letters','register')
            is_valid = False
        elif not data['first_name'].isalpha():
            flash('First name must contain letters only','register')
            is_valid = False

        if len(data['last_name']) < 1:
            flash('Last name required','register')
            is_valid = False
        elif len(data['last_name']) < 2:
            flash('Last name must be at least 2 letters','register')
            is_valid = False
        elif not data['last_name'].isalpha():
            flash('Last name must contain letters only','register')
            is_valid = False

        if len(data['email']) < 1:
            flash('Email required','register')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash('Must use valid email format','register')
            is_valid = False
        elif User.get_by_email(data):
            flash('Email address already registered','register')
            is_valid = False

        if len(data['password']) < 1:
            flash('Password required','register')
            is_valid = False
        elif len(data['password']) < 8:
            flash('Password must be at least 8 characters','register')
            is_valid = False
        elif data['password'] != data['confirm_password']:
            flash('Password does not match confirm password','register')
            is_valid = False

        return is_valid

    # @staticmethod
    # def xxx(cls,data):
    #     query = '''

    #             '''
    #     result = connectToMySQL(db).query_db(query,data)
    #     xxxx = xxxx
    #     return xxxx




        