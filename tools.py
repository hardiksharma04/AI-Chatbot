from datetime import datetime, date

def get_time():
    return datetime.now().strftime("%I:%M %p")

def get_date():
    return date.today().strftime("%d-%m-%Y")

def say_hello():
    return "Hello Hardik! 👋 Welcome back."

def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation."