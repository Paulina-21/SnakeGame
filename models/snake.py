from .directions import Directions
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