import os


def log_check(log_file):
    if log_file.is_file():
        return True
    else:
        return False


def log_write(log_file, text):
    with open(log_file, "a") as file:
        file.write(f'{text}\n')


def move_file(file):
    os.rename(f'{file}', f'completed_orders/{file}')


def log_create(log_file, text):
    with open(log_file, "w") as file:
        file.write(f'{text}\n')


def log_delete(log_file):
    os.remove(log_file)
