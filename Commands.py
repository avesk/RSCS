import fake_serial as serial

class Commands():
    '''Class for sending WASD, Power, and Pump Toggle Byte commands
     over serial.

     Bytes are formated: 
        (P)umpToggle (C)utPower (B)reakToggle (P)ower (F)orward (B)ack (L)eft (R)ight
     '''

    default_serial_location = '/dev/ttyUSB0'

    TOGGLE_PUMP = b'\x08\x00' # 0100 0000 
    CUT_POWER = b'\x04\x00'  # 0100 0000 
    BREAK_TOGGLE = b'\x02\x00' # 0010 0000 
    POWER = b'\x01\x00' # 0001 0000 
    FORWARD = b'\x00\x08' # 0000 1000
    BACKWARD = b'\x00\x04' # 0000 0100
    LEFT = b'\x00\x02' # 0000 0010
    RIGHT = b'\x00\x01' # 0000 0001

    def __init__(self, serial_location=default_serial_location):
        self.open(serial_location)

    def open(self, serial_location=default_serial_location):
        self.ser = serial.Serial(serial_location)

    def close(self):
        self.ser.close()

    def toggle_pump(self):
        print("TOGGLE_PUMP")
        self.ser.write(self.TOGGLE_PUMP)

    def cut_power(self):
        print("CUT_POWER")
        self.ser.write(self.CUT_POWER)

    def power(self):
        print("POWER")
        self.ser.write(self.POWER)

    def break_toggle(self):
        print("BREAK_TOGGLE")
        self.ser.write(self.BREAK_TOGGLE)

    def forward(self):
        print("FORWARD")
        self.ser.write(self.FORWARD)

    def backward(self):
        print("BACKWARD")
        self.ser.write(self.BACKWARD)

    def left(self):
        print("LEFT")
        self.ser.write(self.LEFT)

    def right(self):
        print("LEFT")
        self.ser.write(self.RIGHT)