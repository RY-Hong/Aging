# Attempts

1. 1 attempt of 20 experiments of XGBoost with 5 fold CV
    * Input file: file.csv (GO_20183.csv)
    * Output file: file.csv-XGBoost_CV_preds-n_est50-exp20.csv
    * Output file by TreeDumper: file.csv-XGBoost_CV_preds-n_est50-exp20.csv_Trees-n_est50-max_d1.txt  
    ```python
    python XGBoost_CV.py 1 50 20 file.csv
    ```

2.  1 attempt of 5 experiments of XGBoost with image output of feature_importances
    * Input file: GO_20183.csv
    * Output file: GO_20183.csv-XGBoost_CV_preds-n_est50-exp5.csv
    * Output file by TreeDumper: GO_20183.csv-XGBoost_CV_preds-n_est50-exp5.csv_Trees-n_est50-max_d1.txt
    * Output image plot of feature importances: est50-exp5_(1-5).png  
    ```python
    python XGBoost_CV.py 1 50 5 GO_20183.csv
    ```

3. 2 attempts of 1 experiments of XGBoost with image output of feature_importances
    * Input file: GO_20183.csv
    * Output image plot of feature importances: 1.png and 2.png
    ```python
    python XGBoost_CV.py 1 50 1 GO_20183.csv
    ```