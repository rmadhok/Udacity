import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    """
    In this exercise, for each turnstile unit, you will determine the date and time 
    (in the span of this data set) at which the most people entered through the unit.
    
    The input to the mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise. You can check out the csv and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    For each line, the mapper should return the UNIT, ENTRIESn_hourly, DATEn, and 
    TIMEn columns, separated by tabs. For example:
    'R001\t100000.0\t2011-05-01\t01:00:00'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    """

    for line in sys.stdin:
        data = line.strip().split(",")

        if data[0] == "" or len(data) != 22:
            continue

        print "{0}\t{1}\t{2}\t{3}".format(data[1], float(data[6]), data[2], data[3])

mapper()

def reducer():
    '''
    Write a reducer that will compute the busiest date and time (that is, the 
    date and time with the most entries) for each turnstile unit. Ties should 
    be broken in favor of datetimes that are later on in the month of May. You 
    may assume that the contents of the reducer will be sorted so that all entries 
    corresponding to a given UNIT will be grouped together.
    
    The reducer should print its output with the UNIT name, the datetime (which 
    is the DATEn followed by the TIMEn column, separated by a single space), and 
    the number of entries at this datetime, separated by tabs.

    For example, the output of the reducer should look like this:
    R001    2011-05-11 17:00:00    31213.0
    R002    2011-05-12 21:00:00    4295.0
    R003    2011-05-05 12:00:00    995.0
    R004    2011-05-12 12:00:00    2318.0
    R005    2011-05-10 12:00:00    2705.0
    R006    2011-05-25 12:00:00    2784.0
    R007    2011-05-10 12:00:00    1763.0
    R008    2011-05-12 12:00:00    1724.0
    R009    2011-05-05 12:00:00    1230.0
    R010    2011-05-09 18:00:00    30916.0
    ...
    ...

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    max_entries = 0
    old_key = None
    datetime = ''

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 4:
            continue

        # etract key-value pair with unit and number of entries
        this_key, entries = data[0], float(data[1])

        datetime = "{0} {1}".format(data[2], data[3])

        if old_key and old_key != this_key:
            print "{0}\t{1}\t{2}".format(old_key, this_date, max_entries)
            max_entries = 0.0

        old_key = this_key

        if max_entries <= entries:
            max_entries = entries
            this_date = datetime

    if old_key != None:
            print "{0}\t{1}\t{2}".format(old_key, this_date, max_entries)

reducer()

