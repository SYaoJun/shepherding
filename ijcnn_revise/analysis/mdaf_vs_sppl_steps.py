import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X = np.arange(20, 62, 2)

Y1 = np.array([639.000, 727.000, 779.000, 734.000, 804.000, 756.000, 797.000, 776.000, 709.000, 779.000, 771.000, 826.000, 749.000, 871.000, 951.000, 826.000, 779.000, 885.000, 857.000, 861.000, 762.000])

Y2 = np.array([373.000, 585.000, 595.000, 606.000, 627.000, 725.000, 640.000, 673.000, 770.000, 687.000, 691.000, 816.000, 709.000, 797.000, 792.000, 684.000, 1074.000, 1011.000, 766.000, 792.000, 597.000])

plt.plot(X, Y1, '-o', label="SPPL")
plt.plot(X, Y2, '-o', label="MDAF")

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.show()

fig.savefig("E:\\destination_in_center.pdf", dpi=600, format='pdf')
# mean = np.mean(Y1) - np.mean(Y2)
#
# print(mean / np.mean(Y1))
# 0.09784829907440797  = 9.79%
