import math

from interbotix_xs_modules.xs_robot.locobot import InterbotixLocobotXS

"""
This script manipulates the arm, pan/tilts the camera, and moves the base.

To get started, open a terminal and run the command:

    ros2 launch interbotix_xslocobot_control xslocobot_control.launch.py robot_model:=locobot_wx200
        use_nav:=false rtabmap_args:=-d

Then change to this directory and run the command:

    python3 combo_control.py

...or run the command:

    ros2 run interbotix_xslocobot_control combo_control.py
"""


def main():
    locobot = InterbotixLocobotXS(
        robot_model='locobot_wx200',
        arm_model='mobile_wx200',
        use_base=True,
        use_nav=True,
        robot_name='locobot'
    )

    locobot.arm.set_ee_pose_components(x=0.3, z=0.2)
    # locobot.arm.set_single_joint_position('waist', math.pi/4.0)
    # locobot.gripper.release()
    # locobot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.25)
    # locobot.gripper.grasp()
    # locobot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.25)
    # locobot.arm.set_single_joint_position('waist', -math.pi/4.0)
    # locobot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    # locobot.arm.set_ee_cartesian_trajectory(pitch=-1.5)
    # locobot.arm.set_single_joint_position('waist', math.pi/4.0)
    # locobot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.25)
    # locobot.gripper.release()
    # locobot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.25)
    # locobot.arm.go_to_home_pose()
    # locobot.arm.go_to_sleep_pose()

    # # move to [1.0, 1.0, pi]
    # locobot.base.command_pose_xyyaw(
    #     x=1.0,
    #     y=1.0,
    #     yaw=math.pi,
    #     blocking=True
    # )
    # # move to [0.0, 0.0, 0.0]
    # locobot.base.command_pose_xyyaw(
    #     x=0.0,
    #     y=0.0,
    #     yaw=0.0,
    #     blocking=True
    # )

    locobot.arm.go_to_home_pose()
    locobot.arm.set_ee_cartesian_trajectory(z=-0.2)
    locobot.arm.set_ee_cartesian_trajectory(x=-0.2)
    locobot.arm.set_ee_cartesian_trajectory(z=0.2)
    locobot.arm.set_ee_cartesian_trajectory(x=0.2)
    locobot.arm.go_to_sleep_pose()

    # locobot.camera.pan(1)
    # locobot.camera.tilt(1)
    # locobot.camera.pan_tilt_move(-1, -1)
    # locobot.camera.pan_tilt_go_home()

    # locobot.shutdown()


if __name__ == '__main__':
    main()
