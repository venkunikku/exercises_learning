import  re
def test():
    f = open('sample_html.txt')
    for line in f.readlines():
        if re.search('<|>',line):
            # print(line,end='')

            ff = open('sample_html.txt')
            for lines in ff.readlines():
                print(re.sub('<|>','',lines))

    f.close()

if __name__ == '__main__':
    test()