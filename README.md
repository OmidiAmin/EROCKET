# REDUCING THE COMPUTATIONAL COMPLEXITY OF LEARNING WITH RANDOM CONVOLUTIONAL FEATURES
This Demo is an implementation of the E-ROCKET feature selection method for removing redundancies of  [MINIROCKET featurs](https://github.com/angus924/minirocket). For the first time, E-ROCKET uses supervised feature selection to reduce the computational complexity of learning with random features.

Please cite this work in the following manner:

`M. A. Omidi, B. Seyfe, and S. Valaee, “Reducing the computational complexity of learning with random convolutional features,” in ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023, pp. 1–5.`

[Click here to see EROCKET paper](https://ieeexplore.ieee.org/document/10095893)
In the EROCKET paper, after transforming data by MINIROCKET, the proposed feature selection algorithm is evaluated over [UCR database](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/). On average, E-ROCKET prunes more than 84 percent of random features. In this demo, E-ROCKET has been applied to one of the UCR datasets called [Coffee](http://www.timeseriesclassification.com/description.php?Dataset=Coffee). With this demo, you can evaluate the E-ROCKET method over other UCR datasets.

# E-ROCKET methodology

A brief overview of the E-ROCKET method has been provided here:
![alt text](https://github.com/OmidiAmin/EROCKET/blob/main/E-ROCKET%20Poster%20-%20May%2027%202023.jpg)

In the E-ROCKET method has three stages:
1. Pretraining: Minirocket is applied to training data. Then, a ridge regression classifier is applied to the transformed training data.
2. Knee/Elbow detection: The regression weights are sorted in ascending order and two knee and elbow points are detected. The weights between these two high-curvature points are smaller. Therefore, we can remove their associated features without incurring significant loss in classification accuracy.
3. Retraining: Finally, we retrain the ridge regression model over remaining featurs.

