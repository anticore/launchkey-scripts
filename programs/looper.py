from time import sleep


def looper(lk, time):
    leds = lk.rows[0] + lk.rows[1][::-1]
    colors = [
        80, 124, 125, 126, 127, 123, 107, 83, 3, 2, 1
    ]

    start_index = time % len(leds)
    end_index = (start_index + len(colors)) % len(leds)
    curr_leds = leds[start_index:end_index] if end_index >= start_index else leds[start_index:] + leds[:end_index]

    for index, led in enumerate(curr_leds):
        lk.led(led, colors[index])

    sleep(0.1)
