import pandas as pd
from sklearn.metrics import roc_curve,roc_auc_score,auc
from sklearn.model_selection import train_test_split
import lightgbm as lgb
print("import successful")
params = {}
params['learning_rate'] = 0.09043007325486686
#params['learning_rate'] = 0.01
params['boosting_type'] = 'gbdt'
params['objective'] = 'binary'
params['metric'] = 'binary_logloss'
params['sub_feature'] = 0.5
params['num_leaves'] = 45
params['min_data'] = 50
params['max_depth'] = 10

# Prepare datasets
X = pd.read_csv('result_data/train_app_prev_b_pos_credit_merged_corr.csv')
#test_data = pd.read_csv('result_data/test_app_prev_b_pos_installment_merged.csv')
Y  = X['TARGET']
X  = X.drop(columns=['TARGET'],axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
d_train = lgb.Dataset(X_train, label=y_train)
clf = lgb.train(params, d_train, 2)
y_pred=clf.predict(X_test)
fpr, tpr, thresholds = roc_curve(y_test.values,y_pred)
print(auc(fpr, tpr))