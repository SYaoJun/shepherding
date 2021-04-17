from utils import gui
from utils import common
from utils import sheep
import numpy as np
import time
import math
from max_perimeter import shepherdR
from knn_distance import sheepR
import matplotlib.pyplot as plt
from numpy import linalg as la


def init_sheep(canvas_local, n):
    agents = {}
    X = list()
    for i in range(n-1):
        np.random.seed(i)
        x = np.random.randint(100, 300)
        y = np.random.randint(100, 300)
        X.append([x, y])
        agents['sheep' + str(i)] = sheep.Agent(canvas_local, x - 5, y - 5, x + 5, y + 5, 'green')

    # 离群点的特殊的一只羊,在目标区域
    X.append([550, 550])
    agents['sheep' + str(n-1)] = sheep.Agent(canvas_local, 550 - 5, 550 - 5, 550 + 5, 550 + 5, 'green')
    # 牧羊犬的初始位置
    herd = sheep.Agent(canvas_local, 50, 550, 60, 560, 'red')
    return np.array(X), agents, herd


def run_animation(all_sheep, sheep_dict, herd):
    step = 0
    target = np.array([600, 600])
    r_dist = 250
    r_rep = 14
    speed = 2
    n = len(all_sheep)
    app_dist = n + 50
    theta = math.pi/4.5
    fn = math.sqrt(n) * r_rep
    last_vector = np.zeros((n, 2), dtype=np.float32)
    # 处理轨迹
    UU = []
    VV = []
    XX = []
    YY = []
    Px = {}
    Py = {}
    for i in range(n):
        Px['coor' + str(i)] = []
        Py['coor' + str(i)] = []

    for i in range(n):
        Px['coor' + str(i)].append(all_sheep[i][0])
        Py['coor' + str(i)].append(all_sheep[i][1])
    dist_center = 0
    dist_shepherd = 0
    pre_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
    pre_herd = herd.position2point()

    while True:
        herd_point = herd.position2point().copy()
        if common.check_sector(all_sheep, theta, target) and common.check_dist(all_sheep, target, fn):
            shepherdR.driving(herd, all_sheep, speed, target, app_dist)
        else:
            shepherdR.collecting(herd, all_sheep, speed, app_dist, target)

        sheepR.sheep_move(herd_point, all_sheep, r_dist, r_rep, speed, sheep_dict, last_vector)

        tk.update()
        time.sleep(0.01)

        if common.is_all_in_target(all_sheep) or step > 4000:
            for per_sheep in sheep_dict.values():
                per_sheep.delete()
            herd.delete()
            print("dispersion: ", common.calculate_dispersion(all_sheep))
            break
        # 处理轨迹
        global_mean = np.array([np.mean(all_sheep[:, 0]), np.mean(all_sheep[:, 1])])
        dist_center += la.norm(pre_mean - global_mean)
        pre_mean = global_mean
        dist_shepherd += la.norm(pre_herd - herd.position2point())
        pre_herd = herd.position2point()
        for i in range(n):
            Px['coor' + str(i)].append(all_sheep[i][0])
            Py['coor' + str(i)].append(all_sheep[i][1])
        XX.append(herd.position2point()[0])
        YY.append(herd.position2point()[1])
        UU.append(global_mean[0])
        VV.append(global_mean[1])
        step += 1

    # 处理轨迹
    fig, ax = plt.subplots()

    xx = np.array(XX)
    yy = np.array(YY)
    uu = np.array(UU)
    vv = np.array(VV)
    for i in range(n):
        plt.plot(np.array(Px['coor' + str(i)]), 600 - np.array(Py['coor' + str(i)]), linewidth=0.1, c="silver", zorder=1)
    plt.plot(xx, 600 - yy, c='darkkhaki', label='shepherd', linewidth=2, zorder=2)
    # plt.plot(uu, 600 - vv, '-.', c='darkcyan', label='sheep center', linewidth=2)

    n = 50
    X = list()
    for i in range(n - 1):
        np.random.seed(i)
        x = np.random.randint(100, 300)
        y = np.random.randint(100, 300)
        X.append([x, y])

    # 离群点的特殊的一只羊,在目标区域
    Y = np.array([550, 50])

    X = np.array(X)
    plt.scatter(X[:, 0], 600-X[:, 1], label="normal sheep", zorder=3)
    plt.scatter(Y[0], Y[1], label="outlier sheep", zorder=3)

    range_x = np.arange(0, 700, 100)
    plt.xticks(range_x)
    plt.yticks(range_x)
    # plt.grid()
    plt.legend()
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()
    fig.savefig('E:\\我的坚果云\\latex\\doubleDistSum\\pics\\outlier_b_mdaf_trajectory.pdf', dpi=600, format='pdf')
    ## 输出距离
    print("dist_center:", dist_center)
    print("dist_shepherd:", dist_shepherd)
    return step


if __name__ == '__main__':
    """
    绘制带有起始羊群和轨迹的图
    """
    tk, canvas = gui.init_tkinter()
    n = 50
    all_sheep, sheep_dict, shepherd_a = init_sheep(canvas, n)
    step = run_animation(all_sheep, sheep_dict, shepherd_a)
    print(step)
    print("MDAF animation over!")
    tk.mainloop()
