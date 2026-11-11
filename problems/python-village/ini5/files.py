if __name__ == '__main__':
    f = open('rosalind_ini5.txt', 'r')
    o = open('output.txt', 'w')

    i = 1
    for line in f:
        if (i % 2 == 0):
            o.write(line)
        i += 1

