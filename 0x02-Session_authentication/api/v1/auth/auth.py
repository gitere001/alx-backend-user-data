#!/usr/bin/env python3

"""
Auth class
"""
import os

from flask import request
from typing import List, TypeVar


class Auth:
    """Class Auth for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns True if the path requires authentication"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        # Normalize the path and excluded paths
        normalized_path = path.rstrip('/')
        normalized_excluded_paths = [
            excluded_path.rstrip('/') for excluded_path in excluded_paths
        ]
        # Check if the normalized path is in the list of normalized excluded
        # paths
        if normalized_path in normalized_excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Retrieves authorization header from a request"""
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user from the request"""
        return None

    def session_cookie(self, request=None):
        """session cookie method to retrieve cookie from request"""
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME', '_my_session_id')
        cookie = request.cookies.get(cookie_name, None)
        return cookie
