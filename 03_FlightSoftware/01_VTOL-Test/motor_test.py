import time as t

from pymavlink import mavutil

# pixhawk serial port 
FC_SERIAL_PORT = "/dev/ttyACM0"

def main():
    while True:
        # establish connection
        aq = mavutil.mavlink_connection(FC_SERIAL_PORT)
        aq.wait_heartbeat()

        # return fc connectivity device params
        print("[AQ_STAT] HEARTBEAT_RECV")
        print(f"TARGET SYS: {aq.target_system}")
        print(f"TARGET COMP: {aq.target_component}")

        # send arm-command 
        aq.mav.command_long_send(aq.target_system, aq.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
        resp = aq.recv_match(type="COMMAND_ACK", blocking=True)
        print(resp)

        # send take off command
        aq.mav.command_long_send(aq.target_system, aq.target_component, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 5)
        resp = aq.recv_match(type="COMMAND_ACK", blocking=True)
        print(resp)

        t.sleep(5)


if __name__ == "__main__":
    main()

