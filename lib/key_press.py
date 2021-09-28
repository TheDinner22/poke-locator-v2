# press keys to simulate a mc command

# dependencies
import pyautogui, time

def type_lt():
    # press '/'
    pyautogui.keyDown('/')
    time.sleep(0.2)
    pyautogui.keyUp('/')

    # press 'l'
    pyautogui.keyDown('l')
    time.sleep(0.2)
    pyautogui.keyUp('l')

    # press 't'
    pyautogui.keyDown('t')
    time.sleep(0.2)
    pyautogui.keyUp('t')

    # press enter
    pyautogui.keyDown('enter')
    time.sleep(0.2)
    pyautogui.keyUp('enter')

if __name__ == "__main__":
    type_lt()
    