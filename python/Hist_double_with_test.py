#!/usr/bin/env python
import sys
import json

#
# ADAPT THE FIRST LINE ACCORDING PYTHON 2.7 OR PYTHON 3
# 
# python 2.7 => #!/usr/bin/env python
# python 3 => '#!/usr/bin/env python3'
#
# Use with a histogram visualisation
# extravariable : user_parameter
#
# double the input, but ignore input if user_parameter = 0
#
#
# configuration :
# a histogram, an extravariable "user_parameter"
#




def double(n):
    return n * 2



with open (sys.argv[1]) as fd :
    jsondata = json.load(fd)

    result = []
    for i in range(len(jsondata['phyphoxData'])):
        if jsondata['extravariables']['user_parameter'][i][0] != 0 :
            for data in jsondata['phyphoxData'][i]:
                result.append(double(data))


    fp = open(sys.argv[2], 'w+')
    json.dump(result, fp)


