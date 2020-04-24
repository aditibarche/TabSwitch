import pyautogui,time
i=0
while ( i < 10 ):
    print("inside while")
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(60)
    i = i + 1
