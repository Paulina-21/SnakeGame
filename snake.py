from enum import Enum
class Directions(Enum):
    Up=1
    Down=2
    Left=3
    Right=4
class Snake:
    def _init(self,coordinates):
        self.coordinates=coordinates
        self.direction=Directions.Right
s1=Snake()
print(s1)
print("Hello world!")
