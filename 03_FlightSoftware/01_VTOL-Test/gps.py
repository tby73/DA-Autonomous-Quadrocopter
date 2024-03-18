import smbus
import pynmea2
import time

class GPS:
    def __init__(self, bus_number=1, device_address=0x42):
        self.bus = smbus.SMBus(bus_number)
        self.device_address = device_address

    def read_nmea_sentence(self):
        sentence = ""
        try:
            # Read one byte at a time until newline character is encountered
            while True:
                data = self.bus.read_byte(self.device_address)
                if data == 10:  # Newline character
                    break
                sentence += chr(data)
        except Exception as e:
            print(f"Error reading I2C data: {e}")
        return sentence.strip()

    def parse_nmea_sentence(self, sentence):
        try:
            msg = pynmea2.parse(sentence)
            if isinstance(msg, pynmea2.types.talker.GGA):
                latitude = msg.latitude
                longitude = msg.longitude
                altitude = msg.altitude
                return latitude, longitude, altitude
        except pynmea2.ParseError as e:
            print(f"Parse error: {e}")
        return None, None, None

    def get_gps_data(self):
        sentence = self.read_nmea_sentence()
        latitude, longitude, altitude = self.parse_nmea_sentence(sentence)
        return latitude, longitude, altitude

def main():
    gps = GPS()

    try:
        while True:
            latitude, longitude, altitude = gps.get_gps_data()
            if latitude is not None and longitude is not None and altitude is not None:
                print(f"Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude} meters")
            time.sleep(1)  # Adjust the delay as needed
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

