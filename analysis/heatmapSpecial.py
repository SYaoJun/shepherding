import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

fig, ax = plt.subplots()

data = {}
labels = np.arange(1, 70)

x50 = [1411.000, 1462.000, 2001.000, 1989.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 1924.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 611.000, 630.000, 573.000, 597.000, 589.000, 616.000, 605.000, 578.000, 710.000, 507.000, 605.000, 532.000, 501.000, 510.000, 525.000, 523.000, 488.000, 516.000, 477.000, 479.000, 502.000, 453.000, 454.000, 445.000, 460.000, 445.000, 428.000, 419.000, 416.000, 412.000, 413.000, 428.000]
x60 = [1604.000, 1234.000, 2001.000, 2001.000, 2001.000, 1769.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 1836.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 724.000, 774.000, 723.000, 747.000, 721.000, 701.000, 727.000, 693.000, 704.000, 732.000, 645.000, 662.000, 621.000, 622.000, 594.000, 609.000, 574.000, 578.000, 589.000, 550.000, 564.000, 642.000, 546.000, 549.000, 597.000, 478.000, 613.000, 472.000, 501.000, 571.000, 506.000, 512.000, 523.000, 525.000, 515.000, ]
x70 = [1994.000, 1947.000, 1870.000, 2001.000, 2001.000, 1786.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 2001.000, 1274.000, 992.000, 2001.000, 1102.000, 990.000, 1347.000, 915.000, 1144.000, 589.000, 1214.000, 587.000, 1057.000, 1031.000, 568.000, 555.000, 951.000, 553.000, 543.000, 539.000, 541.000, 540.000, 538.000, 537.000, 550.000, 550.000, 547.000, 543.000, 533.000, 534.000, 509.000, 513.000, 544.000, 541.000, 531.000, 514.000, 523.000, 515.000, 517.000, 517.000, 500.000, 519.000, 500.000, 504.000, 509.000, 505.000, 496.000, 490.000, 523.000, 511.000, 518.000, 493.000, 491.000, 500.000, 481.000]

for i in range(20):
    x50.append(428)

for i in range(10):
    x60.append(515)

data['50'] = x50
data['60'] = x60
data['70'] = x70

df = pd.DataFrame(data, index=labels)


sns.heatmap(df, vmin=0, vmax=2001, cmap="YlGnBu")

ax.set_ylabel('k neighbors')
ax.set_xlabel('the number of sheep')
plt.show()

fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\kneighbor50to70.pdf", dpi=600, format='pdf')