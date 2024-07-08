#!/usr/bin/env python3
"""
    Module implementing BasicAuth class

"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class that extends Auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns base64 part of the Authorization header
        for Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]
