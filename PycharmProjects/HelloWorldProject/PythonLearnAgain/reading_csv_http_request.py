import urllib.request # for accessing the urls
import datetime
import os # for file paths
import ssl # for creating a context as HTTPS reques like youtube were failing due to cretitificate issue.

#globals for the files paths
read_csv = r'C:\Users\vburaga\Desktop\Delete Later'
write_csv = r'C:\Users\vburaga\Desktop\Delete Later'



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
            row_writer = csv.writer(up)
            for row in line:
                i += 1
                url = row[4]
                try :
                    response = urllib.request.urlopen(url,timeout=2)
                    t = tuple(
                        (row[0], row[1], row[2], row[3], row[4], response.status, response.getheader('Content-Type')))
                    updated_rows.append(t)
                    row_writer.writerow(
                        [row[0], row[1], row[2], row[3], row[4], response.status, response.getheader('Content-Type')])
                    print('Completed:', i)
                except Exception as e:
                    print('Time Out', e)
                    row_writer.writerow(
                        [row[0], row[1], row[2], row[3], row[4], 'timeout', 'timeout'])


def read_csv_files_failed_timedout_ruls():
    import csv
    print(datetime.datetime.now())
    path_csv = r'C:\Users\vburaga\Desktop\Delete Later\video_urls_udpated_run1.csv'
    with open(path_csv,'r') as f:
        line = csv.reader(f,delimiter=',')
        updated_rows = []
        i = 0

        with open(r'C:\Users\vburaga\Desktop\Delete Later\video_urls_udpated.csv','w',newline='') as up:
            row_writer = csv.writer(up)
            for row in line:
                i += 1
                value = row[5].strip()
                if  row[5].strip() != '200':
                    url = row[4]
                    try:
                        response = urllib.request.urlopen(url, timeout=10)
                        row_writer.writerow(
                            [row[0], row[1], row[2], row[3], row[4], response.status,
                             response.getheader('Content-Type')])
                        print('Completed:', i,url)
                    except Exception as e:
                        print('Time Out', e, i, url)
                        row_writer.writerow(
                            [row[0], row[1], row[2], row[3], row[4], 'timeout', 'timeout'])
    print(datetime.datetime.now())



def read_csv_files_to_check_urls(file_read_from,file_write_to,timeout=2):
    import csv
    print(datetime.datetime.now())

    read_csv_full_path = os.path.join(read_csv,file_read_from)
    print('Reading from following path',read_csv_full_path)

    with open(read_csv_full_path,'r') as f:
        line = csv.reader(f,delimiter=',')
        updated_rows = []
        i = 0
        write_csv_full_path = os.path.join(write_csv,file_write_to)
        print('Writing to the following file', write_csv_full_path)
        with open(write_csv_full_path,'w',newline='') as up:
            row_writer = csv.writer(up)

            #creating a context avaoid CERTIFICATE_VERIFY_FAILED ERRORS
            ssl.CERT_NONE
            context = ssl._create_default_https_context


            for row in line:
                i += 1
                value = row[5].strip()
                if  row[5].strip() != '200':
                    url = row[4]
                    try:
                        response = urllib.request.urlopen(url, timeout=timeout,context=context)
                        row_writer.writerow(
                            [row[0], row[1], row[2], row[3], row[4], response.status,
                             response.getheader('Content-Type')])
                        print('Completed:', i,url)
                    except Exception as e:
                        print('Time Out', e, i, url)
                        row_writer.writerow(
                            [row[0], row[1], row[2], row[3], row[4], 'timeout', 'timeout'])
    print(datetime.datetime.now())


if __name__ == '__main__':
    #check_urls()
    #old_way()
    #read_csv_files()
    #read_csv_files_failed_timedout_ruls()
    read_csv_files_to_check_urls('Not_expo_URLs.csv','Not_expo_URLs_updated.csv',timeout=10)
