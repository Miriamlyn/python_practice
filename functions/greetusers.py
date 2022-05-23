#named blocks of codes designed to do specific job
#docstrings is comment that describes what a function does and has a triple quote sign 
# def: informs python that you're defining a function.


def greet_users():
    """Display a simple greeting."""
    print("Hello!")

greet_users()

#you can pass arguments inside a function
def greet_users2(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}! ")

greet_users2('Eric')


def learn_functions(Subject):
    """Display what user is learning"""
    print(f"Amaka is learning, {Subject.title()} ")

learn_functions("functions")