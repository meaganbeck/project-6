"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time
import nose    # Testing framework
from nose.tools import *
import logging
import arrow
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_brevet1():
    brevet_dist = 200.0
    brevet_start_time = arrow.get("2023-02-17T10:00")#, "YYYY-MM-DD HH:mm")
    checkpoints = {
            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
            50: (brevet_start_time.shift(hours=1, minutes=28), brevet_start_time.shift(hours=3.0, minutes = 30)),
            100: (brevet_start_time.shift(hours=2.0, minutes=56), brevet_start_time.shift(hours=6.0, minutes = 40)),
            175: (brevet_start_time.shift(hours=5.0, minutes=9), brevet_start_time.shift(hours=11.0, minutes = 40)),
            200: (brevet_start_time.shift(hours=5.0, minutes=53), brevet_start_time.shift(hours=13.0, minutes = 30)),
            }
    for km, times in checkpoints.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time, ""
        assert close_time(km, brevet_dist, brevet_start_time) == end_time, ""

def test_brevet2():
    brevet_dist = 300.0
    brevet_start_time = arrow.get("2023-02-17T00:00")#, "YYYY-MM-DD HH:mm")
    checkpoints = {
            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
            50: (brevet_start_time.shift(hours=1.0, minutes= 28), brevet_start_time.shift(hours =3.0, minutes = 30)),
            100: (brevet_start_time.shift(hours= 2.0, minutes= 56), brevet_start_time.shift(hours=6.0, minutes = 40)),
            200: (brevet_start_time.shift(hours = 5.0 , minutes = 53), brevet_start_time.shift(hours=13.0, minutes = 20)),
            250: (brevet_start_time.shift(hours = 7.0, minutes = 27), brevet_start_time.shift(hours=16.0, minutes = 40)),
            300: (brevet_start_time.shift(hours=9.0, minutes=0), brevet_start_time.shift(hours=20.0)),
            340: (brevet_start_time.shift(hours=9.0, minutes=0), brevet_start_time.shift(hours= 20.0)),
            }
    for km, times in checkpoints.items():
        start_time, end_time = times
        print(open_time(km,brevet_dist, brevet_start_time).format("YYYY-MM-DD HH:mm"))
        print(close_time(km,brevet_dist, brevet_start_time).format("YYYY-MM-DD HH:mm"))
        assert open_time(km, brevet_dist, brevet_start_time) == start_time, ""
        assert close_time(km, brevet_dist, brevet_start_time) == end_time, ""

def test_brevet3():
    brevet_dist = 400.0
    brevet_start_time = arrow.get("2023-02-17T00:00")#, "YYYY-MM-DD HH:mm")
    checkpoints = {
            0: (brevet_start_time.shift(hours = 0.0), brevet_start_time.shift(hours=1.0)),
            100: (brevet_start_time.shift(hours = 2.0, minutes = 56), brevet_start_time.shift(hours=6.0, minutes = 40)),
            250: (brevet_start_time.shift(hours= 7.0, minutes=27), brevet_start_time.shift(hours=16.0, minutes = 40)),
            380: (brevet_start_time.shift(hours=11.0, minutes=30), brevet_start_time.shift(hours=25.0, minutes = 20)),
            400: (brevet_start_time.shift(hours=12.0, minutes=8), brevet_start_time.shift(hours=26.0, minutes = 40)),
            480: (brevet_start_time.shift(hours=12.0, minutes=8), brevet_start_time.shift(hours=26.0, minutes = 40)),
            }
    for km, times in checkpoints.items():
        start_time, end_time = times
        print(open_time(km,brevet_dist, brevet_start_time).format("YYYY-MM-DD HH:mm"))
        print(close_time(km,brevet_dist, brevet_start_time).format("YYYY-MM-DD HH:mm"))
        assert open_time(km, brevet_dist, brevet_start_time) == start_time, ""
        assert close_time(km, brevet_dist, brevet_start_time) == end_time, ""

def test_brevet4():
    brevet_dist = 600.0
    brevet_start_time = arrow.get("2023-02-17T00:00")#, "YYYY-MM-DD HH:mm")
    checkpoints = {
            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
            200: (brevet_start_time.shift(hours= 5.0, minutes=53), brevet_start_time.shift(hours=13.0, minutes = 20)),
            350: (brevet_start_time.shift(hours= 10.0, minutes=35), brevet_start_time.shift(hours=23.0, minutes = 20)),
            380: (brevet_start_time.shift(hours =11.0, minutes=30), brevet_start_time.shift(hours=25.0, minutes = 20)),
            450: (brevet_start_time.shift(hours =13.0, minutes=48), brevet_start_time.shift(hours= 30.0, minutes = 0)),
            600: (brevet_start_time.shift(hours= 18.0, minutes=48), brevet_start_time.shift(hours= 40.0)),
            720: (brevet_start_time.shift(hours = 18.0, minutes=48), brevet_start_time.shift(hours= 41.0)),
            }
    for km, times in checkpoints.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time, ""
        assert close_time(km, brevet_dist, brevet_start_time) == end_time, ""

def test_brevet5():
    brevet_dist = 1000.0
    brevet_start_time = arrow.get("2023-02-17T00:00")#, "YYYY-MM-DD HH:mm")
    checkpoints = {
            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
            500: (brevet_start_time.shift(hours=15.00, minutes = 28), brevet_start_time.shift(hours=33.0, minutes = 20)),
            999: (brevet_start_time.shift(hours=33.0, minutes=3), brevet_start_time.shift(hours=74.0, minutes = 55)),
            1000: (brevet_start_time.shift(hours=33.0, minutes=5), brevet_start_time.shift(hours = 75)),
            1200: (brevet_start_time.shift(hours=33.00, minutes=5), brevet_start_time.shift(hours=75.0)),
            }
    for km, times in checkpoints.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time, ""
        assert close_time(km, brevet_dist, brevet_start_time) == end_time, ""

@raises(ValueError)
def test_brevet6():
    brevet_dist = 1200.0 #invalid
    brevet_start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    checkpoints = {
            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
            50: (brevet_start_time.shift(hours = 1, minutes=1), brevet_start_time.shift(hours=1)),
            100: (brevet_start_time.shift(hours=1, minutes=1), brevet_start_time.shift(hours=1)),
            175: (brevet_start_time.shift(hours=1, minutes=1), brevet_start_time.shift(hours=1)),
            200: (brevet_start_time.shift(hours=1, minutes=1), brevet_start_time.shift(hours=1)),
            }
    #for km, times in checkpoints.items(): 
     #   start_time, end_time = times
      #  raise ValueError
    for km, times in checkpoints.items():
        start_time, end_time = times
        open_time(km, brevet_dist, brevet_start_time) 
        close_time(km, brevet_dist, brevet_start_time) 

