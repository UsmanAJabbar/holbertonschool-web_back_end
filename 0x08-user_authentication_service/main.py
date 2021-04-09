#!/usr/bin/env python3
""" Unit Test file """
from requests import get, post, put, delete
import requests
ENDPOINT = 'http://localhost:5000'


def register_user(email: str, password: str) -> None:
    """ Register user """
    ping = post(f'{ENDPOINT}/users', data=dict(email=email, password=password))
    assert ping.status_code == 200, 'Register Fail'


def log_in_wrong_password(email: str, password: str) -> None:
    """ Login Bad Password """
    ping = post(f'{ENDPOINT}/sessions', data=dict(email=email,
                                                  password=password))
    assert ping.status_code == 401, 'Logged in with the bad pass'


def log_in(email: str, password: str) -> str:
    """ Login Good Password """
    ping = post(f'{ENDPOINT}/sessions', data=dict(email=email,
                                                  password=password))
    assert ping.status_code == 200, 'Good login failed'
    return ping.cookies['session_id']


def profile_unlogged() -> None:
    """ Unknown Profile """
    ping = get(f'{ENDPOINT}/profile')
    assert ping.status_code == 403, 'No session ID got through'


def profile_logged(session_id: str) -> None:
    """ Profile with a session ID """
    ping = get(f'{ENDPOINT}/profile', cookies=dict(session_id=session_id))
    assert ping.status_code == 200, 'Failed to find a user with the session ID'


def log_out(session_id: str) -> None:
    """ Logout Session """
    ping = delete(f'{ENDPOINT}/sessions', cookies=dict(session_id=session_id))
    assert ping.status_code != 403, 'Failed to logout user'


def reset_password_token(email: str) -> str:
    """ Generate and return a password token via API """
    ping = post(f'{ENDPOINT}/reset_password', data=dict(email=email))
    assert ping.status_code == 200, 'Failed to generate a reset token'
    return ping.json()['reset_token']


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Updates a user containing a reset token with a new password """
    ping = put(f'{ENDPOINT}/reset_password',
               data=dict(email=email,
                         reset_token=reset_token,
                         new_password=new_password))
    assert ping.status_code == 200, 'Failed to update the password'


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

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
