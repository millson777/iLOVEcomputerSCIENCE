class User:
    def __init__(self, username, email, ss, pass):
        """ 
        username - string
        email - class Email
        SS# - class Social
        hash - class Hash  
        """
        self.username = username
        self.email = email
        self.ss = ss
        self.pass = pass
  
    def  __str__(self):
        """
        return the username, email, and social strings in a nice readable way
        """
        return str(self.username) + " is a user with email address " + self.email + ".\n" + \
                  
