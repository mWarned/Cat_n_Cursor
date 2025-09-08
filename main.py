from time import sleep

import pyautogui
import win32gui
# from screeninfo import get_monitors

import PetCat

def desktop_in_focus() -> bool:
    # monitors = get_monitors()

    hwnd = win32gui.GetForegroundWindow()
    class_name = win32gui.GetClassName(hwnd)

    if class_name in ("Progman", "WorkerW"):
        return True
    else :
        return False


if __name__ == '__main__':
    pet = PetCat.PetCat()
    pet.load_image()

    while True:
        cursorX, cursorY = pyautogui.position()

        if desktop_in_focus():
            pet.show_cat()
            pet.chases(cursorX, cursorY)
        else:
            print("Cat sleeps")
        sleep(0.02)