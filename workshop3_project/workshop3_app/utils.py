# workshop3_app/utils.py

def serial_sum(*args):
    if len(args) == 1:
        n = args[0]
        return sum(range(1, n + 1))
    elif len(args) == 2:
        start, end = args[0], args[1]
        return sum(range(start, end + 1))
    else:
        return None  # Handle invalid input
