#create tv class
#create parameters for tv
#create functions for tv
#set values for each parameter

class Television:
    def __init__(self, channel, volume):
        #create attributes
        self.channel = channel
        self.volume = volume

    #set methods
    def turnOn(self):
        print("This TV is turned on")

    def turnOff(self):
        print("This TV is turned off")

    def getChannel(self):
        print(f'The channel is {self.channel}')
    
    def setChannel(self):
        while True:
            channel = int(input("Please input the channel (1-120)"))
            if channel < 1 or channel > 120:
                print("The channels are only 1-120")
            else:
                self.channel = channel
                print(f'The current channel is {channel}')
                break

    def getVolume(self):
        print(f'The volume is {self.volume}')
    
    def setVolume(self):
        while True:
            volume = int(input("Please input the volume (1-7)"))
            if volume < 1 or volume > 7:
                print("The channels are only 1-7")
            else:
                self.volume = volume
                print(f'The current volume is {volume}')
                break

    def channelUp(self):
        if self.channel == 120:
            print("Already at last channel")
        else: 
            channel = self.channel + 1
            self.channel = channel
            print(f"The channel is now {self.channel}")

    def channelDown(self):
        if self.channel == 1:
            print("Already at last channel")
        else: 
            channel = self.channel - 1
            self.channel = channel
            print(f"The channel is now {self.channel}")

    def volumeUp(self):
        if self.volume == 7:
            print("Already at highest volume")
        else: 
            volume = self.volume + 1
            self.volume = volume
            print(f"The volume is now {self.volume}")

    def volumeDown(self):
        if self.volume == 1:
            print("Already at lowest volume")
        else: 
            volume = self.volume - 1
            self.volume = volume
            print(f"The volume is now {self.volume}")