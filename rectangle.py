class Rectangle(object):

    def __init__(self, topleftx, toplefty, bottomrightx, bottomrighty):
        self._topleftx = topleftx
        self._toplefty = toplefty
        self._bottomrightx = bottomrightx
        self._bottomrighty = bottomrighty

    def getArea(self):

        horizontal = self._bottomrightx - self._topleftx
        vertical = self._toplefty - self._bottomrighty
        return horizontal * vertical

    def __eq__(self, otherrect):

        if self.getArea() == otherrect.getArea():
            return True
        else:
            return False

    def __ne__(self, otherrect):
        
        if self.getArea() != otherrect.getArea():
            return True
        else:
            return False   

    def __lt__(self, otherrect):
        if self.getArea() < otherrect.getArea():
            return True
        else:
            return False     

    def __gt__(self, otherrect):
        if self.getArea() > otherrect.getArea():
            return True
        else:
            return False 

    def __str__(self):

        return ("TopLeft: (%d,%d) - BottomRight: (%d,%d)" % (self._topleftx, self._toplefty, self._bottomrightx, self._bottomrighty))

if __name__ == "__main__":

    rect1 = Rectangle(10, 10, 20, 20)
    rect2 = Rectangle(10, 10, 30, 30)

    print(rect1 == rect2)
    print(rect1 != rect2)
    print(rect1 < rect2)
    print(rect1 > rect2)