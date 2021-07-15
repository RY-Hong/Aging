# Aging Gene ML
Reproducing of https://github.com/kerepesi/aging_ml

***
### Environment
- Python 3.5.3  
- Pandas 0.20.3  
- scikit-learn 0.19.0  
- xgboost 1.1.1  
(unless otherwise specified)  
  

### Changes to the original code at [Aging_ML](https://github.com/kerepesi/aging_ml)
#### XGBoost_CV.py
Line 35, 52
```diff  
+ print(clf.feature_importances_)
```  

Line 45
```diff
+ pyplot.bar(range(len(clf.feature_importances_)),clf.feature_importances_)  
+ pyplot.show()
```  

#### TreeDumper.py
Line 8, 12  @[danyatingshen](https://github.com/danyatingshen)  
```diff
- model.booster()  
+ model.get_booster()
```
