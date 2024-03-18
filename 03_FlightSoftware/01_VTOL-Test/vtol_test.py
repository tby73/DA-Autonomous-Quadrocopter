from pymavlink import mavutil
import time

# Define serial port and baud rate
SERIAL_FC_PORT = "/dev/ttyACM0"
SERIAL_BAUDRATE = 115200

def GetAltitude(master):
    master.mav.request_data_stream_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_DATA_STREAM_EXTRA1, 10, 1)
    
    msg = master.recv_match(type='SCALED_PRESSURE', blocking=True)
    altitude = msg.press_abs / 1000.0  # Altitude in meters

    return altitude

def VTOL(serial_port, altitude):
    # Connect to the vehicle
    aq = mavutil.mavlink_connection(serial_port, baud=SERIAL_BAUDRATE)

    # Arm the vehicle
    print("[AQ_STAT]: ARMING DRONE")
    aq.mav.command_long_send(aq.target_system, aq.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)

    resp = aq.recv_match(type="COMMAND_ACK", blocking=True)
    print(f"[AQ_STAT]: DRONE ARMED ({resp})")

    # Send takeoff command
    aq.mav.command_long_send(aq.target_system, aq.target_component, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, altitude)
    resp = aq.recv_match(type="COMMAND_ACK", blocking=True)

    print(f"[AQ_STAT]: TAKE OFF RECEIVED (CMD: {resp})")
    print(f"[AQ_STAT]: DRONE TAKING OFF TO TARGET ALTITUDE [{altitude}] m")

    # Monitor altitude until the vehicle reaches 90% of the target altitude
    while True:
        altitude = GetAltitude(aq)
        print(f"[AQ_STAT] LIVE ALTITUDE: [{altitude}] m")

        if altitude >= altitude * 0.9:
            print("[AQ_STAT] REACHED ALTITUDE, PROCEED TO LAND IN 2 SECONDS")
            break
        time.sleep(2)

    # Send land command
    aq.mav.command_long_send(aq.target_system, aq.target_component, mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, 0, 0)

def main():
    print("*** AutoQuad VTOL TEST ***")
    print("OPTIONS:")
    print("[v] VTOL (VERTICAL TAKE OFF AND LANDING)")
    command = input("AQ/VTOL_TEST>")

    if command.lower() == "v":
        altitude = int(input("  ALT[m]: "))
        VTOL(SERIAL_FC_PORT, altitude=altitude)

if __name__ == "__main__":
    main()

