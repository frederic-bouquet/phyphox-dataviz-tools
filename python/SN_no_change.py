#!/usr/bin/env python
import sys
import json

#
# ADAPT THE FIRST LINE ACCORDING PYTHON 2.7 OR PYTHON 3
# 
# python 2.7 => #!/usr/bin/env python
# python 3 => '#!/usr/bin/env python3'
#
# Use with a single number visualisation
#
# calculate the average (default behavior when no script is defined)
# usefull for tests, or for creating a input.json
#
# configuration :
# a single number visualisation
#


def mean(n):
    return sum(n) / len(n)



with open (sys.argv[1]) as fd :
    jsondata = json.load(fd)

    result = []
    for element in jsondata['phyphoxData']:
        for data in element:
            result.append(data)

    fp = open(sys.argv[2], 'w+')
    json.dump(mean(result), fp)



