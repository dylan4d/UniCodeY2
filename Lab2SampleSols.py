#Part 1
def getLongestWord(filename):
   
    result = []
    file = open(filename, "r")
    largest = 0
    for line in file:
        if len(line) > largest:
            largest = len(line)
    file.seek(0)
    for line in file:
        if len(line) == largest:
            result.append(line)
    return result

print(getLongestWord("sample.txt"))

#Part 2
def getLineCount(filename):
    file = open(filename, "r")
    line_count = 0
    for line in file:
        line_count += 1
    return line_count

print("There are %d lines" % getLineCount("myfile.txt"))

#Part 3
class Point(object):

   def __init__(self, xval, yval):
      self._x = xval
      self._y = yval
       
   def getX(self):
      return self._x
      
   def setX(self, xval):
      self._x = xval

   def getY(self):
      return self._y

   def setY(self, yval):
      self._y = yval
      
   def __str__(self):
       return "x val: %d y val: %d" % (self._x, self._y)
       
   x = property(getX, setX)
   y = property(getY, setY)


point = Point(10, 10)
point.y = 20
print(point)
