class User:
    def __init__(self, uid, name, email, password):
        self.uid = uid
        self.name = name
        self.email = email
        self.password = password
    
    def getUserName(self):
        return self.user_name

    def getEmail(self):
        return self.email
        
    def getUserPassword(self):
        return self.password