import time as t

from pymavlink import mavutil

# pixhawk serial port 
FC_SERIAL_PORT = "/dev/ttyACM0"

def main():

    # Set the target system and component IDs
    target_system = 1  # Change this to the appropriate target system ID
    target_component = 1  # Change this to the appropriate target component ID

    # Create a MAVLink connection
    master = mavutil.mavlink_connection(FC_SERIAL_PORT)  # Change the connection string as needed

    # Wait for the connection to be established
    master.wait_heartbeat()

    motor_count = 4  # Number of motors
    motor_order = [0, 1, 2, 3]  # Order of motor testing (0-based index)
    motor_throttle = 0.5  # Throttle level for the test (between 0.0 and 1.0)
    motor_time = 25  # Duration of each motor test in seconds

    # Send the MAV_CMD_DO_MOTOR_TEST command
    master.mav.command_long_send(
        target_system,                            # target_system
        target_component,                        # target_component
        mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST,   # command
        0,                                       # confirmation
        motor_count,                             # param1: Number of motors to test
        motor_throttle,                          # param2: Throttle level
        motor_time,                              # param3: Duration of each test (in seconds)
        0,                                       # param4: Reserved (set to 0)
        *motor_order,                            # param5: Order of motor testing
        0, 0, 0                                 # param6, param7: Reserved (set to 0)
    )

    print("Motor test command sent.")



if __name__ == "__main__":
    main()
