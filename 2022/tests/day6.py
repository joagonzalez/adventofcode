import pytest
from day6 import marker 

def test_marker_1():
    assert 5 == marker('bvwbjplbgvbhsrlpgdmjqwftvncz')
    
def test_marker_2():
    assert 6 == marker('nppdvjthqldpwncqszvftbrmjlhg')

def test_marker_3():
    assert 10 == marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')

def test_marker_4():
    assert 11 == marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')

