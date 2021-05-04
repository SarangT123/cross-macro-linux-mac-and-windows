import pyautogui
import keyboard
import time

print('Packages loaded')

hotkey = input("Enter the key to be set as hotkey : ")


difficulty = int(input('input the difficulty "0 - normal , 1 - hard , 2 - easy" : '))


delay = int(input("Enter the dealy between click in milliseconds (minimum 70 recomended 3000) : ")) / 1000

print ('open minecraft in fullscreen with focus. you can minimize this window')
print ('this macro will start in 3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('macro started')

while True:
    if keyboard.is_pressed(hotkey) == True:
        print('reset initiatiated')

        pyautogui.press('Esc')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(delay)
        pyautogui.press('enter')

        print('escape done')

        pyautogui.press('tab')
        time.sleep(delay) 
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1)
        pyautogui.press('tab')        
        time.sleep(delay) 
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('tab')
        time.sleep(0.1) 
        pyautogui.press('tab')

        print('part done')

        if difficulty == 0:
            print('no change in diff')
        elif difficulty == 1:
            pyautogui.press('tab')
            time.sleep(0.01)
            pyautogui.press('enter')
        elif difficulty == 2:
            pyautogui.press('tab')
            time.sleep(0.01)
            pyautogui.press('tab')
            time.sleep(0.01)
            pyautogui.press('enter')

        print('difficulty set')

        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(0.01)
        pyautogui.press('tab')
        time.sleep(delay)
        pyautogui.press('enter')

        print('resetted')

        pass





                                                                                                                                                                                                                
