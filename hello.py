def say_hi(name = None):
    if name:
        print(f'Hi, my name is {name}.')
    else:
        print('Hi.')

def say_hello(name_first, name_last = None):
    if name_last:
        print("Hello, {name_first} {name_last}")
    else:
        print("Hello, {name_first}")

__version__ = '1.2'
