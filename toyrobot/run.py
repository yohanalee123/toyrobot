import fileinput


from robot import Robot
from robot.command import *


def main():
    """Run Mr Robot, run!

    Simulate a robot interactively."""
    robot = Robot()

    for line in fileinput.input():
        try:
            (cmd, coords) = parse(line)
            if cmd == 'PLACE':
                robot.place(coords)
            else:
                # Assume Robot has a method for each valid command.
                # (A potential weak point, but this is covered sufficiently by
                # the command_pattern testing)
                getattr(robot, cmd.lower())()

        except InvalidCommand:
            # Silently ignore invalid commands
            pass


if __name__ == "__main__":
    main()
