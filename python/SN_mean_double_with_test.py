#!/usr/bin/env python
import sys
import json

#
# ADAPT THE FIRST LINE ACCORDING PYTHON 2.7 OR PYTHON 3
# 
# python 2.7 => #!/usr/bin/env python
# python 3 => '#!/usr/bin/env python3'
#
# Use with a single number visualisation and the programm accelerometer_demo
# extravariable : user_parameter
#
# calculate the average if user_parameter != 0
#
#
# configuration :
# a single number visualisation, an extravariable "user_parameter"
#




def mean(n):
    return sum(n) / len(n)

def double(n):
    return n * 2


with open (sys.argv[1]) as fd :
    jsondata = json.load(fd)

    result = []

    for i in range(len(jsondata['phyphoxData'])):
        if (jsondata['extravariables']['user_parameter'][i][0] != 0):
            for data in jsondata['phyphoxData'][i]:
                result.append(double(data))            
#            result.append(double(jsondata['phyphoxData'][i][0]))

    fp = open(sys.argv[2], 'w+')
    json.dump(mean(result), fp)

