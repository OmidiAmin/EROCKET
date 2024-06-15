Hello everybody. In this folder, I've provided the result of running Erocket over all 128 UCR classification datasets. The number of iterations for each dataset is 30.

1. erocket.xlsx contains the results of all 30 iterations over 128 UCR datasets. The columns are as follows:
    1. Row number,
    2. Dataset name
    3. Iteration number
    4. Minirocket accuracy (a number between [0,1])
    5. Minirocket number of features
    6. Erocket accuracy
    7. Number of retained features after applying Erocket
    8. Training time of using all 9996 minirocket features (in seconds)
    9. Knee detection time in Erocket
    10. Erocket retrain time
2. erocket_mean.xlsx contains the average results over 128 UCR datasets. The columns are as follows:
    1. Row number
    2. Dataset name
    3. Minirocket average accuracy of 30 repetitions (a number between [0,1])
    4. Minirocket average number of features
    5. Erocket average accuracy
    6. Average number of retained features after applying Erocket
    7. Average training time of using all 9996 minirocket features (in seconds)
    8. Average training time (fit time + knee detection time + retraining time) of erocket.
