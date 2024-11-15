class AuthenticationManager:
    def __init__(self):
        self.authenticated_users = []

    def authenticate_user(self, username, password):
        # Example authentication check
        if username == "admin" and password == "password":
            print("Authentication successful.")
            self.authenticated_users.append(username)
        else:
            print("Authentication failed.")

    def is_authenticated(self, username):
        return username in self.authenticated_users
