
def main():
    func(9)
    func()


def func(a=7):
    # print('range Def')
    for i in range(a,10):
        print(i,end=' ')
    print()

if __name__ == '__main__':main()