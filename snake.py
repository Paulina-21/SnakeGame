from enum import Enum
import numpy as np

class Directions(Enum):
    Up=1
    Down=2
    Left=3
    Right=4 

class Snake:
    """ 
    Snake Class

    Attributes 
    ----------    
        coordinates : list[int, int]
            The head is the first in list.
            First position is y, next is x
            A line is created first, elements are added to it 

    Methods
    -------
        move(directions: Directions)
            move the snake

    
    """
    coordinates:list[int,int]
    direction:Directions

    def __init__(self,coordinates):
        self.coordinates=coordinates
        self.direction=Directions.Right
    

    def move(self,direction):
        #get direction
        self.direction=direction
        #remove last (tail)
        del self.coordinates[-1]
        #change head position
        if direction==Directions.Left:
            self.coordinates.insert(0,[self.coordinates[0][0],self.coordinates[0][1]-1])
        if direction== Directions.Right:
            self.coordinates.insert(0,[self.coordinates[0][0],self.coordinates[0][1]+1])
        if direction==Directions.Up:
            self.coordinates.insert(0,[self.coordinates[0][0]-1,self.coordinates[0][1]])
        if direction==Directions.Down:
            self.coordinates.insert(0,[self.coordinates[0][0]+1,self.coordinates[0][1]])

class PlayGround:
    """
    PlayGround Class
    for future improvements (ex. obstacles)
    """
    def __init__(self,n):
        self.n=n      

class View:
    """
    View Class

    Attributes
    ----------
        matrix: list[list[int,int]]
    
    Methods
    -------
        draw(snake: Snake)
        
    """
    matrix:list[list[int,int]]=[]
    def __init__(self,playGround:PlayGround):
        self.playGround=playGround
    
    def draw(self,new_snake:Snake):
        if (new_snake.coordinates[0][0]<0 or 
            new_snake.coordinates[0][1]<0 or 
            new_snake.coordinates[0][0]>=self.play.n or
            new_snake.coordinates[0][1]>=self.play.n):
                raise Exception("You hit the wall")
        self.matrix=[]

        for y_coord in range (self.play.n):
            self.matrix.append([])
            for x_coord in range(self.play.n):
                #add 1 if coordinates of snake
                if [y_coord,x_coord] in new_snake.coordinates:
                    self.matrix[y_coord].append(1)
                else: self.matrix[y_coord].append(0)
            print(self.matrix[y_coord])
                
        
try:
    
    s1=Snake([[2,2],[2,3]]) 

    p1=PlayGround(10)
    print(p1)
    v1=View(p1)
    v1.draw(s1)
    s1.move(Directions.Up)
    print()
    print()
    v1.draw(s1)
    s1.move(Directions.Up)
    print()
    print()
    v1.draw(s1)
    s1.move(Directions.Up)
    print()
    print()
    v1.draw(s1)
except Exception as ex:
    print(ex)


