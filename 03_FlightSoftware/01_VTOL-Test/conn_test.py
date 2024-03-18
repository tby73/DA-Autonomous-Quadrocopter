from pymavlink import mavutil
import dronekit as dk

FC_SERIAL_PORT = "/dev/ttyACM0"

def ConnectionTest(fc_port):
    aq = mavutil.mavlink_connection(fc_port)
    aq.wait_heartbeat()
    return aq.target_system, aq.target_component

def ModeTest(fc_port):
    vehicle = dk.connect(fc_port, baud=921600, wait_ready=False)
    return vehicle.mode.name

def main():
    aq_mode = ModeTest(FC_SERIAL_PORT)
    #ts, tc = ConnectionTest(FC_SERIAL_PORT)

    print(f"DK AP MODE: {aq_mode}")
    print(f"[AQ_STAT] HEARTBEAT_RECV")
    #print(f"TARGET_SYS: {ts}")
    #print(f"TARGET_COMP: {tc}")



if __name__ == "__main__":
    main()
