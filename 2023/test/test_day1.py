import pytest
from common import load_file
from day1 import find_number, \
                 find_calibration_value, \
                 day1, day1_2, letters2numbers



test1='1abc2'
test2='pqr3stu8vwx'
test3='a1b2c3d4e5f'
test4='treb7uchet'    

tests_part_two = load_file('data/day1_2_test')

def test_day1_find_number_1():
    assert 1 == find_number(directon='left', word=test1)
    assert 2 == find_number(directon='right', word=test1)

def test_day1_find_number_2():   
    assert 3 == find_number(directon='left', word=test2)
    assert 8 == find_number(directon='right', word=test2)

def test_day1_find_number_3():
    assert 1 == find_number(directon='left', word=test3)
    assert 5 == find_number(directon='right', word=test3)

def test_day1_find_number_4():
    assert 7 == find_number(directon='left', word=test4)
    assert 7 == find_number(directon='right', word=test4)
    
def test_day1_calibration_1():
    assert 12 == find_calibration_value(line=test1)
    
def test_day1_calibration_2():
    assert 38 == find_calibration_value(line=test2)

def test_day1_calibration_3():
    assert 15 == find_calibration_value(line=test3)
    
def test_day1_calibration_4():
    assert 77 == find_calibration_value(line=test4)

def test_day1_test_cases():        
    assert 142 == day1('data/day1_test')
    
def test_day1_2_replace_1():
    assert '219' == letters2numbers(word=tests_part_two[0])
    
def test_day1_2_replace_2():
    assert '823' == letters2numbers(word=tests_part_two[1])

def test_day1_2_replace_3():
    assert 'abc123xyz' == letters2numbers(word=tests_part_two[2])

def test_day1_2_replace_4():
    assert 'x2134' == letters2numbers(word=tests_part_two[3])

def test_day1_2_replace_5():
    assert '49872' == letters2numbers(word=tests_part_two[4])

def test_day1_2_replace_6():
    assert 'z18234' == letters2numbers(word=tests_part_two[5])
    
def test_day1_2_replace_7():
    assert '7pqrst6teen' == letters2numbers(word=tests_part_two[6])
    
def test_day1_2_replace_8():
    assert '21' == letters2numbers(word=tests_part_two[7])
  
def test_day1_2_test_cases():        
    assert 302 == day1_2('data/day1_2_test')
