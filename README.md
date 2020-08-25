# BikeDemand

## App Guide

### How to operate with the repository

0. Pull the repository on your local machine
1. Download the data from https://www.kaggle.com/c/bike-sharing-demand/data
2. Unzip to 'bike-sharing-demand' and put as subfolder to repository
3. Install requirements pip install -r requirements.txt 
4. Run python start.py to train the model
5. Follow the attached steps to fully run and test the solution.

**Recommended software** Pycharm

#### Run Unittests

Both single point and multi data points.

<pre><code>pytest ./test.py
</code></pre>

#### Run API

Run app in main directory.

<pre><code>python app2.py
</code></pre>

#### Run API requests

Both single point and multi data points.

<pre><code>python ./app_test.py
</code></pre>

## Analytics

#### Assumptions

- Orginal test is ignored, due to lack of target value.
- Test set is taken as 20% of original train set, randomly.


#### Log of Analytical Performance

- LinearRegression() R2:  0.1084245004064398 MAE:  132.9918705935313
- ADD_datetime_features LinearRegression() R2:  0.16861714744970657 MAE:  125.82931853905438
- CHANGEof_TRAIN_TEST split LinearRegression() R2:  0.3953567122037507 MAE:  105.37189478950403
- ADD_ohe_features LinearRegression() R2:  0.40108421460875343 MAE:  105.05410937621441
- DecisionTreeRegressor() R2:  0.8895141986830241 MAE:  34.882920110192835
- GradientBoostingRegressor() R2:  0.8587898632890966 MAE:  46.7984731089591
- ADD_rushhour_feature DecisionTreeRegressor() R2:  0.8928538705854316 MAE:  34.70798898071625

**Comment**
Any manual feautre like rushhour will not substantially increase the performance of the model. The rushhour feature is interaction feature. Multiple interactions are generate in the decision-tree-like models. Further manual feature like rushhour will not be added.

