import time as t
import dronekit as dk

from dronekit import VehicleMode

TCP_FC_TARGET = "tcp:127.0.0.1:5760"

def PrintOptions():
    print("*** AutoQuad VTOL TEST ***")
    print("OPTIONS:")
    print("[t] TAKE-OFF")
    print("     <alt> ALTITUDE")
    print("[v] VTOL (VERTICAL TAKE OFF AND LANDING)")
    print("     <alt> ALTITUDE")
    print("[l] LAND")

def VTOL(tcp_addr, altitude):
    vehicle = dk.connect(tcp_addr, wait_ready=True)
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("[AQ_STAT] DRONE ARMING")
        t.sleep(1)
    
    print(f"[AQ_STAT] DRONE TAKING OFF TO TARGET ALTITUDE [{altitude}] m")
    vehicle.simple_takeoff(altitude)

    while True:
        print(f"[AQ_STAT] LIVE ALTITUDE: [{vehicle.location.global_relative_frame.alt}] m")

        if vehicle.location.global_relative_frame.alt >= altitude * 0.9:
            print("[AQ_STAT] REACHED ALTITUDE, PROCEED TO LAND IN 2 SECONDS")
            break
        t.sleep(2)

    print("[AQ_STAT] LANDING...")
    vehicle.mode = VehicleMode("LAND")
    vehicle.close()

def main():
    PrintOptions()
    command = input("AQ/VTOL_TEST>")

    if command == "v" or command == "V":
        altitude = int(input("  ALT[m]: "))
        VTOL(TCP_FC_TARGET, altitude=altitude)


if __name__ == "__main__":
    main()

        

