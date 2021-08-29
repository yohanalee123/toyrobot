from toyrobot.robot.position import Position, InvalidPosition

# A simple ring implemented as nested dicts (a whole class would be overkill)
COMPASS = {
    'NORTH': {
        'left': 'WEST',
        'right': 'EAST'
    },
    'WEST': {
        'left': 'SOUTH',
        'right': 'NORTH'
    },
    'SOUTH': {
        'left': 'EAST',
        'right': 'WEST'
    },
    'EAST': {
        'left': 'NORTH',
        'right': 'SOUTH'
    },
}


def has_position(method):
    def wrapper(self):
        if not self._position:
            return
        method(self)

    return wrapper


class Robot():
    """Simulate a robot moving on a 5x5 grid"""

    _position = None

    def place(self, coords):
        """Place robot at the specified position on the table"""
        try:
            self._position = Position(coords)
        except InvalidPosition:
            pass

    @has_position
    def move(self):
        """Move the robot one unit in the direction it is currently facing"""
        c = self._position.coords()
        try:
            f = c['f']
            if f == 'NORTH':
                c['y'] += 1
            elif f == 'EAST':
                c['x'] += 1
            elif f == 'SOUTH':
                c['y'] -= 1
            elif f == 'WEST':
                c['x'] -= 1

            self._position = Position(c)
        except InvalidPosition:
            pass

    @has_position
    def left(self):
        """Rotate the robot 90 degrees to the left"""
        c = self._position.coords()
        try:
            f = c['f']
            c['f'] = COMPASS[f]['left']
            self._position = Position(c)
        except InvalidPosition:
            pass

    @has_position
    def right(self):
        """Rotate the robot 90 degrees to the right"""
        c = self._position.coords()
        try:
            f = c['f']
            c['f'] = COMPASS[f]['right']
            self._position = Position(c)
        except InvalidPosition:
            pass

    @has_position
    def report(self):
        """Print the current position of the robot"""
        print(self._position)
