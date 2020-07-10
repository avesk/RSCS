
import fake_serial 
import serial 

class Commands():
    '''Class for sending WASD, Power, and Pump Toggle Byte commands
     over serial.

     Bytes are formated: 
        (P)umpToggle (C)utPower (B)reakToggle (P)ower (F)orward (B)ack (L)eft (R)ight
     '''

    default_serial_dev = '/dev/serial0'

    NORTH = b'\x01' # 00000001
    WEST = b'\x02' # 00000010
    SOUTH = b'\x04' # 00000100
    EAST = b'\x08' # 00001000
    NORTH_WEST = b'\x03' # 00000011
    NORTH_EAST = b'\x09' # 00001001
    SOUTH_WEST = b'\x06' # 00000110
    SOUTH_EAST = b'\x0C' # 00001100
    FAST_MODE = b'\x10' # 00010000
    START = b'\x20' # 00100000
    TOGGLE_PUMP = b'\x40' # 01000000
    E_STOP = b'\x80' # 10000000

    def __init__(self, serial_dev=default_serial_dev):
        try:
            ser = serial
            self.ser = ser.Serial(serial_dev)
        except:
            print("FAKE SERIAL!!")
            ser = fake_serial
            self.ser = ser.Serial(serial_dev)

    def close(self):
        self.ser.close()

    def start(self):
        print("START")
        self.ser.write(self.START)

    def toggle_pump(self):
        print("TOGGLE_PUMP")
        self.ser.write(self.TOGGLE_PUMP)

    def e_stop(self):
        print("E_STOP")
        self.ser.write(self.E_STOP)

    def break_toggle(self):
        print("BREAK_TOGGLE")
        self.ser.write(self.BREAK_TOGGLE)

    def fast_mode(self):
        print("FAST_mode")
        self.ser.write(self.FAST_MODE)

    def north(self):
        print("NORTH")
        self.ser.write(self.NORTH)

    def south(self):
        print("SOUTH")
        self.ser.write(self.SOUTH)

    def west(self):
        print("WEST")
        self.ser.write(self.WEST)

    def east(self):
        print("EAST")
        self.ser.write(self.EAST)
    
    def north_west(self):
        print("NORTH_WEST")
        self.ser.write(self.NORTH_WEST)
    
    def north_east(self):
        print("NORTH_EAST")
        self.ser.write(self.NORTH_EAST)
    
    def south_west(self):
        print("SOUTH_WEST")
        self.ser.write(self.SOUTH_WEST)
    
    def south_east(self):
        print("SOUTH_EAST")
        self.ser.write(self.SOUTH_EAST)