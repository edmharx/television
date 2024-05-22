from TV import Television
import keyboard

tv_1 = Television(30, 3)
tv_2 = Television(3, 2)

#showcase the methods
#create a working remote control for tv using keyboard press



#hotkeys for tv 1
keyboard.add_hotkey('tab', tv_1.turnOn)
keyboard.add_hotkey('esc', tv_1.turnOff)
keyboard.add_hotkey('w', tv_1.volumeUp)
keyboard.add_hotkey('d', tv_1.channelUp)
keyboard.add_hotkey('a', tv_1.channelDown)
keyboard.add_hotkey('s', tv_1.volumeDown)
keyboard.add_hotkey('z', tv_1.setChannel)
keyboard.add_hotkey('x', tv_1.setVolume)
keyboard.add_hotkey('q', tv_1.getChannel)
keyboard.add_hotkey('e', tv_1.getVolume)
keyboard.wait('shift+tab')
