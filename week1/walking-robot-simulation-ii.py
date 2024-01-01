class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        # find the next direction
        self.next_dir = {
            'East': 'North',
            'North': 'West',
            'West': 'South',
            'South': 'East'
        }
        # moves based on current direction
        self.moves = {
            'East': [1, 0],
            'North': [0, 1],
            'West': [-1, 0],
            'South': [0, -1]
        }

        # current loc and direction
        self.loc = [0, 0]
        self.dir = 'East'

        # moving one turn in the board
        self.one_turn = self.width * 2 + self.height * 2

    def step(self, num: int) -> None:

        # Calculate the number of turns
        if num > self.one_turn:
            num = num - (num // self.one_turn) * self.one_turn

            # Only happens for [0, 0] since the initial direction is [0,0]
            # and the direction is East instead of South
            if num == 0 and self.loc == [0, 0]:
                self.dir = 'South'

        # Move the robot maximum each time 
        while num > 0:
            cur_move = self.moves[self.dir]
            max_move = min(self.max_move_dir(), num)
            num -= max_move
            new_width, new_height = self.loc[0] + cur_move[0] * max_move, self.loc[1] + cur_move[1] * max_move
            self.loc = [new_width, new_height]
            # only if there is still move, we need to change the direction
            if num > 0:
                self.dir = self.next_dir[self.dir]

    # return the maximum move the robot can make in the direction
    def max_move_dir(self):
        if self.dir == 'East':
            return self.width - self.loc[0]
        if self.dir == 'North':
            return self.height - self.loc[1]
        if self.dir == 'West':
            return self.loc[0] - 0
        if self.dir == 'South':
            return self.loc[1] - 0

    def getPos(self) -> List[int]:
        return self.loc

    def getDir(self) -> str:
        return self.dir


