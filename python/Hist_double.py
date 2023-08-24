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
#
# double the input
#
#
# configuration :
# a histogram
#





def double(n):
    return n * 2


with open (sys.argv[1]) as fd :
    jsondata = json.load(fd)

    result = []
    for element in jsondata['phyphoxData']:
        for data in element:
            result.append(double(data))

    fp = open(sys.argv[2], 'w+')
    json.dump(result, fp)

