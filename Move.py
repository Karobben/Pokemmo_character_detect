from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
import random, time
from time import sleep
keyboard = Controller()

def left():
    keyboard.press(Key.left)
    #sleep(ii)
    #keyboard.release(Key.left)

def right():
    keyboard.press(Key.right)
    #sleep(ii)
    #keyboard.release(Key.right)

def up():
    keyboard.press(Key.up)
    #sleep(ii)
    #keyboard.release(Key.up)

def down():
    keyboard.press(Key.down)
    #sleep(ii)
    #keyboard.release(Key.down)

def run(i):
    if i == 0:
        left()
    elif i == 1:
        down()
    elif i ==2 or i == 4 or i == 5:
        up()
    elif i ==3:
        right()

def stop():
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        keyboard.release(Key.up)
        keyboard.release(Key.down)

def run_random():
    run(random.choice(range(6)))

def Moving(time_A):
    time_B = time.time()
    Time = random.choice(range(20))
    if time_B - time_A > Time:
        time_A =time_B
        stop()
        run_random()
    return time_A

def Battle_go():
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    run_random()
    keyboard.press('z')
    keyboard.release('z')
    stop()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    keyboard.press('z')
    keyboard.release('z')
    stop()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    keyboard.press('z')
    keyboard.release('z')
    stop()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    run_random()
    keyboard.press('z')
    keyboard.release('z')
    stop()
    keyboard.press('x')
    keyboard.release('x')
