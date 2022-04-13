
# Online Python - IDE, Editor, Compiler, Interpreter

import pyautogui
import time

groups = ['fallschurchvahomeschoolers', '962220134329459', '3315205681937491']

time.sleep(5)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')

for i in range(len(groups)):
    link = 'https://facebook.com/groups/'+groups[i]
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')
    
    print("Waiting for 45seconds to post into the FB Group\n")
    time.sleep(45)
    
    pyautogui.typewrite('p')
    time.sleep(5)
    
    print("Writing post on FB Group\n")
    pyautogui.typewrite("Hello WEquil, this is a testing post for an automated feature")
    time.sleep(3)
    
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')
    
    time.sleep(3)
    
    pyautogui.write(['f6'])
    time.sleep(1)