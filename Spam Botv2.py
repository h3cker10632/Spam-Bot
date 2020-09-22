from pynput.keyboard import Key, Controller
import time

print("""
░█████╗░███████╗███╗░░██╗████████╗██████╗░░█████╗░██╗░░░░░  ░██████╗██████╗░░█████╗░███╗░░░███╗
██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░  ██╔════╝██╔══██╗██╔══██╗████╗░████║
██║░░╚═╝█████╗░░██╔██╗██║░░░██║░░░██████╔╝███████║██║░░░░░  ╚█████╗░██████╔╝███████║██╔████╔██║
██║░░██╗██╔══╝░░██║╚████║░░░██║░░░██╔══██╗██╔══██║██║░░░░░  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
╚█████╔╝███████╗██║░╚███║░░░██║░░░██║░░██║██║░░██║███████╗  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
░╚════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝""")




k = input("Enter Message:")
count = int(input("Number of times to send message:"))
message = k
keyboard = Controller()
time.sleep(5)
print("You Have 5 seconds to click a text box")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
 #next to range put the number of messages you are sending
for i in range(count):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

if keyboard.release(Key.enter):
    print("Message sent")
 