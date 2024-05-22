#create tv class
#create parameters for tv
#create functions for tv
#set values for each parameter

class Television:
    def __init__(self, name, channel, volume):
        #create attributes
        self.name = name
        self.channel = channel
        self.volume = volume

    #set methods
    def turnOn(self):
        print(f"{self.name} is turned on")

    def turnOff(self):
        print(f"{self.name} is turned off")

    def getChannel(self):
        print(f'The channel is {self.channel}')
    
    def setChannel(self):
        while True:
            channel = int(input(f"Please input the channel for {self.name} (1-120)"))
            if channel < 1 or channel > 120:
                print("The channels are only 1-120")
            else:
                self.channel = channel
                print(f'The current channel of {self.name} is {channel}')
                break

    def getVolume(self):
        print(f"{self.name} volume is {self.volume}")
    
    def setVolume(self):
        while True:
            volume = int(input(f"Please input the volume for {self.name} (1-7)"))
            if volume < 1 or volume > 7:
                print("The channels are only 1-7")
            else:
                self.volume = volume
                print(f'The current volume for {self.name} is {volume}')
                break

    def channelUp(self):
        if self.channel == 120:
            print(f"{self.name} is already at last channel")
        else: 
            channel = self.channel + 1
            self.channel = channel
            print(f"{self.name} channel is now {self.channel}")

    def channelDown(self):
        if self.channel == 1:
            print(f"{self.name} is already at last channel")
        else: 
            channel = self.channel - 1
            self.channel = channel
            print(f"{self.name} channel is now {self.channel}")

    def volumeUp(self):
        if self.volume == 7:
            print(f"{self.name} is already at highest volume")
        else: 
            volume = self.volume + 1
            self.volume = volume
            print(f"The volume of {self.name} is now {self.volume}")

    def volumeDown(self):
        if self.volume == 1:
            print(f"{self.name} is already at lowest volume")
        else: 
            volume = self.volume - 1
            self.volume = volume
            print(f"The volume of {self.name} is now {self.volume}")