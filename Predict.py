from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb
import lightgbm as lgb
import catboost as cb
from sklearn.externals import joblib
import os

print("调用成功 Predict：")


def LoadModel():
    print(os.getcwd())
    cab= joblib.load('./model/cab_model.pkl')
    lgb= joblib.load('./model/lgb_model.pkl')
    xgb=joblib.load('./model/xgb_model.pkl') 
    gbdt=joblib.load( './model/gbdt_model.pkl') 
    stack_lr=joblib.load( './model/stack_lr.pkl')
    return cab,lgb,xgb,gbdt,stack_lr

def ModelPredict(para):

    # para=[7.16, 0.4, 0.31,0.9,2.7,1.48, 0.78, 0.86]
    data=pd.DataFrame(columns=('R', 'angle', 'occusion','score'))
    print("预测开始：")
     
    
    for i in range(int(len(para)/4)):
        print(i*4)
        data.loc[i]=para[i*4:i*4+4]
    print(data)
    y_test=data.pop('score');x_test=data
    print(x_test)
    print(y_test)
    cab,lgb,xgb,gbdt,stack_lr=LoadModel()
    
    print("加载完毕：")
    y_pred_cab_test= cab.predict(x_test)
    y_pred_lgb_test = lgb.predict(x_test)
    y_pred_xgb_test= xgb.predict(x_test)
    y_pred_gbdt_test = gbdt.predict(x_test)
    
    print("stack")
    stack_x_test = pd.DataFrame()
    stack_x_test['Method_1'] = y_pred_cab_test
    stack_x_test['Method_2'] = y_pred_lgb_test
    stack_x_test['Method_3'] = y_pred_xgb_test   
    stack_x_test['Method_4'] = y_pred_gbdt_test
    stack_pred=stack_lr.predict(stack_x_test)
    print("stack_mae:",mean_absolute_error(y_test, stack_pred))  #mae:2.1501818709279975
    print(stack_pred.tolist())
    return  stack_pred.tolist()
    # return  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # return  [1,2,3]









 

    












    









































