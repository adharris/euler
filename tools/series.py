

def fibonacci():
    yield 1
    yield 1

    previous = 1
    current = 1

    while True:
        next_value = previous + current
        previous = current
        current = next_value
        yield current