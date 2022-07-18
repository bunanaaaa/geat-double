import numpy as np
import geatpy as ea
import numpy as np
import success as suc
import change as ch
import matplotlib.pyplot as plt
step=30

feature = '甲烷'
feature1 = 'C2'
feature2 = '出口流量'
feature3 = '大钩高度'
feature4 = '立压'
feature5 = '全烃'
feature6 = '泵冲1'
feature7='泵冲3'
feature8='入口流量'
name=['xt2.csv','xt1.csv','xt3.csv','xt4.csv','xt5.csv','xt6.csv']
df,ornum=ch.form_data(step,name[0])
df1,ornum1=ch.form_data(step,name[1])
df2,ornum2=ch.form_data(step,name[2])
df3,ornum3=ch.form_data(step,name[3])
df4,ornum4=ch.form_data(step,name[4])
df5,ornum5=ch.form_data(step,name[5])
class MyProblem(ea.Problem):  # 继承Problem父类

    def __init__(self, M=2):
        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        Dim = 14  # 初始化Dim（决策变量维数）
        maxormins = [1,-1]  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        varTypes = [0] * Dim  # 初始化varTypes（决策变量的类型，0：实数；1：整数）
        lb = [0] * Dim  # 决策变量下界
        ub = [1] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self,
                            name,
                            M,
                            maxormins,
                            Dim,
                            varTypes,
                            lb,
                            ub,
                            lbin,
                            ubin)


    def evalVars(self, Vars):  # 目标函数
        x=Vars[:,[0]]
        x1 = Vars[:, [1]]
        x2 = Vars[:, [2]]
        x3 = Vars[:, [3]]
        x4 = Vars[:, [4]]
        x5 = Vars[:, [5]]
        x6=Vars[:,[6]]
        x7 = Vars[:, [7]]
        x8 = Vars[:, [8]]
        x9 = Vars[:, [9]]
        x10 = Vars[:, [10]]
        x11= Vars[:, [11]]
        x12 = Vars[:, [12]]
        x13=Vars[:,[13]]
        f1 = suc.sec2(step,df,ornum,x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8)
        f2 =suc.sec3(step,df,ornum,x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8)
        plt.scatter(f1, f2, color='r')
        plt.xlabel('f1')  # 设置x轴标题
        plt.ylabel('f2')
        # 利用可行性法则处理约束条件
        CV = np.hstack([
            x1-x1
        ])
        f = np.hstack([f1, f2])
        print('hihi',f,'nono',CV,'pp',Vars,'nono')
        return f, CV

