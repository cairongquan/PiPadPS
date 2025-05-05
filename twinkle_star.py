from time import sleep
from handle_map import dropMouse, pluckstrumming

def play_twinkle_twinkle(bpm=120):
    # 每拍的间隔
    beat_interval = 30 / bpm

    # 当前和弦
    active_harmony = 'top'

    # 小星星旋律与和弦
    melody = [
        ('top', 5, 1), ('top', 5, 1),
        ('top_right_top', 3, 1), ('top_right_top', 3, 1),
        ('top_left_top', 3, 1), ('top_left_top', 3, 1),
        ('top_right_top', 3, 2),

        ('top', 4, 1), ('top', 4, 1),
        ('top_left_top', 4, 1), ('top_left_top', 4, 1),
        ('top_right_top', 4, 1), ('top_right_top', 4, 1),
        ('top', 5, 2),

        ('top_left_top', 3, 1), ('top_left_top', 3, 1),
        ('top', 4, 1), ('top', 4, 1),
        ('top_left_top', 4, 1), ('top_left_top', 4, 1),
        ('top_right_top', 4, 2),

        ('top_right_top', 3, 1), ('top_right_top', 3, 1),
        ('top', 4, 1), ('top', 4, 1),
        ('top_left_top', 4, 1), ('top_left_top', 4, 1),
        ('top_right_top', 3, 2),

        ('top', 5, 1), ('top', 5, 1),
        ('top_right_top', 3, 1), ('top_right_top', 3, 1),
        ('top_left_top', 3, 1), ('top_left_top', 3, 1),
        ('top_right_top', 3, 2),

        ('top', 4, 1), ('top', 4, 1),
        ('top_left_top', 4, 1), ('top_left_top', 4, 1),
        ('top_right_top', 4, 1), ('top_right_top', 4, 1),
        ('top', 5, 2),
    ]

    # 播放旋律与和弦
    for harmony, string, duration in melody:
        # 如果和弦发生变化，切换和弦
        if active_harmony != harmony:
            print(f"Changing harmony: {active_harmony} -> {harmony}")
            dropMouse(harmony)
            active_harmony = harmony
            sleep(0.08)  # 切换和弦的间隔

        # 播放音符
        pluckstrumming(string)
        print(f"Playing note: Harmony {harmony}, String {string}")
        sleep(beat_interval * duration)

# 调用播放函数
play_twinkle_twinkle(bpm=120)
