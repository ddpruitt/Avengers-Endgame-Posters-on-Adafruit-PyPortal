import time
import board
from adafruit_pyportal import PyPortal

# Images
images = [
    'a1.bmp',
    'a2.bmp',
    'a3.bmp',
    'a4.bmp',
    'a5.bmp',
    'a6.bmp',
    'a7.bmp',
    'a8.bmp',
    'a9.bmp',
    'a10.bmp',
    'a11.bmp',
    'a12.bmp',
    'a13.bmp',
    'a14.bmp',
    'a15.bmp',
    'a16.bmp',
    'a17.bmp',
    'a18.bmp',
    'a19.bmp',
    'a20.bmp',
    'a21.bmp',
    'a22.bmp',
    'a23.bmp',
    'a24.bmp',
    'bw.bmp',
    'cap.bmp',
    'hulk.bmp',
    'iron.bmp',
    'marvel.bmp',
    'post.bmp',
    'spider.bmp',
    'thor.bmp',
    'vis.bmp',
    'witch.bmp'
]

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(status_neopixel=board.NEOPIXEL)

# pyportal.play_file(audio)
# speed up projects with lots of text by preloading the font!
pyportal.preload_font()
pyportal.set_backlight(1.00)
i = 0.001

# disp

while True:
    try:

        for image in images:
            pyportal.set_background(image)
            board.DISPLAY.refresh_soon()
            board.DISPLAY.wait_for_frame()
            time.sleep(i)

    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    time.sleep(0.1)