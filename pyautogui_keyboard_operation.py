import pyautogui
import time
import subprocess
import pyscreeze

'''
# Open Notepad automatically
subprocess.Popen("notepad.exe")

# Wait for Notepad to open
time.sleep(3)

# Type text
pyautogui.write("Learning PyAutoGUI Keyboard Operations", interval=0.05)

# Press Enter
pyautogui.press("enter")

# Type second line
pyautogui.write("Hello World", interval=0.05)

# Select all
pyautogui.hotkey("ctrl", "a")

time.sleep(1)

# Copy
pyautogui.hotkey("ctrl", "c")

time.sleep(1)

# Move to the end
pyautogui.press("end")

# Press Enter twice
pyautogui.press("enter", presses=2)

# Paste copied text
pyautogui.hotkey("ctrl", "v")

time.sleep(1)

# Type using Shift key
pyautogui.press("enter")

pyautogui.keyDown("shift")
pyautogui.write("hello")
pyautogui.keyUp("shift")
'''

screenshot = pyautogui.screenshot()
screenshot.save("final.png")  # Save the screenshot to a file