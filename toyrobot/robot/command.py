from re import compile, X

PATTERN = compile(
    r"""
        (?P<x>\d+),                  # x coord
        (?P<y>\d+),                  # y coord
        (?P<f>NORTH|EAST|SOUTH|WEST) # facing
        """, X
)


def parse(line):
    """Parse one command line and return valid components

    An exception is raised if the line does not correspond to a valid command
    string.
    """

    tokens = line.strip().split()
    tokens = [t.upper() for t in tokens]

    cmd = tokens[0]
    if cmd not in {'MOVE', 'LEFT', 'RIGHT', 'REPORT', 'PLACE'}:
        raise InvalidCommand

    coords = None
    if cmd == 'PLACE':
        if len(tokens) < 2:
            raise InvalidCommand

        valid = PATTERN.search(tokens[1])
        if not valid:
            raise InvalidCommand

        coords = dict(
            x=int(valid['x']),  # regexp ensures the str is a digit
            y=int(valid['y']),
            f=valid['f'],
        )

    return cmd, coords


class InvalidCommand(Exception):
    """Raised when an invalid command is given"""
    pass
