import numpy as np
from sklearn import linear_model
import pandas as pd

# 计算斜率


def calculate_slope(data):
    reg = linear_model.LinearRegression()
    reg.fit(np.array(range(len(data))).reshape(-1, 1), np.array(data).reshape(-1, 1))
    slope = reg.coef_ # 斜率
    intercept = reg.intercept_ # 截距
    slope = slope[0][0]
    intercept = intercept[0]
    return slope

def calculate_var(data):
    df=pd.DataFrame(data)
    arr= np.var(df)
    return arr


def form_slope(data,step,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8):
    df = pd.DataFrame(data['井深'], columns=['井深'])
    df[feature] = 0
    df[feature1] = 0
    df[feature4] = 0
    df[feature2 + '-' + feature8] = 0
    df[feature3] = 0
    df[feature5] = 0
    df[feature6 + feature7] = 0
    df[feature + 's'] = 0
    df[feature1 + 's'] = 0
    df[feature4 + 's'] = 0
    df[feature2 + '-' + feature8 + 's'] = 0
    df[feature3 + 's'] = 0
    df[feature5 + 's'] = 0
    df[feature2] = 0
    df[feature2 + 's'] = 0
    df[feature6 + feature7 + 's'] = 0
    for i in range(1, len(data) - step + 1, 1):
        df[feature + 's'][i + step - 1] = abs(calculate_slope(data[feature][i:i + step - 1]))
        df[feature1 + 's'][i + step - 1] = abs(calculate_slope(data[feature1][i:i + step - 1]))
        df[feature2 + 's'][i + step - 1] = abs(calculate_slope(data[feature2][i:i + step - 1]))
        df[feature2 + '-' + feature8 + 's'][i + step - 1] = abs(
            calculate_slope(data[feature2][i:i + step - 1] - data[feature8][i:i + step - 1]))
        df[feature3 + 's'][i + step - 1] = abs(calculate_slope(data[feature3][i:i + step - 1]))
        df[feature4 + 's'][i + step - 1] = abs(calculate_slope(data[feature4][i:i + step - 1]))
        df[feature5 + 's'][i + step - 1] = abs(calculate_slope(data[feature5][i:i + step - 1]))
        df[feature6 + feature7 + 's'][i + step - 1] = abs(
            calculate_slope(data[feature6][i:i + step - 1] + data[feature7][i:i + step - 1]))
        df[feature][i + step - 1] = (calculate_var(data[feature][i:i + step - 1]))
        df[feature1][i + step - 1] = (calculate_var(data[feature1][i:i + step - 1]))
        df[feature2][i + step - 1] = (calculate_var(data[feature2][i:i + step - 1]))
        df[feature2 + '-' + feature8][i + step - 1] = (
            calculate_var(data[feature2][i:i + step - 1] - data[feature8][i:i + step - 1]))
        df[feature3][i + step - 1] = (calculate_var(data[feature3][i:i + step - 1]))
        df[feature4][i + step - 1] = (calculate_var(data[feature4][i:i + step - 1]))
        df[feature5][i + step - 1] = (calculate_var(data[feature5][i:i + step - 1]))
        df[feature6 + feature7][i + step - 1] = (
            calculate_var(data[feature6][i:i + step - 1] + data[feature7][i:i + step - 1]))

    df['actual'] = data['溢流']
    df[feature + 'c'] = 0
    df[feature1 + 'c'] = 0
    df[feature2 + '-' + feature8 + 'c'] = 0
    df[feature3 + 'c'] = 0
    df[feature4 + 'c'] = 0
    df[feature5 + 'c'] = 0
    df[feature6 + feature7 + 'c'] = 0
    df[feature + 'sc'] = 0
    df[feature1 + 'sc'] = 0
    df[feature2 + '-' + feature8 + 'sc'] = 0
    df[feature3 + 'sc'] = 0
    df[feature4 + 'sc'] = 0
    df[feature5 + 'sc'] = 0
    df[feature2 + 'c'] = 0
    df[feature2 + 'sc'] = 0
    df[feature6 + feature7 + 'sc'] = 0
    for ii in range(step - 1, len(df) - 1):
        df[feature + 'c'][ii] = df[feature][ii + 1] - df[feature][ii]
        df[feature1 + 'c'][ii] = df[feature1][ii + 1] - df[feature1][ii]
        df[feature2 + 'c'][ii] = df[feature2][ii + 1] - df[feature2][ii]
        df[feature2 + '-' + feature8 + 'c'][ii] = df[feature2 + '-' + feature8][ii + 1] - df[feature2 + '-' + feature8][
            ii]
        df[feature3 + 'c'][ii] = df[feature3][ii + 1] - df[feature3][ii]
        df[feature4 + 'c'][ii] = df[feature4][ii + 1] - df[feature4][ii]
        df[feature5 + 'c'][ii] = df[feature5][ii + 1] - df[feature5][ii]
        df[feature6 + feature7 + 'c'][ii] = df[feature6 + feature7][ii + 1] - df[feature6 + feature7][ii]
        df[feature + 'sc'][ii] = df[feature + 's'][ii + 1] - df[feature + 's'][ii]
        df[feature1 + 'sc'][ii] = df[feature1 + 's'][ii + 1] - df[feature1 + 's'][ii]
        df[feature2 + '-' + feature8 + 'sc'][ii] = df[feature2 + '-' + feature8 + 's'][ii + 1] - \
                                                   df[feature2 + '-' + feature8 + 's'][ii]

        df[feature2 + 'sc'][ii] = df[feature2 + 's'][ii + 1] - df[feature2 + 's'][ii]
        df[feature3 + 'sc'][ii] = df[feature3 + 's'][ii + 1] - df[feature3 + 's'][ii]
        df[feature4 + 'sc'][ii] = df[feature4 + 's'][ii + 1] - df[feature4 + 's'][ii]
        df[feature5 + 'sc'][ii] = df[feature5 + 's'][ii + 1] - df[feature5 + 's'][ii]
        df[feature6 + feature7 + 'sc'][ii] = df[feature6 + feature7 + 's'][ii + 1] - df[feature6 + feature7 + 's'][ii]

    return df


