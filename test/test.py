# import numpy as np
# Y2 = np.array([531.000, 695.000, 788.000, 717.000, 894.000, 854.000, 831.000, 928.000, 855.000, 869.000, 955.000, 902.000, 1010.000, 488.000, 548.000, 583.000, 1059.000, 633.000, 948.000, 476.000, 575.000, 534.000, 511.000, 894.000, 898.000, 863.000, 956.000, 1102.000, 906.000, 1021.000, 1223.000, 1223.000, 978.000, 936.000, 944.000, 912.000, 955.000, 951.000, 1072.000, 1227.000, 1382.000, 1020.000, 1339.000, 1006.000, 1437.000, 1047.000, 1544.000, 1133.000, 1458.000, 1123.000, 1248.000, 1578.000, 1478.000, 1293.000, 1457.000, 1253.000, 1614.000, 1509.000, 1308.000, 1587.000, 1624.000, 1507.000, 1327.000, 1542.000, 1253.000, 1181.000, 1318.000, 1586.000, 1625.000, 1534.000, 1414.000, 1588.000, 1701.000, 1665.000, 1441.000, 1414.000, 1345.000, 1318.000, 1446.000, 1690.000, 1661.000, 1407.000, 1696.000, 1670.000, 1395.000, 1751.000, 1428.000, 1667.000, 1463.000])
#
# Y5 = np.array([659.000, 670.000, 407.000, 439.000, 480.000, 444.000, 462.000, 400.000, 433.000, 428.000, 399.000, 456.000, 351.000, 402.000, 528.000, 454.000, 380.000, 489.000, 439.000, 487.000, 513.000, 526.000, 492.000, 384.000, 459.000, 421.000, 413.000, 452.000, 570.000, 474.000, 473.000, 438.000, 380.000, 401.000, 396.000, 413.000, 415.000, 397.000, 399.000, 412.000, 412.000, 417.000, 415.000, 441.000, 520.000, 423.000, 472.000, 448.000, 618.000, 412.000, 440.000, 562.000, 527.000, 502.000, 656.000, 459.000, 454.000, 534.000, 566.000, 464.000, 486.000, 482.000, 487.000, 497.000, 510.000, 505.000, 512.000, 497.000, 533.000, 514.000, 520.000, 531.000, 582.000, 526.000, 506.000, 544.000, 539.000, 543.000, 539.000, 519.000, 542.000, 544.000, 552.000, 550.000, 553.000, 683.000, 570.000, 623.000, 672.000])
#
# a = np.mean(Y2)
# b = np.mean(Y5)
# print(a/b)
import numpy as np
x = np.array([[3, 4], [5, 6]])
print('[', end="")
i = 0
for item in x:
    print('[', end="")
    j = 0
    for key in item:
        print("{:.2f}".format(key), end="")
        if j != len(item)-1:
            print(",", end="")
        j += 1
    if i != len(x) - 1:
        print(']', end=",")
    else:
        print(']', end="")
    i += 1
print(']', end="")
print()