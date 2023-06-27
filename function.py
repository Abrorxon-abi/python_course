from datetime import date


def merge_lists_to_dict(list1, list2):
    merged = zip(list1, list2)
    return dict(merged)


keys = [1, 2, 4]
values = ['qwe', 'fas', 'car']
print(merge_lists_to_dict(keys, values))


# ========================================


def merge_lists_to_dict(keys, values):
    merged = zip(keys, values)
    return dict(merged)


keys = [1, 2, 4]
print(merge_lists_to_dict(keys, values=['qwe', 'fas', 'car']))


# ========================================


def get_post_info(posts_qty, name):
    info = f'{name} wrote {posts_qty} posts'
    return info


info = get_post_info(name='Vovka', posts_qty=15)
print(info)


# ========================================


def get_posts_info(**person):
    # print(person)

    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts"
    )

    # info = f"{person['name']} wrote {person['posts_qty']} posts"

    return info


info = get_posts_info(name='Vovka', posts_qty=25)
print(info)


# ========================================


def update_car_info(**car):
    car['is_aviable'] = True
    return car


car = update_car_info(brand='BMW', price=12000)
print(car)


# ========================================


def sum_all(*args):
    return sum(args)


print(sum_all(1, 3, 9, 20))


# ========================================


def mult_by_factor(value, multiplier=1):
    """Multiplies number by multiplicator"""
    return value * multiplier


print(mult_by_factor(5))


# ========================================


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 107,
    'author': 'Vovka',
}

post_with_weekday = create_new_post(post=initial_post)
print(initial_post)
print(post_with_weekday)


# ========================================


def print_number_info(num):
    """
    Prints whether number is even or odd

    Args:
        num (int): Number to be evaluated
    """

    if (num % 2) == 0:
        print('Entered number is even')
    else:
        print('Entered number is odd')


def print_square_num(num):
    print('Square of the number:', num * num)


def process_number(number, callback_fn):
    callback_fn(number)


entered_num = int(input('Enter any number: '))
process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)


# ========================================


def send_data(data):
    # sending data to the remote server
    pass


def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    # actions with updated data
    send_data_fn(updated_data)


process_data({'name': 'Vovka', 'phone_number': 123456}, send_data)


# ========================================
