#!/usr/bin/env python3
"""authenication model"""
import bcrypt
from db import DB
import uuid
from user import User
from typing import Union


def _hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    byte_passwrd = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte_passwrd, salt)
    return hashed_password


def _generate_uuid() -> str:
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        """Initialize a new Auth instance
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user and return the user"""
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {user.email} already exists.")
        hashed_password = _hash_password(password)
        self._db.add_user(email, hashed_password)

        return self._db.find_user_by(email=email)

    def valid_login(self, email: str, password: str) -> bool:
        """check if the user exists and the password is correct"""
        user = self._db.find_user_by(email=email)
        if user:
            byte_password = password.encode('utf-8')
            hashed_password = user.hashed_password
            return bcrypt.checkpw(byte_password, hashed_password)
        return False

    def create_session(self, email: str) -> Union[str, None]:
        """create a new session for a user"""
        user = self._db.find_user_by(email=email)
        if user:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Get a user from a session id"""
        if session_id is None:
            return None
        user = self._db.find_user_by(session_id=session_id)
        if not user:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """destroy a session for a user"""
        if user_id in None:
            return None
        self._db.update_user(user_id, session_id=None)
