#!/usr/bin/env python3
""" Basic Authentication class	"""
from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar
from api.v1.views.users import User
import base64


class BasicAuth(Auth):
    """class BasicAuth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the base64 authorization header from the given authorization
        header.

        Args:
            authorization_header (str): The authorization header to extract
            the base64 authorization header from.

        Returns:
            str: The extracted base64 authorization header, or None if the
            authorization header is None, not a string, or does not start with
            'Basic '.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """
        Decodes a Base64 string.

        Args:
            base64_authorization_header (str): The Base64 string to decode.

        Returns:
            str: The decoded value of the Base64 string as a UTF-8 string, or
            None if the input is invalid.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> Tuple[str, str]:
        """ Extracts user email and password from the Base64 decoded string """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string into email and password
        credentials = decoded_base64_authorization_header.split(':', 1)

        # Return the extracted email and password
        return credentials[0], credentials[1]

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Returns a User instance based on email and password """
        # Check validity of inputs
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        if user_email is None or user_pwd is None:
            return None

        # Search for the user by email
        users = User.search({'email': user_email})
        if not users:
            return None

        # Check if the user with the given email exists
        user = users[0]

        # Verify the password
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User instance based on a received request
        """
        Auth_header = self.authorization_header(request)
        if Auth_header is not None:
            token = self.extract_base64_authorization_header(Auth_header)
            if token is not None:
                decoded = self.decode_base64_authorization_header(token)
                if decoded is not None:
                    email, pword = self.extract_user_credentials(decoded)
                    if email is not None:
                        return self.user_object_from_credentials(email, pword)
        return
