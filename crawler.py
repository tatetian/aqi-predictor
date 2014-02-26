#!/bin/python
import os
from datetime import date
from datetime import timedelta
from time import strftime

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_url(year, month, day):
    return 'http://www.young-0.com/airquality/index.php?number=1&unit=1&enddate=1&year=%u&month=%u&day=%u&hour=0&city=0&cn=0&action=2' % (year, month, day)

def fetch_page(year, month, day):
    url = get_url(year, month, day)
    output_file = "data/%04u_%02u_%02u.html" % (year, month, day)
    os.system("wget -q -O " + output_file + " " + url)

if __name__ == '__main__':
    start_date = date(2013, 2, 1)
    end_date = date(2014, 2, 1)

    for one_day in daterange(start_date, end_date):
        y = one_day.year
        m = one_day.month
        d = one_day.day
        print "fetching", strftime("%Y-%m-%d", one_day.timetuple()), "...",
        fetch_page(y,m,d)
        print "done."


