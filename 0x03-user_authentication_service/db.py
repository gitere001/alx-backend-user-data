#!/usr/bin/env python3
"""DB module for the AirBnB clone project
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound
from typing import Union

from user import Base, User


class DB:
    """DB class to handle all the interactions with the database
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

    def find_user_by(self, **kwargs) -> Union[User, None]:
        """finds a user by a given criteria"""
        all_users = self._session.query(User)
        for key, value in kwargs.items():
            if hasattr(User, key):
                all_users = all_users.filter(getattr(User, key) == value)
        try:
            return all_users.one()
        except NoResultFound:
            return None

    def update_user(self, user_id: int, **kwargs) -> None:
        """updates a user by a given criteria"""
        user = self.find_user_by(id=user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            self._session.commit()
        else:
            raise NoResultFound('not found')
