import change as ch
import trendline as td
import change as ch


def form_step(x,x1,x2,x3,x4,x5,x6,x7, x8, x9, x10, x11, x12, x13,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8):
  step=[]
  for j in range(10):
   step.append(10)
   for i in range(10,500,10):
       step[j]=i
       min=10000000
       temp = sec5(i, df[0][i], ornum[0][i], x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13) \
              + sec5(i, df[1][i], ornum[1][i], x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13) \
              + sec5(i, df[2][i], ornum[2][i], x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13) \
              + sec5(i, df[3][i], ornum[3][i], x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13) + sec5(i, df[4][i], ornum[4][i], x, x1, x2,x3, x4, x5, x6, x7, x8, x9, x10,x11, x12, x13) + sec5(i, df[5][i],
                                                                                                         ornum[5][i], x, x1,
                                                                                                         x2, x3, x4, x5,
                                                                                                         x6, x7, x8, x9,
                                                                                                         x10, x11, x12,
                                                                                                         x13)
       for jj in range(10):
        if(temp[jj]<min):
          min=temp[jj]
          tmp=i
   step[j]=tmp
  res=x1-x1
  for i in range(10):
      res[i]=step[i]
  return res

def flag_form(step,j,df,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13):

     flag=[]
     for ii in range(step - 1, len(df) - 1):
        if ((df[feature2+'c'][ii] > x2[j] or df[feature4 + 'c'][ii] > x4[j]) or (
                df[feature2+'sc'][ii] > x9[j] or df[feature4 + 'sc'][ii] > x11[j])):
            if ((df[feature + 'c'][ii] > x[j] or df[feature1 + 'c'][ii] > x1[j] or df[feature5 + 'c'][ii] > x5[j]) or (
                    df[feature + 'sc'][ii] > x7[j] or df[feature1 + 'sc'][ii] > x8[j] or df[feature5 + 'sc'][ii] >
                    x12[j])):
                flag.append(ii)
                print("yy")
            else:
                if (df[feature6 + feature7 + 'c'][ii] <= x6[j] or df[feature6 + feature7 + 'sc'][ii] <= x13[j]):
                    if (-df[feature3 + 'c'][ii] <= x3[j] or -df[feature3 + 'sc'][ii] <= x10[j]):
                        flag.append(ii)
     return flag
def flag_form1(step,j,df,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13):
  flag=[]
  for i in range(step-1, len(df) - 1):
    if((df[feature2 + '-' + feature8 + 'c'][i] > x2[j] or df[feature4 + 'c'][i] > x4[j])and(df[feature2 + '-' + feature8 + 'sc'][i] > x9[j] or df[feature4 + 'sc'][i] > x11[j])and (df[feature + 'c'][i] > x[j] or df[feature1 + 'c'][i] > x1[j] or df[feature5 + 'c'][i] > x5[j])and (df[feature + 'sc'][i] > x7[j] or df[feature1 + 'sc'][i] > x8[j] or df[feature5 + 'sc'][i] > x12[j])and(df[feature6 + feature7 + 'c'][i] <= x6[j]or df[feature6 + feature7 + 'sc'][i] <= x13[j])and(df[feature3 + 'c'][i] >= x3[j]or df[feature3 + 'sc'][i] >= x10[j])):

           flag.append(i)

  return flag



def sec(step,df,ornum,x,x1,x2,x3,x4,x5,x6,x7, x8, x9, x10, x11, x12, x13,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8):

    tot=x1-x1 #存储的是预测正确的个数
    whtot=x1-x1 #存储的是真实情况下溢流的个数
    wrtot=x1-x1 #存储的是预测错误的个数
    res=x1-x1
    flag=[]
    for j in range(10):
     flag.clear()
     flag=flag_form(step,j, df, feature, feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)

    for i in range(len(flag)):
        pflag=0
        for jj in range(len(ornum)):
            if(flag[i]==ornum[jj]):
                tot[j]=tot[j]+1
                pflag=1
                break
        if(pflag==0):
            wrtot[j]=wrtot[j]+1
    whtot[j]=len(ornum)
    res[j]=tot[j]/(whtot[j]+wrtot[j])
    return res
def sec1(step,df,ornum,x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8):

    flag=[]
    xx = x1
    xx = xx - x1 + 1000000
    for j in range(10):
        flag.clear()
        flag=flag_form(step,j, df, feature, feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)
        tot=0
        ptot=0
        for i in range(len(flag)):
           tot=abs(ornum[0]-flag[i])+tot
           ptot=ptot+1

        print(tot,ptot)

        if(ptot!=0):
            xx[j]=tot/ptot

    return xx
def sec2(step,df,ornum,x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8):

    flag=[]
    print('sec2')
    xx=x1
    xx=xx-x1+1000000
    for j in range(10):
       flag.clear()
       flag = flag_form(step,j, df, feature, feature1, feature2, feature3, feature4, feature5, feature6, feature7,
                            feature8, x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)

       for ii in range(len(flag)):
           if(xx[j]>abs(ornum[0]-flag[ii])):
               xx[j]=abs(ornum[0]-flag[ii])

    print(xx)
    return xx
def sec3(step,df,ornum,x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,feature,feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8):

    flag=[]
    print('hihih')
    xx = x1
    xx = xx - x1
    for j in range(10):
        flag.clear()
        flag = flag_form(step,j, df, feature, feature1, feature2, feature3, feature4, feature5, feature6, feature7,
                             feature8, x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)

        for ii in range(len(flag)):
           pflag=0
           if (abs(ornum[0] - flag[ii]) <= 50):
               xx[j] = 1000 + xx[j]
               continue
           for jj in range(len(ornum)):
             if(flag[ii]==ornum[jj]):
                   xx[j]=100+xx[j]
                   pflag=1
                   break
           if(pflag==0):
              xx[j]=xx[j]-2000

    print(x,xx,len(flag),len(df))
    print(flag)

    return xx
def sec4(f1,x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13):
    xx = x1
    xx = xx - x1
    flag=[[]]
    for j in range(10):
        for i in range(len(name)):
         flag[i].clear()
         flag[i] = flag_form(f1[j], j, df[i][f1[j]],  x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)
        for i in range(0,len(name)):
         for ii in range(len(flag[i])):
            pflag = 0
            if (abs(ornum[i][f1[j]][0] - flag[i][ii]) <= 50):
                xx[j] = 1000 + xx[j]
                continue
            for jj in range(len(ornum)):
                if (flag[i][ii] == ornum[i][f1[j]][jj]):
                    xx[j] = 100 + xx[j]
                    pflag = 1
                    break
            if (pflag == 0):
                xx[j] = xx[j] - 2000
    return xx
def sec5(step,df,ornum,x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13):

    flag=[]
    xx = x1
    xx = xx - x1 + 1000000
    for j in range(10):
        flag.clear()
        flag=flag_form(step,j, df, x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)
        tot=0
        ptot=0
        for i in range(len(flag)):
           tot=abs(ornum[0]-flag[i])+tot
           ptot=ptot+1

        print(tot,ptot)

        if(ptot!=0):
            xx[j]=tot/ptot

    return xx
