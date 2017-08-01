"""
Indiana Univeristy bus route analysis
"""

import json

def write_headers():
    """
    This function writes the headers
    into the output file and returns None
    """

    with open('route.json') as ro:
        routes = json.load(ro)
    # read the various routes stops
    a.write(str(routes['B']+'\n'))
    # write the headers into the output file

def check_track(row_cur, stop_list):
    """
    This function checks where the bus goes
    in the desired stops as per the data
    """
    print row_cur
    print stop_list
    diff = abs(stop_list.index(row_cur[0])-stop_list.index(row_cur[1]))
    if diff == 1:
        return True, diff
    else:
        return False, stop_list[stop_list.index(row_cur[0]):stop_list.index(row_cur[1])]

def show_trip(trip):
    """
    """

    output = ''
    date = trip[0][-2]
    route = trip[0][4]
    bus_id = trip[0][3]
    output = '{},{},{},,,,'.format(date, route, bus_id)
    stop_id = ['67','24','25','26','27','28','29','31','33','4','6','8','10',
              '87','88','16','75','20','21','22','23', '24']

    for i in xrange(len(trip)):
        s = stop_id[stop_id.index(trip[i][0]):]
        status, diff = check_track(trip[i], s)

        if status:
            if trip[i][1] in ['24','88', '33', '6', '8', '88']:
                dat = '{},{},{},'.format(trip[i][-1], trip[i][-1],
                                            trip[i][-1])
                output += dat

            else:
                dat = '{},{},'.format(trip[i][-1], trip[i][-1])
                output += dat


        else:
            for each in diff:
                if each in ['24', '33', '6', '8', '88']:
                    dat = ',,,'
                    output += dat

                else:
                    dat = ',,'
                    output += dat


    a.write(output + '\n')



def bus_analysis(data_gen):
    """
    This function helps to format the data
    as per our need.
    """

    trips = []
    stop_id = ('25','26','27','28','29','31','33','4','6','8','10',
              '87','88','16','75','20','21','22','23')
    while True:
        try:
            d = data_gen.next().split(',')
            if not(d[0] in stop_id and d[1] in ('24', '67', '71')):
                trips.append(d)
            else:
                trips.append(d)
                d = data_gen.next().split(',')
                if (d[0] == '24' and d[1] == '24'):
                    trips.append(d)
                else:
                    pass
                show_trip(trips)
                # function call
                trips = []
                if not(d[0] == '24' and d[1] == '24'):
                    trips.append(d)

                print('ONE TRIP OVER!!!')
        except Exception, e:
            print e
            show_trip(trips)
            break


def fetch_data(data):
    """
    This generator function helps us
    to get the data row by row.
    """

    data_iter = iter(data.split('\n'))
    for row in data_iter:
            yield row


if __name__ == '__main__':
    # start of the program
    with open('Bpart1data.csv') as dat:
        data = dat.read()
    a = open('output.csv', 'a')
    write_headers()
    # function call
    data_gen = fetch_data(data)
    #print data_gen
    # get the data from a generator object
    bus_analysis(data_gen)
    # function call
    a.close()
