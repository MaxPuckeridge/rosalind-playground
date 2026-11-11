
def output(a, b):
    cumulative = 0

    x  = a
    if (a % 2 != 1):
        x = a + 1

    while (x < b):
        cumulative += x
        x += 2

    return cumulative

if __name__ == '__main__':
    print(output(4172, 8190))

