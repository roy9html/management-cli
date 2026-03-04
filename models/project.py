class Project:
    def __init__(self, title, description, due_date, user):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user = user
    
    def to_dict(self):
        return{
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user": self.user
        }    
        
    def __str__(self):
        return f"{self.title} (Ownr: {self.user})"
        