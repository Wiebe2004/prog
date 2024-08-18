class Flag:
    def __init__(self,country,colors,horizontal):
        self.country = country
        self.horizontal = horizontal
        self.__colors = colors

    @property
    def colors(self):
            return self.__colors
        
    @colors.setter
    def colors(self,colors):
        if colors is None or len(colors) <= 0:
            raise ValueError("Vlag heeft geen kleuren")
        self.__colors = colors

    def __printColors(self):    
        res = ""
        for c in self.colors:
            res += c + " "
        return res[:-1]
        
    def get_info(self):
        ori = ""
        if self.horizontal == True:
            ori = "Horizontal"
        else:
            ori = "Vertical"
        return f"Flag of {self.country}\nColors: {self.__printColors()}\nOrientation: {ori}"
    

class Parade:
    def __init__(self,name):
        self.name = name
        self.__flags = list()

    @property
    def flags(self):
        return self.__flags
    
    def __findFlagIndex(self,country):
        for f in range(0,len(self.flags)):
            if self.__flags[f].country.lower() == country.lower():
                return f
        return -1

    def add_flag(self,flag):
        if self.__findFlagIndex(flag.country) < 0:
            self.__flags.append(flag)
        
    def remove_flag(self,country):
        if self.__findFlagIndex(country) >=0:
            idx = self.__findFlagIndex(country)
            self.__flags.pop(idx)


        
belgian_flag = Flag("Belgium",("black","yellow","red"),False)
german_flag = Flag("Germany",("black","red","yellow"),True)
spanish_flag = Flag("Spain",("red","yellow","red"),True)
dutch_flag = Flag("Netherlands",("red","white","blue"),False)

erasmus_parade = Parade("Erasmus Parade")

erasmus_parade.add_flag(belgian_flag)
erasmus_parade.add_flag(german_flag)
erasmus_parade.add_flag(spanish_flag)
erasmus_parade.add_flag(dutch_flag)

erasmus_parade.remove_flag("netherlands")

for flag in erasmus_parade.flags:
        print(flag.get_info())
