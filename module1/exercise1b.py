from math import sqrt

def getAverage(mylist):
    return sum(mylist)/len(mylist)

def getStandardDeviation(mylist):
    tmp=[]
    for i in mylist:
        tmp.append((i - getAverage(mylist))**2)
    return sqrt( sum(tmp) / (len(mylist) - 1) )

def getResults( data_list, stat_results ):
    for ls in data_list:
        stat_results.append([getAverage(ls), getStandardDeviation(ls)])