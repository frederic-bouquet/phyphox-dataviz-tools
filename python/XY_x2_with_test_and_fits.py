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
# data points are sent one by one by a phyphox program
#
# square the x value but ignore input if user_parameter = 0
# additionnal cruves are plotted (labeled 'fits', but that is up to you)
#
#
# configuration :
# an XY graph, an extravariable "user_parameter"
# an additional curve fitone (the opposite)
# an additional curve fittwo (a linear fit)
#





def double(n):
    return n * 2

def negatif(n):
    return n * -1

with open (sys.argv[1]) as fd :
    jsondata = json.load(fd)
    result = []
    for i in range(len(jsondata['phyphoxData'])):
        if jsondata['extravariables']['user_parameter'][i][0] != 0 :
            point={}
            point['x'] = []
            point['y'] = []
            for j in range(len(jsondata['phyphoxData'][i]['x'])):
                point['x'].append(jsondata['phyphoxData'][i]['x'][j] ** 2)
                point['y'].append(jsondata['phyphoxData'][i]['y'][j])
            result.append(point)  
        
    fitone = {}
    fitoneX = []
    fitoneY = []
    
    for i in range(len(jsondata['phyphoxData'])):
        if jsondata['extravariables']['user_parameter'][i][0] != 0 :
            for j in range(len(jsondata['phyphoxData'][i]['x'])):
                fitoneX.append( jsondata['phyphoxData'][i]['x'][j] ** 2 )
                fitoneY.append( -1 * jsondata['phyphoxData'][i]['y'][j] )
            
    fitone['x'] = fitoneX
    fitone['y'] = fitoneY

    fittwo = {}
    fittwoX = []
    fittwoY = []
    
    for i in range(len(jsondata['phyphoxData'])):
        if jsondata['extravariables']['user_parameter'][i][0] != 0 :
            for j in range(len(jsondata['phyphoxData'][i]['x'])):
                fittwoX.append( jsondata['phyphoxData'][i]['x'][j] ** 2 )
                fittwoY.append( 2 * jsondata['phyphoxData'][i]['y'][j] )
        
    fittwo['x'] = fittwoX
    fittwo['y'] = fittwoY

    arr = {}
    arr['measures'] = result
    arr['fits'] = {}
    arr['fits']['fitone'] = fitone
    arr['fits']['fittwo'] = fittwo   


    fp = open(sys.argv[2], 'w+')
#    json.dump(arr, fp, indent=4, sort_keys=True, separators=(',', ': '))
    json.dump(arr, fp)