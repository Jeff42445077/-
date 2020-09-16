加载背景音乐
（设置音乐单曲循环）
我方飞机诞生
interval = 0

while True:
    if 用户是否点击关闭按钮:
        退出程序

    interval = interval + 1

    if interval == 50 :
        interval = 0
        小飞机诞生
         
    小飞机移动一个位置
    屏幕刷新

    if 用户移动鼠标:
        我方飞机中心位置 = 用户鼠标位置
        屏幕刷新
    if 我方飞机与敌方飞机产生冲突:
        我方挂
        播放撞机背景音乐
        修改我方飞机图案
        打印 game over
        淡出停止背景音乐
