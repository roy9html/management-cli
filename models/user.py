class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email
        }

    def __str__(self):
        return f"{self.name} - {self.email}"