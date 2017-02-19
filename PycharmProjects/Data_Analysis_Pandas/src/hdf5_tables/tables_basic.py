from tables import *
import datetime


def create_tables():
    h5file = open_file('./hdf5_tables/log.h5', mode='w', title='Logg Tracking')
    group = h5file.create_group(where='/', name='log', title='Audit log data in tables')
    table = h5file.create_table(where=group, name='http_log', description=Log, title='Web log group')
    print(h5file)
    print(repr(h5file))

    # pointer to the row table
    http_log_table = table.row
    print('LoadStart', datetime.datetime.now())
    for i in range(500):
        #print('working on follwoing {0}'.format(i))
        http_log_table['audit_id'] = 'audit_log_{0:d}'.format(i)
        http_log_table['date'] = i
        http_log_table['url'] = 'url_{0:d}'.format(i)
        http_log_table.append()
    print('LoadEnd-1', datetime.datetime.now())
    table.flush()
    print('LoadEnd-2', datetime.datetime.now())
    print('Read-Start', datetime.datetime.now())
    read_table = h5file.root.log.http_log
    records = [ [x['audit_id'],x['url']] for x in read_table.iterrows()]
    print('Read-End', datetime.datetime.now())

    h5file.close()



class Log(IsDescription):
    audit_id = StringCol(16)
    date = Int32Col()
    url = StringCol(20)


if __name__ == '__main__':
    print('Overall-Start', datetime.datetime.now())
    create_tables()
    print('Overall-End', datetime.datetime.now())
