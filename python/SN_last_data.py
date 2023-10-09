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
# represent the last data
# usefull for tests, or for creating a input.json
#
# configuration :
# a single number visualisation
#






with open (sys.argv[1]) as fd :
    jsondata = json.load(fd)


    i = len(jsondata['phyphoxData'])
    j = len(jsondata['phyphoxData'][i-1])

    fp = open(sys.argv[2], 'w+')
    json.dump(jsondata['phyphoxData'][i-1][j-1], fp)



