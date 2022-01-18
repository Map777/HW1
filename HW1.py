# Homework 1
# Morgan Paul


def get_data(file):
    my_file = open(file, "r")
    content = my_file.readlines()

    #content_list = content.split(",")
    my_file.close()
    return print(content)


print(get_data("/Users/morganpaul/Desktop/Duke Spring 2022/821/example.txt"))

import math
from statistics import covariance
def analyze_data(content, option= y):
    if option=1:
    # average
    n = len(content)
    avg = sum(content)/n
    #return avg

    #if option=2:
    #standard deviation
    for i in content
        numerator = sum(i-avg)**2
    std_dev = math.sqrt(numerator/n)

    if option=3:
    # covariance
    n1= len(content[0])
    avg1 = sum(content[0])/n1
    for i in content[0]
    numerator1 = sum(i-avg1)**2

    n2= len(content[1])
    avg2 = sum(content[1])/n2
    for i in content[1]
    numerator2 = sum(i-avg2)**2
    covariance = ________ /n-1



    if option=4:
    # correlation
    
    corr = covariance/(sig1*sig2)

    return float
