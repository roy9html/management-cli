class Task:

    def __init__(self, title, project, assigned_to, status="pending"):
        self.title = title
        self.project = project
        self.assigned_to = assigned_to
        self.status = status
        

    def complete(self):
        self.status = "completed"
        

    def to_dict(self):
        return {
            "title": self.title,
            "project": self.project,
            "assigned_to": self.assigned_to,
            "status": self.status
        }
        
        

    def __str__(self):
        return f"{self.title} - {self.status}"