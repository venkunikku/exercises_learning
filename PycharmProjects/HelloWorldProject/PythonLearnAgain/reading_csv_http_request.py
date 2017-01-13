import urllib.request
def check_urls():
    columns = ['spin_unique_id','item_id','division_number','item_number,url','status','contentType']
    path = r'C:\Users\vburaga\Desktop\New folder\urls.txt'
    path_csv = r'C:\Users\vburaga\Desktop\Delete Later\video_urls.csv'
    with open(path_csv) as f:
        for line in f.readline():
            print(line)
            values = line.split(',')
            print(values)


def old_way():
    columns = ['spin_unique_id', 'item_id', 'division_number', 'item_number,url', 'status', 'contentType']
    path = r'C:\Users\vburaga\Desktop\New folder\urls.txt'
    path_csv = r'C:\Users\vburaga\Desktop\Delete Later\video_urls.txt'
    f = open(path)
    for line in f.readline():
        print(line)

def read_csv_files():
    import csv
    path_csv = r'C:\Users\vburaga\Desktop\Delete Later\video_urls.csv'
    with open(path_csv,'r') as f:
        line = csv.reader(f,delimiter=',')
        updated_rows = []
        i = 0

        with open(r'C:\Users\vburaga\Desktop\Delete Later\video_urls_udpated.csv','w',newline='') as up:
            for row in line:
                i += 1
                url = row[4]
                try :
                    response = urllib.request.urlopen(url,timeout=2)
                    t = tuple(
                        (row[0], row[1], row[2], row[3], row[4], response.status, response.getheader('Content-Type')))
                    updated_rows.append(t)
                    row_writer = csv.writer(up)
                    row_writer.writerow(
                        [row[0], row[1], row[2], row[3], row[4], response.status, response.getheader('Content-Type')])
                    print('Completed:', i)
                except Exception as e:
                    print('Time Out', e)
                    row_writer.writerow(
                        [row[0], row[1], row[2], row[3], row[4], 'timeout', 'timeout'])


if __name__ == '__main__':
    #check_urls()
    #old_way()
    read_csv_files()
