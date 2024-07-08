#!/urs/bin/env python3
"""
    Module implementing Auth class

"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Manages the API authentiction"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Requires authentication"""
        if path is None:
            return True
        if not excluded_paths:
            return True
        if not path.endswith('/'):
            path += "/"
        for excluded_path in excluded_paths:
            if excluded_path == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authentiction header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user"""
        return None