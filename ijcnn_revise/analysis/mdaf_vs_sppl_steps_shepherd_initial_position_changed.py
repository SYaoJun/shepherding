import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X = np.arange(20, 62, 2)

Y1 = np.array([769.000, 623.000, 822.000, 656.000, 596.000, 686.000, 588.000, 722.000, 742.000, 755.000, 785.000, 804.000, 798.000, 897.000, 898.000, 819.000, 951.000, 813.000, 740.000, 857.000, 899.000, ])

Y2 = np.array([542.000, 569.000, 518.000, 555.000, 582.000, 698.000, 619.000, 783.000, 753.000, 818.000, 738.000, 536.000, 768.000, 762.000, 781.000, 844.000, 823.000, 829.000, 816.000, 848.000, 775.000, ])

plt.plot(X, Y1, '-o', label="SPPL")
plt.plot(X, Y2, '-o', label="MDAF")

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.show()