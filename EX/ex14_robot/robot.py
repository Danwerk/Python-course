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
    while robot.get_right_line_sensors()[0] == 1024 and robot.get_left_line_sensors()[2] == 1024:
        robot.set_wheels_speed(100)
        robot.sleep(0.1)

    while sum(robot.get_line_sensors()) != 6144:
        print(robot.get_line_sensors())

        if robot.get_third_line_sensor_from_right() == 1024 and robot.get_third_line_sensor_from_left() == 1024:
            robot.set_wheels_speed(100)
            robot.sleep(0.01)

        if robot.get_third_line_sensor_from_left() == 1024 and robot.get_third_line_sensor_from_right() == 0:
            robot.set_left_wheel_speed(-10)
            robot.set_right_wheel_speed(15)
            robot.sleep(0.01)

        elif robot.get_third_line_sensor_from_right() == 1024 and robot.get_third_line_sensor_from_left() == 0:
            robot.set_left_wheel_speed(20)
            robot.set_right_wheel_speed(-10)
            robot.sleep(0.001)

        else:
            robot.set_wheels_speed(45)
            robot.sleep(0.01)
            print(robot.get_line_sensors())
    robot.done()


def the_true_follower(robot: FollowerBot):
    """
    Create a FollowerBot that will follow the black line on the track and make it ignore all possible distractions.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    while robot.get_right_line_sensors()[0] == 1024 and robot.get_left_line_sensors()[2] == 1024:
        robot.set_wheels_speed(100)
        robot.sleep(0.001)
        print(robot.get_position())
    while True:
        if robot.get_position() == (251, 301):
            break
        else:
            if sum(robot.get_line_sensors()) == 6144:
                robot.set_wheels_speed(100)
                robot.sleep(0.001)

            elif sum(robot.get_line_sensors()) == 3852:
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(-100)
                robot.sleep(0.3)

            elif robot.get_third_line_sensor_from_right() == 1024 and robot.get_third_line_sensor_from_left() == 1024:
                robot.set_wheels_speed(100)
                robot.sleep(0.01)

            elif robot.get_third_line_sensor_from_left() == 1024 and robot.get_third_line_sensor_from_right() == 0:
                robot.set_left_wheel_speed(-78)
                robot.set_right_wheel_speed(100)
                robot.sleep(0.001)

            elif robot.get_third_line_sensor_from_right() == 1024 and robot.get_third_line_sensor_from_left() == 0:
                robot.set_left_wheel_speed(100)
                robot.set_right_wheel_speed(-78)
                robot.sleep(0.001)

            else:
                robot.set_wheels_speed(100)
                robot.sleep(0.02)
                #print(robot.get_line_sensors())
                print(robot.get_position())
    robot.done()


'''

    robot.done()
''' \
'''
    while robot.get_right_line_sensors()[0] == 1024 and robot.get_left_line_sensors()[2] == 1024:
        robot.set_wheels_speed(100)
        robot.sleep(0.1)
    i = 0
    while i != 12:
        if sum(robot.get_line_sensors()) == 6144:
            i += 1
            while sum(robot.get_line_sensors()) != 0:
                robot.set_wheels_speed(100)
                robot.sleep(0.01)
                print(robot.get_line_sensors())

        if robot.get_third_line_sensor_from_right() == 1024 and robot.get_third_line_sensor_from_left() == 1024:
            robot.set_wheels_speed(100)
            robot.sleep(0.01)
            print(robot.get_line_sensors())

        if robot.get_third_line_sensor_from_left() == 1024 and robot.get_third_line_sensor_from_right() == 0:
            robot.set_left_wheel_speed(-10)
            robot.set_right_wheel_speed(15)
            robot.sleep(0.01)

        elif robot.get_third_line_sensor_from_right() == 1024 and robot.get_third_line_sensor_from_left() == 0:
            robot.set_left_wheel_speed(20)
            robot.set_right_wheel_speed(-10)
            robot.sleep(0.001)
            print(robot.get_line_sensors())

        else:
            robot.set_wheels_speed(55)
            robot.sleep(0.01)
            print(robot.get_line_sensors())
    robot.done()
'''
if __name__ == '__main__':
    # print(test_run(FollowerBot()))
    # print(drive_to_line(FollowerBot()))
    # print(follow_the_line(FollowerBot()))
    print(the_true_follower(FollowerBot()))
