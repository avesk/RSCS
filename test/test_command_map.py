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

    def cmd(self, key):
        return command_map[key]

    def test_north(self):
        getattr(self.Cmds, self.cmd('w'))()
        self.Cmds.ser.write.assert_called_with(b'\x01')
    
    def test_west(self):
        getattr(self.Cmds, self.cmd('a'))()
        self.Cmds.ser.write.assert_called_with(b'\x02')
    
    def test_south(self):
        getattr(self.Cmds, self.cmd('s'))()
        self.Cmds.ser.write.assert_called_with(b'\x04')

    def test_east(self):
        getattr(self.Cmds, self.cmd('d'))()
        self.Cmds.ser.write.assert_called_with(b'\x08')

    def test_north_west(self):
        getattr(self.Cmds, self.cmd('q'))()
        self.Cmds.ser.write.assert_called_with(b'\x03')

    def test_north_east(self):
        getattr(self.Cmds, self.cmd('e'))()
        self.Cmds.ser.write.assert_called_with(b'\x09')

    def test_south_west(self):
        getattr(self.Cmds, self.cmd('z'))()
        self.Cmds.ser.write.assert_called_with(b'\x06')
    
    def test_south_east(self):
        getattr(self.Cmds, self.cmd('c'))()
        self.Cmds.ser.write.assert_called_with(b'\x0C')
    
    def test_fast_mode(self):
        getattr(self.Cmds, self.cmd(' '))()
        self.Cmds.ser.write.assert_called_with(b'\x10')

    def test_start(self):
        getattr(self.Cmds, self.cmd('m'))()
        self.Cmds.ser.write.assert_called_with(b'\x20')
    
    def test_toggle_pump(self):
        getattr(self.Cmds, self.cmd('p'))()
        self.Cmds.ser.write.assert_called_with(b'\x40')

    def test_e_stop(self):
        getattr(self.Cmds, self.cmd('Backspace'))()
        self.Cmds.ser.write.assert_called_with(b'\x80')
    
  