import pyautogui
import time
import pyperclip
from datetime import datetime
pyautogui.FAILSAFE = True
pyautogui.PAUSE=0.5

print("Step 1 : Open the Chrome Browser ...")
time.sleep(2)
pyautogui.hotkey('win','r')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

print("Step 2 : Go to the news website France24 ...")
time.sleep(1)
pyautogui.hotkey('ctrl','t',interval=0.1)
time.sleep(1)
pyautogui.write('https://www.france24.com/en/',interval=0.1) 
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

print("Step 3 : Copy the informations from site ...")
time.sleep(1)
pyautogui.hotkey('ctrl','a')
time.sleep(1)
pyautogui.hotkey('ctrl','c')
time.sleep(1)

print("Step 4 : Open Microsoft Excel ...")
time.sleep(2)
pyautogui.hotkey('win','r')
time.sleep(1)
pyautogui.write('excel')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')

print("Step 5 : Creating new rows ...")
time.sleep(1)
# Row 1
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
pyautogui.write(current_time,interval=0.1)
pyautogui.press("enter")

# Row 2
pyautogui.hotkey("ctrl", "v",interval=0.1)
pyautogui.press("enter")

# Row 3
pyautogui.write("News collected automatically")
time.sleep(2)

print("Step 6 : Save the Excel File ...")
time.sleep(2)

pyautogui.press("f12")
time.sleep(3)

today = datetime.now().strftime("%Y-%m-%d")
filename = f"daily_report_{today}.xlsx"
pyautogui.write(filename, interval=0.05)
pyautogui.press("enter")
time.sleep(5)

print("Step 7 : Take the screenshot ...")
time.sleep(2)
pyautogui.screenshot("final_sheet.png")

print("Task Completed!")


