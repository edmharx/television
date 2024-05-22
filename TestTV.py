from TV import Television
import keyboard

tv_1 = Television(30, 3)
tv_2 = Television(3, 2)

#showcase the methods
#create a working remote control for tv using keyboard press


on = True
while on:
    #hotkeys for tv 1
    keyboard.add_hotkey('d', tv_1.channelUp)
    keyboard.wait()
    keyboard.add_hotkey('a', tv_1.channelDown)
    keyboard.wait()
    keyboard.add_hotkey('s', tv_1.volumeDown)
    keyboard.wait()
    keyboard.add_hotkey('w', tv_1.volumeUp)
    keyboard.wait()
    keyboard.add_hotkey('esc', tv_1.turnOff)
    keyboard.wait()
