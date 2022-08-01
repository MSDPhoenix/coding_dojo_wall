from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models import user,comment
bcrypt = Bcrypt(app)
db = 'coding_dojo_wall'

class Post:
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None
        self.comments = []

    # @classmethod
    # def get_by_id(cls,data):
    #     query = 'SELECT * FROM users WHERE id=%(user_id)s;'
    #     result = connectToMySQL(db).query_db(query,data)
    #     user = cls(result[0])
    #     return user

    # @classmethod
    # def get_by_email(cls,data):
    #     query = 'SELECT * FROM users WHERE email=%(email)s;'
    #     result = connectToMySQL(db).query_db(query,data)
    #     user = cls(result[0])
    #     return user

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM posts ORDER BY created_at DESC;'
        result = connectToMySQL(db).query_db(query)
        posts = []
        for row in result:
            post = Post(row)
            post.creator = user.User.get_by_id(row)
            comment_data =  {
                'post_id':row['id']
                }
            post.comments = comment.Comment.get_comments_for_post(comment_data)
            posts.append(post)
        return posts


    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO posts (content,user_id)
                VALUES (%(content)s,%(user_id)s);
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
                DELETE FROM posts
                WHERE id=%(post_id)s;
                '''
        return connectToMySQL(db).query_db(query,data)

    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['content']) < 1:
            flash('* Post content must not be blank','post')
            is_valid=False
        return is_valid
