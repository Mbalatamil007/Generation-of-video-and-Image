import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("step1: open the chrome browser...")
time.sleep(2)

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)

print("Click inside Chrome within 5 seconds...")
time.sleep(5)

print("Step 2: Go to a website...")
pyautogui.hotkey("ctrl", "t", interval=0.1)
time.sleep(1)

# Focus the address bar
pyautogui.hotkey("ctrl", "l")
time.sleep(0.5)

pyautogui.write("https://weather.com/", interval=0.1)
pyautogui.press("enter")
time.sleep(5)

print("Step 3: copy the full data of the weather website...")
pyautogui.hotkey("ctrl", "a")
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

print("Step 4: open the text editor and paste the data...")
pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("notepad")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
