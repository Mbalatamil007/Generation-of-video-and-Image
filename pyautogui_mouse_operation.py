import pyautogui
import time

time.sleep(3)  # Wait for 3 seconds before starting the mouse operations
#mouse operation
pyautogui.moveTo(100, 100, duration=1)  # Move the mouse to (100, 100) over 1 second

pyautogui.moveRel(200, 0, duration=1)  # Move the mouse 200 pixels to the right over 1 second
pyautogui.moveRel(0, 200, duration=1)  # Move the mouse 200 pixels down over 1 second
pyautogui.click()  # Click the mouse at the current position
pyautogui.doubleClick()  # Double-click the mouse at the current position
pyautogui.rightClick()  # Right-click the mouse at the current position
pyautogui.click(100, 100)  # Click the mouse at (100, 100)
pyautogui.rightClick(200, 200)  # Right-click the mouse at (200, 200)
pyautogui.scroll(500)  # Scroll up 500 units
pyautogui.leftClick(100, 100)  # Left-click the mouse at (100, 100)
pyautogui.dragTo(300, 300, duration=1)  # Drag the mouse to (300, 300) over 1 second

pyautogui.scroll(-500)  # Scroll down 500 units
time.sleep(3)  # Wait for 3 seconds
pyautogui.scroll(1000)  # Scroll up 1000 units
pyautogui.scroll(-1000)  # Scroll down 1000 units