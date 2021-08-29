#! ../env/bin/python

import pytest

@pytest.fixture
def robot():
    """A simple fixture providing a robot instance"""
    from toyrobot.robot import Robot
    return Robot()
