import pyautogui as py

def write_subject(subject): 
  py.moveTo(x=2000, y=765, duration=1)
  py.leftClick()
  py.write(subject)

