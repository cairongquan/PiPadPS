# 抖音
from zero_hid import Mouse
from time import sleep

page = 0
status = True

# 抽奖
def click_chord():
    with Mouse(absolute=True) as m:
        m.move(2200,3800)
        sleep(1)
        m.left_click()
        sleep(1)
        m.move(2800,30800)
        sleep(1)
        m.left_click()
        sleep(1)
        m.move(16400,18000)
        sleep(1)
        m.left_click()

def drove_page_next():
    global page
    global status
    with Mouse(absolute=True) as m,Mouse(absolute=False) as mouse:
        m.move(16400,15000)
        sleep(0.5)
        m.left_click(release=False)
        sleep(0.2)
        mouse.move(0,-50)
        sleep(0.2)
        mouse.move(0,-20)
        sleep(1)
        m.release()
    page += 1
    if page >= 4:
        status = False

def drove_page_prev():
    global page
    global status
    with Mouse(absolute=True) as m,Mouse(absolute=False) as mouse:
        m.move(16400,15000)
        sleep(0.5)
        m.left_click(release=False)
        sleep(0.2)
        mouse.move(0,50)
        sleep(0.2)
        mouse.move(0,20)
        sleep(1)
        m.release()
    page -= 1
    if page <= 0:
        page = 0
        status = True

while True:
    click_chord()
    sleep(18)
    if status:
        drove_page_next()
    else:
        drove_page_prev()
    sleep(10)