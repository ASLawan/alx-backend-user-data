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
        return False


    def authorization_header(self, request=None) -> str:
        """Authentiction header"""
        return None

    
    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user"""
        return None
