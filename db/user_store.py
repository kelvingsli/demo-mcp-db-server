import logging

from .dbconnection import DbConnection
from models.user import User

session = DbConnection().create_session()

class UserStore:

    def get_dbuser_codename(self, full_name: str):
        try:
            user = session.query(User).filter(User.full_name.ilike(f'%{full_name}%')).first()
            # Post.query.filter(Post.title.ilike('%some_phrase%'))
            return user
        except Exception as err:
            logging.error(err)
            raise err

    def insert_dbuser(self, full_name: str, code_name: str):
        try:
            user = User(full_name=full_name, code_name=code_name)
            session.add(user)
            session.commit()
        except Exception as err:
            logging.error(err)
            raise err

    def delete_dbuser(self, user_id: int):
        try:
            user = session.query(User).filter_by(id=user_id).first()
            session.delete(user)
            session.commit()
        except Exception as err:
            logging.error(err)
            raise err