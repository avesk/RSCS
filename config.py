import argparse

# Create the parser
parser = argparse.ArgumentParser(
    description='RSCS Config'
)

# Add the arguments
parser.add_argument(
    '-m',
    '--mock_serial',
    type=bool,
    help='mock pyserial library',
    default=False
)

parser.add_argument(
    '-s',
    '--serial_dev',
    type=str,
    help='Serial Device Name',
    default='/dev/ttyUSB0'
)

# Execute the parse_args() method
args = parser.parse_args()
