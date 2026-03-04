from models.user import User
from models.task import Task

def test_user():
    user = User("Alex", "alex@mail.com")
    assert user.name == "Alex"
    
    
def test_task_complete():
    task = Task("Build CLI", "CLI TOOL", "Alex")
    task.complete()
    assert task.status == "completed"
    
    
from models.user import User
from models.task import Task
    