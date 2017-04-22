

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
        

def triangle_numbers():
    total = 1
    count = 1
    while True:
        yield total
        count += 1
        total += count
        

def yield_terms(iterable, indecies):
    enumerated = enumerate(iterable)
    for index in indecies:
        while True:
            i, v = next(enumerated)
            if i == index:
                yield v
                break
