class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.categories = []
        self.habits = []

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"


class Category:
    def __init__(self, name):
        self.name = name
        self.habits = []

    def __str__(self):
        return self.name


class Habit:
    def __init__(self, name, description, start_date, category):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.category = category
        self.logs = []

    def __str__(self):
        return f"Habit: {self.name}, Category: {self.category.name}"


class HabitLog:
    def __init__(self, log_date, description, start_time, end_time, duration):
        self.log_date = log_date
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration

    def __str__(self):
        return f"Date: {self.log_date}, Description: {self.description}, Duration: {self.duration} minutes"
