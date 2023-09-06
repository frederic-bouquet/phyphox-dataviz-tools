
# Phyphox Data Vizualization App Tools

  

This repository contains python scripts and phyphox programs that can be used together with the Phyphox Data Visualization app that can be found [https://github.com/trberrido/phyphox](https://github.com/trberrido/phyphox). These programs serve as examples on how to access the data and modify them before displaying them.

## Phyphox Programs
  
Phyphox is a free and opensource smartphone application that allows you to use the sensors in the smartphones for experiments. See [https://phyphox.org/](phyphox.org). Custom programs can be written following a xlm format described in the  following wiki contains all the information: [https://phyphox.org/wiki/index.php/Main_Page](https://phyphox.org/wiki/index.php/Main_Page). The following phyphox programs are given as examples; if you want to test them on your server you need to enter the proper address in the code.

The relevant part in the experiment to send data to the server looks like this:

	   <network>
	      <connection interval="1" address="https://www.MyServer.com/MyFolderWhereTheAppIsInstalled/api/input" id="submit" service="http/post" conversion="none" privacy="https://phyphox.org/disclaimer/" autoConnect="true">
	        <send id="dataID1" type="buffer">buffer1</send>
	        <send id="dataID2 type="buffer">buffer2</send>
	      </connection>
	    </network>

The parameters of the connection should be adapted to your need. Their role is described in the above wiki. Note that:
-	The parameter `address` in the `connection` field must correspond to your server;
-	The parameter `id` in the `send` field must be entered in the data ID field (or extravariable field) of the visualization.
-	`buffer1` and `buffer2` are phyphox buffers; the data they contain will be sent to the server. They can contain 0, 1, or multiple data. They need to be defined as any phyphox buffer does (see the phyphox file format).
-	There must be at least one “send” field, and as many as needed.


## Python Scripts

  

The python scripts are compatible with python 3 and python 2.7, but the first line must be adapted to the version of python that is installed on the server. If you want to test a script on your local computer, you should run it with two arguments:

  

$ python theNameOfMyPythonScript.py input.json output.json

  

The syntax of `input.json` and `output.json` is detailed in the ReadMe of [https://github.com/trberrido/phyphox](https://github.com/trberrido/phyphox). If you have a phyphox experiment sending data to your server, and you need a realistic `input.json` file for developing your Python script, using the no_change script adapted to your visualization in a dummy run is a good way to obtain one.

  

To test a script on a server, you need the Phyphox Visualization App installed, and a phyphox program that will send data to your server.

  

These scripts are example of how to access data and modify them before visualization:

  

-  **SN_no_change.py**: must be used in a Single Number visualization. It calculates the mean, which is also the default behavior when no script is used.

-  **SN_mean_double.py**: must be used in a Single Number visualization. It doubles the data and calculates the mean.

-  **SN_mean_double_with_test.py**: must be used in a Single Number visualization, and needs the extravariable `user_parameter` defined in the configuration. The phyphox experiment should send data and a buffer with the Id `user_parameter` on each send. If the value of `user_parameter` is zero, the data are ignored, if not the data are doubled and averaged.

-  **Hist_no_change.py**: must be used in a Histogram visualization. It plots all data that are received without altering them, which is also the default behavior when no script is used.

-  **Hist_double.py**: must be used in a Histogram visualization. It plots the double of all data that are received.

-  **Hist_double_with_test.py**: must be used in a Histogram visualization, and needs the extravariable `user_parameter` defined in the configuration. The phyphox experiment should send data and a buffer with the Id `user_parameter` on each send. If the value of `user_parameter` is zero, the data are ignored, if not the data are doubled and plotted.

-  **XY_no_change.py**: must be used in a Graph visualization. It plots all the (X, Y) data that are received without altering them, which is also the default behavior when no script is used.

-  **XY_x2.py**: must be used in a Graph visualization. For all the (X, Y) data that are received, it plots the data point (X², Y).

-  **XY_x2_with_test.py**: must be used in a Graph visualization, and needs the extravariable `user_parameter` defined in the configuration. The phyphox experiment should send data and a buffer with the Id `user_parameter` on each send. If the value of `user_parameter` is zero, the data are ignored, if not for all the (X, Y) data that are received, it plots the data point (X², Y).

-  **XY_x2_with_test_and_fits.py**: must be used in a Graph visualization, and needs the extravariable `user_parameter` defined in the configuration. It also needs two additional plots to be defined in the configuration, with the lineIDs `fitone` and `fittwo`. The phyphox experiment should send data and a buffer with the Id `user_parameter` on each send. If the value of `user_parameter` is zero, the data are ignored. If not for all the (X, Y) data that are received, it plots the data point (X², Y), but also two other plots, `fitone` (X², - Y) and `fittwo` (X², 2Y).





