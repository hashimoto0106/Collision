# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:18:02 2020

@author:sample
"""

import os
import time
import config
import logger
import database
import version
# import rsyslog
# import syslog
import help
import console
import line
import function
import parameter
import translation
from tqdm import tqdm
from datetime import datetime
import graph2d
import graph3d


def proc():
    # 2D Graph
    graph_2d = graph2d.graph("title", True)
    graph_2d.set_graph("xlabel", "ylabel", (-10, 10), (-10, 10))
    graph_2d.plot_vector("x", (0, 0), (3, 5), "blue")
    graph_2d.plot_vector("x", (0, 0), (1, 8), "green")
    graph_2d.plot_point("point", (4, 2), ".", "red")
    graph_2d.plot_circle((3, 2), 1, "yellow")
    graph_2d.plot_rectangle((-5, -5), 1, 3, "yellow")
#    graph_2d.plot_ellipse_test((-2.5, -2.5), 1, 3, "yellow")
    graph_2d.plot_ellipse("ellipse", (-2.5, -2.5), 1, 3, "yellow")

    # Image Graph
    graph_image = graph2d.graph("Image", True)
    graph_image.set_graph_image(500, 480)
    graph_image.plot_point("point", (140, 300), ".", "red")

    # 3D Graph
    graph_3d = graph3d.graph("title","xlabel", "ylabel", "zlabel", (-10.0, 10.0), (-10.0, 10.0), (-10.0, 10.0), True)
    graph_3d.set_coodinate((0, 0, 0), (10, 0, 0), (0, 10, 0), (0, 0, 10))
    graph_3d.plot_vector("x", (0, 0, 0), (2, 5, 9), "blue")
    graph_3d.plot_vector("x", (0, 0, 0), (-1, -3, -4), "green")
    graph_3d.plot_point("point", (3, 7, -8), ".", "red")
    graph_3d.plot_sphere((1, 2, 3), 3, "red")
    graph_3d.plot_sphere((-1, -2, -3), 2, "yellow")

    # 極座標
    graph_polar = graph2d.graph("title", True, True)
    graph_polar.set_graph_polar(5)
    graph_polar.plot_point_polar("point", 2.0, 1.0, ".", "red")
    graph_polar.plot_point_polar("point", 1, 0.5, ".", "green")
    
    print(parameter.PARAMETER1)
    print(parameter.PARAMETER2)
    function.get_fruit_price(1, 0)
    for i in tqdm(range(10)):
        time.sleep(0.02)


if __name__ == "__main__":

    logger.app_logger.info('Application Ver.%s Start', version.get_version())
    print(console.Fore.RED + "Red")
    print(console.Color.RED + "BLACK" + console.Color.END)
    # rsyslog.open()
    # rsyslog.logging(syslog.LOG_ALERT, 'Application started')
    now = datetime.now()
    start_time = time.time()

    os.system('cls')  # コンソールクリア
    # database.create_table()  # テーブル生成
    logger.logging_environment()  # 実行環境ログ
    config.logging_paramter()  # Parameter読み込み

    translation.init()
    print('*****************************This is sample message.')
    print('This string isn\'t translated.')
    print(console.Fore.RED + "Red")

    proc()

    # line.send_message("Application End")
    proc_time = (time.time()-start_time)
    database.insert(now, proc_time)  # データベース追加
    logger.app_logger.info('Application End(%.6lf[sec])', proc_time)
    print("foo," + console.Fore.BLUE + "bar," + console.Back.RED + "baz")
    # rsyslog.logging(syslog.LOG_ALERT, 'Application End')
    # rsyslog.close()
