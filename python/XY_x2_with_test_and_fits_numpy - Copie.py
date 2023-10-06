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
# here a linear fit is done using numpy
#
#
# configuration :
# an XY graph, an extravariable "user_parameter"
# an additional curve fitone (the opposite)
# an additional curve fittwo (a linear fit)
#


# ASSUMES A SINGLE X Y DATA IN A PACKET SENT BY PHYPHOX



def double(n):
    return n * 2

def negatif(n):
    return n * -1



with open (sys.argv[1]) as fd :

    dataX = []
    dataY = []
    jsondata = json.load(fd)
    result = []
    for i in range(len(jsondata['phyphoxData'])):
        if jsondata['extravariables']['user_parameter'][i][0] != 0 :                                 # here the data point is only considered if user_parmeter <> 0 , as an example
        # the data point sent by phyhox is stored in two different ways : one in dataX and dataY for a linear fit, one in a dictionnary point{} for display
            point={}
            point['x'] = [ jsondata['phyphoxData'][i]['x'][0] * jsondata['phyphoxData'][i]['x'][0] ] # here x is squared, as an example
            point['y'] = jsondata['phyphoxData'][i]['y']                                             # here y is left unchanged as an example
            result.append(point)
            dataX.append(point['x'][0])
            dataY.append(point['y'][0])        
        
    #fitone must be declared in the web visualization configuration. It is the opposite of the data
    fitone = {}
    fitoneX = []
    fitoneY = []
    for i in range(len(jsondata['phyphoxData'])):
        fitoneX.append( jsondata['phyphoxData'][i]['x'][0] * jsondata['phyphoxData'][i]['x'][0] )
        fitoneY.append( -1 * jsondata['phyphoxData'][i]['y'][0] )
    fitone['x'] = fitoneX
    fitone['y'] = fitoneY

    #fittwo must be declared in the web visualization configuration. It is a linear fit of the data
    fittwo = {}
    fittwoX = dataX.copy()
    fittwoY = []
    coef = np.polyfit(dataX, dataY, 1) # numpy linear fit, coef[0] is the slope, coef[1] the intercept
    poly1d_fn = np.poly1d(coef) 
    # poly1d_fn is now a function which takes in x and returns an estimate for y
    fittwoX.sort()
    for i in range(len(fittwoX)):
        fittwoY.append( poly1d_fn(fittwoX[i]) )
    fittwo['x'] = fittwoX
    fittwo['y'] = fittwoY
    
    
    arr = {}
    arr['measures'] = result
    arr['fits'] = {}
    arr['fits']['fitone'] = fitone
    arr['fits']['fittwo'] = fittwo


    fp = open(sys.argv[2], 'w+')
#   json.dump(arr, fp, indent=4, sort_keys=True, separators=(',', ': '))
    json.dump(arr, fp)