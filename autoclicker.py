import pyautogui
from pynput.keyboard import *
import time

#  ======== settings ========
delay = 1  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
keys = [KeyCode.from_char(c) for c in "f"]
keyboard = Controller()
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// Keyboard AutoClicker - a syntaxval modified fork of iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            keyboard.press("f")
            keyboard.release("f")
            time.sleep(delay)
    lis.stop()


if __name__ == "__main__":
    main()
