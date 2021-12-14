class Person:
    def __init__(self, name = "", address = ""):
        self.__name = name
        self.__address = address

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def toString(self):
        return "{}({})".format(self.getName(), self.getAddress())

