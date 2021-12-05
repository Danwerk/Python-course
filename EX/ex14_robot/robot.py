"""Robot."""
from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesnt matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(30)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    while not robot.get_right_line_sensors()[2] < 512:
        if robot.get_left_line_sensors()[2] == 0:
            break
        else:
            robot.set_wheels_speed(10)
            robot.sleep(0.1)

    i = 20
    while True:
        if i == 0:
            break
        else:
            robot.set_wheels_speed(10)
            robot.sleep(0.1)
            i -= 1
    robot.set_wheels_speed(0)
    robot.done()


def follow_the_line(robot: FollowerBot):
    """
    Create a FollowerBot that will follow a black line until the end of that line.

    The robot's starting position will be just short of the start point of the line.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    while robot.get_right_line_sensors()[2] == 1024:
        robot.set_wheels_speed(10)
        robot.sleep(0.1)
        if robot.get_left_line_sensors()[2] == 0:
            while robot.get_left_line_sensors()[2] == 0:
                robot.set_wheels_speed(10)
                robot.sleep(0.1)
                if robot.get_left_line_sensors()[2] > 512:
                    robot.set_right_wheel_speed(90)
                    robot.sleep(0.1)
                elif robot.get_right_line_sensors()[2] > 512:
                    robot.set_left_wheel_speed(90)
    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """


if __name__ == '__main__':
    # print(test_run(FollowerBot()))
    # print(drive_to_line(FollowerBot()))
    print(follow_the_line(FollowerBot()))
