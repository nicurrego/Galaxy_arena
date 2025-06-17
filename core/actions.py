class Action:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    STAY = 4
    SHOOT = 5
    
    @classmethod
    def all(cls):
        return [cls.UP, cls.DOWN, cls.LEFT, cls.RIGHT, cls.STAY, cls.SHOOT]
