
def output(str, arr):
    a, b, c, d = arr
    out = str[a:b+1] + " " + str[c:d+1]
    return out

if __name__ == '__main__':
    str = "OD9JUgM1nXNLMsWYj9qan6YzgepB1pTGKj0HmB2s2vx836mF9wNemorhaedus99t78WUXs4D0ydgyxd7Y0i3kBgpquerquedula4x4MTIUd1Tx3WsfMIkcGGP86i65QX0wkPH3GvJE5911OxawTJizJdIy4JvqC5o0NM6KMERNz42APJqmVJ2BUKguQSdRat0f."
    arr = [ 50, 60, 88, 98]
    print(output(str, arr))

