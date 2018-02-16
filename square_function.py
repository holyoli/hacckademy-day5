import math
a_list = [1,2,3,4,5,6,7,8,9]

def square(numb):
    return numb**2

def square_numb(a_list):
    square_list = []
    for each_element in a_list:
        if type(each_element) is int and each_element > 0:
            square_list.append(each_element**2)
    return square_list
