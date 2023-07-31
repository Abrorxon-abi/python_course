

def calculate_time(func):
    def wrapper(*args):
        func(*args)
    return wrapper


@calculate_time
def test_fn(val):
    if not val.isalnum():
        raise Exception('Invalid input type: need str or int')
    else:
        print(val)


test_fn(input('enter a text or number: '))
