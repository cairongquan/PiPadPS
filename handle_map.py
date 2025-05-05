from zero_hid import Mouse
from time import sleep

# 和谐列表
harmonyMapper = [
        {
            'top': 'A',
            'bottom': 'F#m',
            'top_left_top':'D',
            'top_left_bottom':'C#m',
            'top_right_top':'E',
            'top_right_bottom':'Bm'
        },
        {
            'top': 'B',
            'bottom': 'G#m',
            'top_left_top':'E',
            'top_left_bottom':'D#m',
            'top_right_top':'F#',
            'top_right_bottom':'C#m'
        },
        {
            'top': 'C',
            'bottom': 'Am',
            'top_left_top':'F',
            'top_left_bottom':'Em',
            'top_right_top':'G',
            'top_right_bottom':'Dm'
        },
        {
            'top': 'Db',
            'bottom': 'Bbm',
            'top_left_top':'Gb',
            'top_left_bottom':'Fm',
            'top_right_top':'Ab',
            'top_right_bottom':'Ebm'
        },
        {
            'top': 'Eb',
            'bottom': 'Cm',
            'top_left_top':'Ab',
            'top_left_bottom':'Gm',
            'top_right_top':'Bb',
            'top_right_bottom':'Fm'
        },
]

# 切换和弦向左边
def l1():
    with Mouse(absolute=True) as m:
        m.move(4300, 18000)
        m.left_click()

# 切换和弦 向右
def r1():
    with Mouse(absolute=True) as m:
        m.move(28400, 18000)
        m.left_click()

# 选择和弦
def dropMouse(position):
    with Mouse(absolute=False) as rel_mouse, Mouse(absolute=True) as m:
        m.move(8500, 17000)
        sleep(0.02)
        m.left_click(release=False)
        sleep(0.02)
        # 向上方拖动
        if position == 'top': rel_mouse.move(0, -20)
        # 向下方拖动
        elif position == 'bottom':rel_mouse.move(0, 20)
        # 向左上方拖动
        elif position == 'top_left_top': rel_mouse.move(-20, -10)
        # 向左下方拖动
        elif position == 'top_left_bottom': rel_mouse.move(-20, 10)
        # 向右上方拖动
        elif position == 'top_right_top': rel_mouse.move(20, -10)
        # 像右下方拖动
        elif position == 'top_right_bottom': rel_mouse.move(20, 10)
        sleep(0.05)
        m.release()

def pluckstrumming(strummingNum):
    with Mouse(absolute=False) as rel_mouse, Mouse(absolute=True) as m:
        # init postion 第一根弦
        m.move(17000,5000)
        sleep(0.1)
        rel_mouse.move(0,(strummingNum - 1) * 6)
        sleep(0.1)
        m.left_click()

#  扫弦 初始位->结束位 从上扫下
def sweepStrumming(startStrumming,endStrumming):
    with Mouse(absolute=False) as rel_mouse, Mouse(absolute=True) as m:
        # init postion 第一根弦
        m.move(17000,5000)
        sleep(0.1)
        rel_mouse.move(0,(startStrumming - 1) * 6)
        sleep(0.1)
        m.left_click(release=False)
        sleep(0.05)
        rel_mouse.move(0,(endStrumming - 1) * 5)
        sleep(0.15)
        m.release()

#  扫弦 初始位->结束位 从下扫上
def sweepStrummingReverse(startStrumming, endStrumming):
    with Mouse(absolute=False) as rel_mouse, Mouse(absolute=True) as m:
        # init postion 最后一根弦
        m.move(17000,7500 + (startStrumming * 300))
        sleep(0.1)
        m.left_click(release=False)
        sleep(0.2)
        rel_mouse.move(0,-30 + ((endStrumming-1) * 5))
        sleep(0.15)
        m.release()