import parts


# The Computer class is a Facade class which will simplify the computer part classes.
# You should implement this class
# This class should be able to be called by the running part
class Computer:
    def __init__(self):
        self.cpu=parts.CPU()
        self.mem=parts.Memory()
        self.hd=parts.HardDisk()
    # implement the class below this line    
        

    def startComputer(self):
        print("Computer is bein started....")
        self.cpu.check()
        self.mem.load()
        self.hd.mount()
        print("Boot Sequence Complete")
        print(" ")
    
    def printCPUInfo(self):
        self.cpu.getInfo()
    def printMemInfo(self):
        self.mem.getInfo()
    def printHDInfo(self):
        self.hd.getInfo()





# The running part
# Don't modify the following code!
com=Computer()
com.startComputer()
com.printCPUInfo()
com.printMemInfo()
com.printHDInfo()
