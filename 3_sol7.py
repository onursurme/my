def infinity(start):
    yield start
    for x in infinity(start + 1):
        yield x

def infinity2(start):    # üstteki ile aynı
    yield start
    yield from infinity2(start + 1)