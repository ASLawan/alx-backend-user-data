#!/usr/bin/env python3
"""
    Module implementing end-to-end integration tests

"""
import requests


BASE_URL = "http://127.0.0.1:5000"


def register_user(email: str, password: str) -> None:
    """Tests the register_user end point"""
    rsps = requests.post(f"{BASE_URL}/users",
                         data={"email": email, "password": password})
    assert rsps.status_code == 200
    assert rsps.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Tests user login credentials - wrong password"""
    rsps = requests.post(f"{BASE_URL}/sessions",
                         data={"email": email, "password": password})
    assert rsps.status_code == 401


def log_in(email: str, password: str) -> str:
    """Tests user login credentials- correct login credentials"""
    rsps = requests.post(f"{BASE_URL}/sessions",
                         data={"email": email, "password": password})
    assert rsps.status_code == 200
    assert rsps.json().get("email") == email
    assert rsps.json().get("message") == "logged in"
    return rsps.cookies.get("session_id")


def profile_unlogged() -> None:
    """Tests user profile end point - unlogged profile"""
    rsps = requests.get(f"{BASE_URL}/profile")
    assert rsps.status_code == 403


def profile_logged(session_id: str) -> None:
    """Tests user profile end point - logged profile"""
    cookies = {"session_id": session_id}
    rsps = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    assert rsps.status_code == 200
    assert "email" in rsps.json()


def log_out(session_id: str) -> None:
    """Tests user logout from session"""
    cookies = {"session_id": session_id}
    rsps = requests.delete(f"{BASE_URL}/sessions", cookies=cookies)
    assert rsps.status_code == 200


def reset_password_token(email: str) -> str:
    """Tests the password reset token end point"""
    rsps = requests.post(f"{BASE_URL}/reset_password", data={"email": email})
    assert rsps.status_code == 200
    return rsps.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests the password reset end point"""
    rsps = requests.put(f"{BASE_URL}/reset_password",
                        data={"email": email,
                              "reset_token": reset_token,
                              "new_password": new_password
                              })
    assert rsps.status_code == 200
    assert rsps.json() == {"email": email, "message": "Password updated"}


EMAIL = "lawan@travel.com"
PASSWD = "Sewoyebaa"
NEW_PASSWD = "TrAvelCEO"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
