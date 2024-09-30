import pyautogui as py

def write_receptors_emails(receptors):
   py.moveTo(x=2300,y=650, duration=1)
   py.leftClick() 

   for receptor in receptors: 
     py.write(receptor)
     py.press('enter', interval=1)
