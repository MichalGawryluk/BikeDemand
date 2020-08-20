# BikeDemand

### Assumptions

Orginal test is ignored, due to lack of target value.
Test set is taken as 20% of last observation due to series data


### Log of Analytical Performance

- LinearRegression() R2:  0.1084245004064398 MAE:  132.9918705935313
- ADD_datetime_features LinearRegression() R2:  0.16861714744970657 MAE:  125.82931853905438
- CHANGEof_TRAIN_TEST split LinearRegression() R2:  0.3953567122037507 MAE:  105.37189478950403
- ADD_ohe_features LinearRegression() R2:  0.40108421460875343 MAE:  105.05410937621441
