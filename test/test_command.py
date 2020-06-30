import unittest
from unittest.mock import MagicMock

from Commands import Commands
from command_map import command_map

class TestCommands(unittest.TestCase):
    def setUp(self):
        self.Cmds = Commands()
        self.Cmds.ser.write = MagicMock()
            
    def tearDown(self):
        self.Cmds = None

    # COMMAND CALLS
    def test_map_north(self):
        self.Cmds.north()
        self.Cmds.ser.write.assert_called_with(b'\x01')
    
    def test_west(self):
        self.Cmds.west()
        self.Cmds.ser.write.assert_called_with(b'\x02')
    
    def test_south(self):
        self.Cmds.south()
        self.Cmds.ser.write.assert_called_with(b'\x04')

    def test_east(self):
        self.Cmds.east()
        self.Cmds.ser.write.assert_called_with(b'\x08')

    def test_north_west(self):
        self.Cmds.north_west()
        self.Cmds.ser.write.assert_called_with(b'\x03')

    def test_north_east(self):
        self.Cmds.north_east()
        self.Cmds.ser.write.assert_called_with(b'\x09')

    def test_south_west(self):
        self.Cmds.south_west()
        self.Cmds.ser.write.assert_called_with(b'\x06')
    
    def test_south_east(self):
        self.Cmds.south_east()
        self.Cmds.ser.write.assert_called_with(b'\x0C')
    
    def test_fast_mode(self):
        self.Cmds.fast_mode()
        self.Cmds.ser.write.assert_called_with(b'\x10')

    def test_start(self):
        self.Cmds.start()
        self.Cmds.ser.write.assert_called_with(b'\x20')
    
    def test_toggle_pump(self):
        self.Cmds.toggle_pump()
        self.Cmds.ser.write.assert_called_with(b'\x40')

    def test_e_stop(self):
        self.Cmds.e_stop()
        self.Cmds.ser.write.assert_called_with(b'\x80')
    
   