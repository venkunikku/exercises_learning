import csv


def read_like_list():
    i=0
    with open('/Users/venkuburagadda/home_data.csv','r') as rcsv:
        sreader = csv.reader(rcsv,delimiter=',')
        #print(sreader)
        for row in sreader:
            print(i)
            if i<100:
                print(row)
            else:
                break
            i+=1

def read_like_dictionary():
    i=0
    with open('/Users/venkuburagadda/home_data.csv','r') as rcsv:
        sreader = csv.DictReader(rcsv)
        #print(sreader)
        for row in sreader:
            print(i)
            if i<1000:
                # del row['sqft_lot']
                print(row )
            else:
                break
            i+=1




if __name__ == '__main__':
    #read_like_list()
    read_like_dictionary()