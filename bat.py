import pyautogui
import pyperclip
import win32gui
import win32con
import time

INTERVAL = 0.5


def press(key):
    pyautogui.press(key)
    time.sleep(INTERVAL)


def startGame():
    press("t")
    pyautogui.write(".tp 2155.97 61.00 92.07")
    press("enter")
    press("esc")
    pyautogui.click()


def getSand():
    press("t")
    pyautogui.write(".tp 2147.27 52 51.60")
    press("enter")
    press("esc")


def endGame():
    press("t")
    pyautogui.write(".tp 2159 52 85.98")
    press("enter")
    press("esc")


print("WARN: This tool requires Horion or other utility mods to teleport")

win32gui.SetForegroundWindow(win32gui.FindWindow(None, "Minecraft"))
time.sleep(0.2)
press("esc")

try:
    while True:
        startGame()
        time.sleep(0.5)
        getSand()
        time.sleep(0.5)
        endGame()
except:
    print("Complete!")
