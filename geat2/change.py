import pandas as pd
import trendline as td

def last(df):
    lnum=[]
    for i in range(len(df)):
      if(df['actual'][i]==1):
          lnum.append(i)
    return lnum

def form_data(step,name):
    data = pd.read_csv(name, encoding='utf-8')
    '''feature='C1(%)'
    feature1='C2(%)'
    feature2='出口流量(L/s)'
    feature3='大钩位置(m)'
    feature4='FDT101_DT(g/cc)'
    feature5='总烃(%)'
    feature6='泵冲1(spm)'''
    feature = '甲烷'
    feature1 = 'C2'
    feature2 = '出口流量'
    feature3 = '大钩高度'
    feature4 = '立压'
    feature5 = '全烃'
    feature6 = '泵冲1'
    feature7 = '泵冲3'
    feature8 = '入口流量'
    df = td.form_slope(data, step, feature, feature1, feature2, feature3, feature4, feature5, feature6,feature7,feature8)
    print(df)
    ornum = last(df)
    print(ornum)
    return df,ornum