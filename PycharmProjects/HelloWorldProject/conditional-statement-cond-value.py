
def cond():
    a, b = 1, 0
    s = "a less than" if a < b else 'a is greater than or equal to b'
    print(s)

if __name__ == '__main__':
    cond()
