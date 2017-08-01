"""
Indiana Univeristy bus route analysis
"""

import json

def write_headers():
    """
    This function writes the headers
    into the output file and returns None
    """

    with open('BdataCreation.json') as ro:
        routes = json.load(ro)
    # read the various routes stops
    a.write(str(routes['B']+'\n'))
    # write the headers into the output file

def getbustype(Complete_day_trips):
    """
    This will take the batch of a bus data for a given busid for the entire day and tries to find out which bustype it could be, b1,b2,b3,b4,b5.
    """

    
def writedatatofile(Complete_day_trips):    
    """
    Writing the computed results with bustype number to the final output file
    """ 
    for i in xrange(len(Complete_day_trips)):
        a.write(','.join(Complete_day_trips[i]) + '\n')
          
    

        
def bus_analysis(data_gen):
    """
    This function helps to format the data
    as per our need.
    """

    Complete_day_trips = []
    batch_row_count = 0
    day_first_record = []

    while True:
        try:           
            
            if (batch_row_count==0): # taking the first record of every complete day trips batch to comapre the next records for busid change
                d = data_gen.next().split(',')
                Complete_day_trips.append(d)
                day_first_record = d
                d = data_gen.next().split(',')
                                
            else: 
                pass
            # if not the first record in a batch of busid complete day trip, goahead and pull reccords until busid changes
            while True:
                if(day_first_record[3]== d[3]): # checking for same busid for the  whole day in batches
                     batch_row_count=batch_row_count+1
                     Complete_day_trips.append(d)
                     last_record_day_trips = d
                     d = data_gen.next().split(',')
                else: # started a new batch so busid sequence failed
                    batch_row_count=0
                    getbustype(Complete_day_trips) # get bus type
                    writedatatofile(Complete_day_trips) # get updated recordss with bustype, now write them to outputfile
                    Complete_day_trips = []
                    Complete_day_trips.append(d)
                    break


            print('ONE batch OVER!!! with start at {},{},{}' .format(day_first_record[3],day_first_record[5],day_first_record[6]))
            print('ONE batch OVER!!! with end at {},{},{}' .format(last_record_day_trips[3],last_record_day_trips[5],last_record_day_trips[6]))                
            last_record_day_trips = []
                
        except Exception, e:
            print e
            batch_row_count=0
            writedatatofile(Complete_day_trips)
            Complete_day_trips = []
            Complete_day_trips.append(d)
            print('ONE batch OVER!!! with start at {},{},{}' .format(day_first_record[3],day_first_record[5],day_first_record[6]))
            print('ONE batch OVER!!! with end at {},{},{}' .format(last_record_day_trips[3],last_record_day_trips[5],last_record_day_trips[6]))                
            last_record_day_trips = []
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
    with open('Bpart1datascheduledataanalysis.csv') as dat:
        data = dat.read()
    a = open('BdataGenerated.csv', 'a')
    write_headers()
    # function call
    data_gen = fetch_data(data)
    #print data_gen
    # get the data from a generator object
    bus_analysis(data_gen)
    # function call
    a.close()
