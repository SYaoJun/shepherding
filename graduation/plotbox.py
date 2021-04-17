import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig,axes = plt.subplots(1,1)

arr1 = np.array([0.7229390681003584,0.5912698412698413,0.708,0.5710059171597633,0.6103896103896104,0.7051792828685259,
                 0.9861111111111112,0.9861751152073732,0.9439252336448598,0.9473684210526315,0.8270042194092827,0.7710843373493976,
                 0.7272727272727273,0.7540322580645161,0.82,0.8207171314741036,0.83399209486166,0.8549019607843137])

arr2 = np.array([0.4175084175084175,0.5204460966542751,0.6837944664031621,0.6561264822134387,0.75,0.8114754098360656,
                 0.9295154185022027,0.6782006920415224,1.0047169811320755,0.9634703196347032,1.0046511627906978,0.9636363636363636,
                 0.7874015748031497,0.927038626609442,0.889795918367347,0.9194915254237288,0.8938775510204081,0.9437229437229437])

df = pd.DataFrame(arr1, columns=['SPPL'])
s2 = pd.Series(arr2)

df['MAM'] = s2
color = dict(boxes='DarkGreen',whiskers='DarkOrange',medians='DarkBlue',caps='Gray')
df.plot.box(ylim=[0.4,1], color = color,ax = axes)
plt.xlabel("the number of sheep")
plt.ylabel("two models")
plt.grid()
plt.show()