#!/usr/bin/env python3
"""Session Auth File"""
from .auth import Auth

class SessionAuth(Auth):
	"""
	------------------
	CLASS: SessionAuth
	------------------
	"""
	user_id_by_session_id = {}


	def create_session(self, user_id: str = None) -> str:
		"""
		----------------------
		METHOD: create_session
		----------------------
		Description:
			Creates a session with the user
			if logged in.
		"""
		if type(user_id) is str:
			from uuid import uuid4

			session_id = str(uuid4())
			self.user_id_by_session_id[session_id] = user_id
			return session_id
	
	def user_id_for_session_id(self, session_id: str = None) -> str:
		"""
		------------------------------
		METHOD: user_id_for_session_id
		------------------------------
		Description:
			Returns a user ID based off a given session ID
		"""
		if type(session_id) is str:
			return self.user_id_by_session_id.get(session_id)
	
	def current_user(self, request=None):
		"""
		--------------------
		METHOD: current_user
		--------------------
		Description:
			Identifies and returns a user based
			off a cookie value in the request.
		"""
		session_cookie = self.session_cookie(request)
		user_id = self.user_id_for_session_id(session_cookie)

		if user_id:
			from api.v1.views.users import User
			user = User.search({'id': user_id})
			if user:
				return user[0]
	
	def destroy_session(self, request=None):
		"""
		-----------------------
		METHOD: destroy_session
		-----------------------
		Description:
			Destroys a session
		"""
		session_id = self.session_cookie(request)
		user_id = self.user_id_for_session_id(session_id)
		if not request or not user_id:
			return False

		del self.user_id_by_session_id[session_id]
		return True