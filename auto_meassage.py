import pyautogui
import time
import keyboard  # for stopping

# Give yourself time to open WhatsApp chat
print("You have 10 seconds to open the chat...")
time.sleep(10)

message = "oiii!!"
delay = 0.1  #seconds between messages

print("Press 'q' to stop...")

while True:
    if keyboard.is_pressed('q'):
        print("Stopped by user.")
        break
    
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(delay)
