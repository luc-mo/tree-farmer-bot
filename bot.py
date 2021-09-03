import pyautogui
import time
import win32api, win32con

def click(x, y, seconds=5):
  win32api.SetCursorPos((x, y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
  win32api.SetCursorPos((0, 0))
  time.sleep(seconds)

images = ['tree_1', 'tree_2']

while True:
  for image in images:
    tree = pyautogui.locateOnScreen(f'./images/{image}.png', confidence=0.7)
    if(tree == None):
      continue
    x = tree.left.item()
    y = tree.top.item()
    click(x, y)
    break
  time.sleep(1)
