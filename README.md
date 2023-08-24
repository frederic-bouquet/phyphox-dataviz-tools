#  Phyphox Data Vizualization App Tools

This repository contains python scripts and phyphox programs that can be used together with the Phyphox Data Visualization app that can be found [https://github.com/trberrido/phyphox](https://github.com/trberrido/phyphox). These programs serve as examples on how to access the data and modify them before displaying them.


## Python Scripts

- **SN_no_change.py**: must be used in a Single Number vizualization. It calculates the mean, which is also the default behavior when no script is used.
- **SN_mean_double.py**: must be used in a Single Number vizualization. It doubles the data and calculates the mean.
- **SN_mean_double_with_test.py**: must be used in a Single Number vizualization, and needs the extravariable `user_parameter` defined in the configuration. The phyphox experiment should send data and a buffer with the Id `user_parameter` on each send. If the value of `user_parameter` is zero, the data are ignored, if not the data are doubled and averaged.