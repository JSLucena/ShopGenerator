class Item:
    def __init__(self, name, price, rarity, typ):
        self.__name = name
        self.__price = price
        self.__rarity = rarity
        self.__typ = typ

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getPrice(self):
        return self.__price
    
    def setPrice(self, price):
        self.__price = price

    def getRarity(self):
        return self.__rarity
    
    def setRarity(self, rarity):
        self.__rarity = rarity
    
    def getType(self):
        return self.__typ
    
    def setType(self, typ):
        self.__typ = typ


