def is_fancode_city(lat, lng):
    return -40 < float(lat) < 5 and 5 < float(lng) < 100

def calculate_completion_percentage(todos, user_id):
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    if not user_todos:
        return 0
    completed_todos = [todo for todo in user_todos if todo['completed']]
    return (len(completed_todos) / len(user_todos)) * 100
