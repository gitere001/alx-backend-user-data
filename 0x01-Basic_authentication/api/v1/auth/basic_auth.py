#!/usr/bin/env python3
""" Basic Authentication class	"""
from api.v1.auth.auth import Auth


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
