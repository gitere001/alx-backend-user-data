#!/usr/bin/env python3
""" Basic Authentication class	"""
from api.v1.auth.auth import Auth
from typing import Tuple


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
