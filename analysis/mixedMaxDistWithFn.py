import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X = np.arange(2, 91)

Y = np.array([676.000, 704.000, 1298.000, 739.000, 698.000, 721.000, 697.000, 693.000, 704.000, 714.000, 698.000, 697.000, 703.000, 692.000, 704.000, 696.000, 671.000, 727.000, 725.000, 701.000, 719.000, 729.000, 689.000, 720.000, 684.000, 642.000, 724.000, 656.000, 690.000, 739.000, 724.000, 751.000, 697.000, 720.000, 692.000, 748.000, 731.000, 732.000, 777.000, 663.000, 740.000, 653.000, 670.000, 601.000, 655.000, 636.000, 665.000, 741.000, 838.000, 734.000, 911.000, 913.000, 907.000, 872.000, 851.000, 758.000, 694.000, 784.000, 922.000, 765.000, 729.000, 736.000, 708.000, 913.000, 791.000, 766.000, 792.000, 827.000, 742.000, 714.000, 714.000, 707.000, 694.000, 711.000, 699.000, 741.000, 730.000, 709.000, 700.000, 689.000, 695.000, 739.000, 704.000, 716.000, 716.000, 705.000, 749.000, 688.000, 751.000])
Y2 = np.array([531.000, 695.000, 788.000, 717.000, 894.000, 854.000, 831.000, 928.000, 855.000, 869.000, 955.000, 902.000, 1010.000, 488.000, 548.000, 583.000, 1059.000, 633.000, 948.000, 476.000, 575.000, 534.000, 511.000, 894.000, 898.000, 863.000, 956.000, 1102.000, 906.000, 1021.000, 1223.000, 1223.000, 978.000, 936.000, 944.000, 912.000, 955.000, 951.000, 1072.000, 1227.000, 1382.000, 1020.000, 1339.000, 1006.000, 1437.000, 1047.000, 1544.000, 1133.000, 1458.000, 1123.000, 1248.000, 1578.000, 1478.000, 1293.000, 1457.000, 1253.000, 1614.000, 1509.000, 1308.000, 1587.000, 1624.000, 1507.000, 1327.000, 1542.000, 1253.000, 1181.000, 1318.000, 1586.000, 1625.000, 1534.000, 1414.000, 1588.000, 1701.000, 1665.000, 1441.000, 1414.000, 1345.000, 1318.000, 1446.000, 1690.000, 1661.000, 1407.000, 1696.000, 1670.000, 1395.000, 1751.000, 1428.000, 1667.000, 1463.000])
# Y3 = np.array([620.000, 707.000, 754.000, 770.000, 831.000, 875.000, 886.000, 1159.000, 854.000, 829.000, 812.000, 845.000, 1510.000, 811.000, 783.000, 838.000, 997.000, 776.000, 1032.000, 1052.000, 550.000, 1003.000, 1123.000, 1033.000, 913.000, 1075.000, 1263.000, 1334.000, 553.000, 1282.000, 1394.000, 1100.000, 1135.000, 1161.000, 1010.000, 1028.000, 1167.000, 1157.000, 1185.000, 1193.000, 1317.000, 1440.000, 1338.000, 1466.000, 487.000, 1134.000, 652.000, 913.000, 835.000, 1550.000, 1503.000, 1472.000, 1502.000, 1560.000, 1298.000, 534.000, 732.000, 1601.000, 1540.000, 1603.000, 1678.000, 574.000, 1629.000, 954.000, 1107.000, 1065.000, 1167.000, 1527.000, 973.000, 1130.000, 1599.000, 998.000, 604.000, 833.000, 1624.000, 1724.000, 1641.000, 1799.000, 1623.000, 1742.000, 1810.000, 1637.000, 1818.000, 1841.000, 589.000, 1518.000, 1826.000, 621.000, 1608.000])
# Y4 = np.array([])
Y5 = np.array([659.000, 670.000, 407.000, 439.000, 480.000, 444.000, 462.000, 400.000, 433.000, 428.000, 399.000, 456.000, 351.000, 402.000, 528.000, 454.000, 380.000, 489.000, 439.000, 487.000, 513.000, 526.000, 492.000, 384.000, 459.000, 421.000, 413.000, 452.000, 570.000, 474.000, 473.000, 438.000, 380.000, 401.000, 396.000, 413.000, 415.000, 397.000, 399.000, 412.000, 412.000, 417.000, 415.000, 441.000, 520.000, 423.000, 472.000, 448.000, 618.000, 412.000, 440.000, 562.000, 527.000, 502.000, 656.000, 459.000, 454.000, 534.000, 566.000, 464.000, 486.000, 482.000, 487.000, 497.000, 510.000, 505.000, 512.000, 497.000, 533.000, 514.000, 520.000, 531.000, 582.000, 526.000, 506.000, 544.000, 539.000, 543.000, 539.000, 519.000, 542.000, 544.000, 552.000, 550.000, 553.000, 683.000, 570.000, 623.000, 672.000])
Y6 = np.array([522.000, 587.000, 432.000, 449.000, 563.000, 458.000, 480.000, 423.000, 408.000, 520.000, 424.000, 515.000, 348.000, 449.000, 511.000, 489.000, 397.000, 633.000, 496.000, 548.000, 575.000, 579.000, 536.000, 407.000, 489.000, 494.000, 423.000, 454.000, 507.000, 491.000, 577.000, 476.000, 564.000, 530.000, 504.000, 475.000, 466.000, 509.000, 510.000, 416.000, 523.000, 591.000, 514.000, 465.000, 451.000, 518.000, 438.000, 585.000, 586.000, 475.000, 488.000, 582.000, 565.000, 506.000, 583.000, 462.000, 526.000, 612.000, 511.000, 550.000, 502.000, 578.000, 507.000, 512.000, 534.000, 551.000, 552.000, 513.000, 608.000, 532.000, 529.000, 569.000, 580.000, 571.000, 516.000, 583.000, 544.000, 576.000, 544.000, 561.000, 539.000, 558.000, 574.000, 563.000, 577.000, 617.000, 601.000, 587.000, 607.000])


# # plt.plot(X, Y,  label="MDA")
plt.plot(X, Y2, 'darkcyan', label="SPPL")
# # plt.plot(X, Y6,  label="MDF")
plt.plot(X, Y5, 'purple', label="MDAF")
#
# # plt.plot(X, Y3,  label="max center distance")

plt.xlabel("the number of sheep")
plt.ylabel("time steps")
plt.xticks(np.arange(0, 100, 10))
plt.legend()
plt.xlim(0, 95)
plt.ylim(0, 2000)
plt.grid()
plt.show()
fig.savefig("E:\\我的坚果云\\latex\\doubleDistSum\\pics\\mixedSheep2to90.pdf", dpi=600, format='pdf')

# a = np.mean(Y2)
# b = np.mean(Y5)
# print(a-b)