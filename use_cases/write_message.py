import pyautogui as py

def write_message(message):
  py.moveTo(x=2300, y=800, duration=1)
  py.leftClick()
  py.write(message)