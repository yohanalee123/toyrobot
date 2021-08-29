# These module level constants are used to restrict the possible positions on
# the table

X_RANGE = {0, 1, 2, 3, 4}
Y_RANGE = {0, 1, 2, 3, 4}
F_RANGE = {'NORTH', 'EAST', 'SOUTH', 'WEST'}


class Position():
    _x = None
    _y = None
    _f = None

    def __init__(self, c):
        if c['x'] in X_RANGE and c['y'] in Y_RANGE and c['f'] in F_RANGE:
            self._x = c['x']
            self._y = c['y']
            self._f = c['f']
        else:
            raise InvalidPosition

    def coords(self):
        return dict(x=self._x, y=self._y, f=self._f)

    def __str__(self):
        return "{},{},{}".format(self._x, self._y, self._f)


class InvalidPosition(Exception):
    """Raised when a position is specified that does not fit on the table"""
    pass
