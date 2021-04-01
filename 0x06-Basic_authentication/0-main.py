#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth

a = Auth()
path = ['/api/v1/users', '/api/v1/status', '/api/v1/stats']
excluded_paths = excluded_paths = ["/api/v1/stat*"]

for p in path:
	print(a.require_auth(p, excluded_paths))