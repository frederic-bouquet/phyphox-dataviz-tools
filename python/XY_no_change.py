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
# makes no change to the x and y values
# usefull for tests, or for creating a input.json
#




with open (sys.argv[1]) as fd :
    jsondata = json.load(fd)
    result = []
    for i in range(len(jsondata['phyphoxData'])):
        point={}
        point['x'] = jsondata['phyphoxData'][i]['x']
        point['y'] = jsondata['phyphoxData'][i]['y']
        result.append(point)


    arr = {}
    arr['measures'] = result
    arr['fits'] = {}
    
    fp = open(sys.argv[2], 'w+')
    json.dump(arr, fp)