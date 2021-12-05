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
    while robot.get_right_line_sensors()[0] == 1024:
        robot.set_wheels_speed(100)
        robot.sleep(0.1)
    while sum(robot.get_line_sensors()) != 6144:
        print(robot.get_line_sensors())
        if robot.get_left_line_sensor() + robot.get_right_line_sensor() + robot.get_second_line_sensor_from_right() + robot.get_second_line_sensor_from_left() == 0:
            robot.set_wheels_speed(100)
            robot.sleep(0.1)
        elif robot.get_third_line_sensor_from_left() == 1024 and robot.get_third_line_sensor_from_right() == 0:
            robot.set_left_wheel_speed(55)
            robot.set_right_wheel_speed(65)
            robot.sleep(0.1)

        elif robot.get_third_line_sensor_from_right() == 1024 and robot.get_third_line_sensor_from_left() == 0:
            robot.set_right_wheel_speed(55)
            robot.set_left_wheel_speed(65)
            robot.sleep(0.1)

        elif robot.get_third_line_sensor_from_left() == 1024 and robot.get_second_line_sensor_from_left() == 1024:
            robot.set_left_wheel_speed(40)
            robot.set_right_wheel_speed(75)
            robot.sleep(0.1)

        elif robot.get_third_line_sensor_from_right() == 1024 and robot.get_second_line_sensor_from_right() == 1024:
            robot.set_right_wheel_speed(40)
            robot.set_left_wheel_speed(65)
            robot.sleep(0.1)
        else:
            robot.set_wheels_speed(40)
            robot.sleep(0.1)


    robot.done()
    '''
    while sum(robot.get_line_sensors()) != 6144:
        if sum(robot.get_left_line_sensors()) >= 1024 and 0 <= sum(robot.get_right_line_sensors()) < 1024:
            robot.set_right_wheel_speed(50)
            robot.sleep(0.1)
        elif sum(robot.get_right_line_sensors()) > 1500 and sum(robot.get_left_line_sensors()) != 0:
            robot.set_left_wheel_speed(85)
            robot.sleep(0.1)
        elif robot.get_right_line_sensors()[2] == 0 and robot.get_left_line_sensors()[2] == 0:
            robot.set_wheels_speed(50)
            robot.sleep(0.2)
        else:
            robot.set_wheels_speed(20)
            robot.sleep(0.1)
    '''


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """


if __name__ == '__main__':
    # print(test_run(FollowerBot()))
    # print(drive_to_line(FollowerBot()))
    print(follow_the_line(FollowerBot()))
