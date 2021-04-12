#!/usr/bin/env python3
from app import app, AUTH
from re import search
user = AUTH.register_user(
    'test@test.com',
    'test'
)
reset_token = AUTH.get_reset_password_token(
    'test@test.com'
    )
regex = r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
# check if user is a uuid 
if not search(regex, reset_token):
    print("The reset token is not a UUID")
    exit(0)
print("OK", end='')