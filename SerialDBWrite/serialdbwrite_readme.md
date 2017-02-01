##Purpose
Write data from a serial connection to a DB.

usage: serialdbwrite.py [-h] interface baud

positional arguments:
  interface, name of the serial interface
  baud, baud rate for communication

optional arguments:
  -h, --help  show this help message and exit

###Instructions

1.  Connect arduino to USB and load the sketch provided 
2.  Make a note of the bus he Ardino is connected to e.g. /dev/cu.usbmodem1421
3.  Copy the sample test db and the python script to the folder.
4.  Execute the python script
    *   e.g ./serialdbwrite.py /dev/cu.usbmodem1421 9600
5.	Terminate the python script using SIGINT (ctrl c) when done. The script will close gracefully.

**Note**: If you change the baud rate you must also update the sample arduino sketch to match or you'll get gibberish.

