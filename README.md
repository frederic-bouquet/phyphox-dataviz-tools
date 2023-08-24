#  Phyphox Data Vizualization App Tools

This repository contains python scripts and phyphox programs that can be used together with the Phyphox Data Visualization app that can be found [https://github.com/trberrido/phyphox](https://github.com/trberrido/phyphox). These programs serve as examples on how to access the data and modify them before displaying them.

## Python Scripts

The python scripts are compatible with python 3 and python 2.7, but the first line must be adapted to the version of python that is installed on the server. If you want to test a script on your local computer, you should run it with two arguments:

    $ python SN_no_change.py input.json output.json

The syntax of `input.json` and `output.json` is detailed in the ReadMe of [https://github.com/trberrido/phyphox](https://github.com/trberrido/phyphox). Note that if you have a phyphox experiment sending data to your server, and you need a realistic `input.json` file to develop your python script, using the `no_change` script adapted to you visualization in a dummy run is a good way of obtaining one.

To test a script on a server, you need the Phyphox Visualization App installed, and a phyphox program that will send data to your server.

These scripts are example of how to access data and modify them before visualization:

- **SN_no_change.py**: must be used in a Single Number visualization. It calculates the mean, which is also the default behavior when no script is used.
- **SN_mean_double.py**: must be used in a Single Number visualization. It doubles the data and calculates the mean.
- **SN_mean_double_with_test.py**: must be used in a Single Number visualization, and needs the extravariable `user_parameter` defined in the configuration. The phyphox experiment should send data and a buffer with the Id `user_parameter` on each send. If the value of `user_parameter` is zero, the data are ignored, if not the data are doubled and averaged.
- **Hist_no_change.py**: must be used in a Histogram visualization. It plots all data that are received without altering them.
- **Hist_double.py**: must be used in a Histogram visualization. It plots the double of all data that are received.
- **Hist_double_with_test.py**: must be used in a Histogram visualization, and needs the extravariable `user_parameter` defined in the configuration. The phyphox experiment should send data and a buffer with the Id `user_parameter` on each send. If the value of `user_parameter` is zero, the data are ignored, if not the data are doubled and plotted.
- **XY_no_change.py**: must be used in a Graph visualization. It plots all the (X, Y) data that are received without altering them.
- **XY_x2.py**: must be used in a Graph visualization. For all the (X, Y) data that are received, it plots the data point (X², Y).
- **XY_x2_with_test.py**: must be used in a Graph visualization, and needs the extravariable `user_parameter` defined in the configuration. The phyphox experiment should send data and a buffer with the Id `user_parameter` on each send. If the value of `user_parameter` is zero, the data are ignored, if not for all the (X, Y) data that are received, it plots the data point (X², Y).
- **XY_x2_with_test_and_fits.py**: must be used in a Graph visualization, and needs the extravariable `user_parameter` defined in the configuration. It also needs two additional plots to be defined in the configuration, with the lineIDs `fitone` and `fittwo`. The phyphox experiment should send data and a buffer with the Id `user_parameter` on each send. If the value of `user_parameter` is zero, the data are ignored. If not for all the (X, Y) data that are received, it plots the data point (X², Y), but also two other plots, `fitone` (X², - Y) and `fittwo` (X², 2Y).

