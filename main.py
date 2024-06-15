from api import get_users, get_todos
from utils import is_fancode_city, calculate_completion_percentage

def main():
    users = get_users()
    todos = get_todos()
    
    fancode_users = [
        user for user in users 
        if is_fancode_city(user['address']['geo']['lat'], user['address']['geo']['lng'])
    ]
    
    print("Users from FanCode city with more than 50% tasks completed:")
    
    for user in fancode_users:
        completion_percentage = calculate_completion_percentage(todos, user['id'])
        if completion_percentage > 50:
            print(f"User: {user['name']} - Completed: {completion_percentage:.2f}%")
            
if __name__ == "__main__":
    main()
