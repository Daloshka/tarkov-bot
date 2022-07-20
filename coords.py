import pyautogui
import time
import keyboard

lastCoords = None

while True:
    if lastCoords is not None:   
        keyboard.wait('ctrl')
        print(f"x {pyautogui.position()[0] - lastCoords[0]}, y {pyautogui.position()[1] - lastCoords[1]}")
        lastCoords = [pyautogui.position()[0], pyautogui.position()[1]]
        lastCoords = None
    else:
        keyboard.wait('ctrl')
        print(pyautogui.position())
        lastCoords = [pyautogui.position()[0], pyautogui.position()[1]]