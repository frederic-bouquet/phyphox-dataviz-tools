#!/usr/bin/env python
import sys
import json

#
# ADAPT THE FIRST LINE ACCORDING PYTHON 2.7 OR PYTHON 3
# 
# python 2.7 => #!/usr/bin/env python
# python 3 => '#!/usr/bin/env python3'
#
# Use with a XY plot visualisation
#
# square the x value
#
#
# configuration :
# an XY graph
#






with open (sys.argv[1]) as fd :
    jsondata = json.load(fd)
    result = []
    for i in range(len(jsondata['phyphoxData'])):
        point={}
        point['x'] = []
        point['y'] = []
        for j in range(len(jsondata['phyphoxData'][i]['x'])):
            point['x'].append(jsondata['phyphoxData'][i]['x'][j] ** 2)
            point['y'].append(jsondata['phyphoxData'][i]['y'][j])
        result.append(point)


    arr = {}
    arr['measures'] = result
    arr['fits'] = {}

    fp = open(sys.argv[2], 'w+')
    json.dump(arr, fp)