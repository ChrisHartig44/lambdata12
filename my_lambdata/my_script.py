import pandas as pd


import datetime


def shrink(n):
    """
    Param is a number
    Function will shrink n

    """
    return n - 20
n = 100

print(shrink(n))


def date_now(datetime_object):
    return (datetime_object)

datetime_object = datetime.datetime.now()

print(date_now(datetime_object))
