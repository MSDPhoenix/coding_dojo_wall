from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import app
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
db = 'coding_dojo_wall'

class Comment:
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.post_id = data['post_id']
        self.creator = None
        self.post = None

    @classmethod
    def get_comments_for_post(cls,data):
        query = '''
                SELECT * FROM comments 
                WHERE post_id=%(post_id)s
                ORDER BY created_at DESC;
                '''
        result = connectToMySQL(db).query_db(query,data)
        comments = []
        for row in result:
            comment = cls(row)
            user_data = {
                'user_id':row['user_id']
            }
            comment.creator = user.User.get_by_id(user_data)
            comments.append(comment)
        return comments

    # @classmethod
    # def get_by_email(cls,data):
    #     query = 'SELECT * FROM users WHERE email=%(email)s;'
    #     result = connectToMySQL(db).query_db(query,data)
    #     user = cls(result[0])
    #     return user

    # @classmethod
    # def get_all(cls):
    #     query = 'SELECT * FROM users;'
    #     result = connectToMySQL(db).query_db(query)
    #     users = []
    #     for row in result:
    #         user = User(row)
    #         users.append(user)
    #     return users

    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO comments (content,post_id,user_id)
                VALUES (%(content)s,%(post_id)s,%(user_id)s);
                '''
        return connectToMySQL(db).query_db(query,data)

    # @classmethod
    # def update(cls,data):
    #     query = '''
    #             UPDATE users
    #             SET xxx=%()s,xxx=%()s,xxx=%()s,xxx=%()s
    #             WHERE id=%(user_id)s;
    #             '''
    #     result = connectToMySQL(db).query_db(query,data)
    #     xxxx = xxxx
    #     return xxxx

    @classmethod
    def delete(cls,data):
        query = '''
                DELETE FROM comments
                WHERE id=%(comment_id)s;
                '''
        return connectToMySQL(db).query_db(query,data)
