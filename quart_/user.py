class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def update_password(self, new_password):
        self.password = new_password
