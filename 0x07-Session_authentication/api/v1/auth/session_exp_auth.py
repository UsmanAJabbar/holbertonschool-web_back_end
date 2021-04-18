#!/usr/bin/env python3
"""Session Expiry Class File"""
from api.v1.auth.session_auth import SessionAuth

class SessionExpAuth(SessionAuth):
    """
    ---------------------
    CLASS: SessionExpAuth
    ---------------------
    """

    def __init__(self):
        """
        ------------------
        MAGIC METHOD: INIT
        ------------------
        """
        from os import environ
        self.session_duration = int(environ.get('SESSION_DURATION', 0))


    def create_session(self, user_id=None):
        """
        ----------------------
        METHOD: create_session
        ----------------------
        Description:
            Creates a new session, returning a new session ID
            from the parent class SessionAuth
        """
        session_id = super().create_session(user_id)
        if session_id:
            from datetime import datetime
            session_dictionary = {'user_id': user_id,
                                  'created_at': datetime.now()}
            self.user_id_by_session_id[session_id] = session_dictionary
            return session_id


    def user_id_for_session_id(self, session_id=None):
        """
        ------------------------------
        METHOD: user_id_for_session_id
        ------------------------------
        """
        session = self.user_id_by_session_id.get(session_id)
        if session:
            from datetime import timedelta as td, datetime as dt

            created_at = session.get('created_at')
            if created_at:
                if self.session_duration <= 0 or\
                   td(seconds=self.session_duration+created_at) >= dt.now():
                    return session.user_id