class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

class Habit:
    def __init__(self, habit_id, name, description, start_date, category_id, user_id):
        self.habit_id = habit_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.category_id = category_id
        self.user_id = user_id

class HabitLog:
    def __init__(self, log_id, log_date, description, start_time, end_time, duration, user_id, habit_id):
        self.log_id = log_id
        self.log_date = log_date
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.user_id = user_id
        self.habit_id = habit_id