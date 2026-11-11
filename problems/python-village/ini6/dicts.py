
def process():
    f = open('rosalind_ini6.txt', 'r')
    s = f.readline()

    words = s.split()

    d = {}

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    o = open('output.txt', 'w')

    for key in d:
        num = d[key] | 0
        line = key + " " + str(num) + '\n'
        o.write(line)

if __name__ == '__main__':
    process()


    