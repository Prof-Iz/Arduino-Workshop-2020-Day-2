import serial 
# import the required python library (PIP install the dependecies )
# pip install pyserial

device = serial.Serial(port='COMX',baudrate=9600,timeout=1)
# port is the serial port your device is communicating with may differ over connections like bluetooth
# just to make sure check which comport is being used using the device manager (Windows)
# baudrate stands for the communication frequency, usually the terminal is set at 9600
# timeout referes to the timeout period for the communication, which in this case is 1 sec

# ________________________________________________________________________________________________________

# After initialising the device (can be any name you want since it's an object name) you can do the following

device.write('String'.encode('utf-8')) #any string sent to the arduino must be encoded into bytes. utf-8 is
# an encoding format
# in the example above the word "String" will be sent over Serial communication to any device connected to
# the device port.

# similarly you may read the serial coming in from said device with the following method 
device.read_until('\n')
# similar to the Arduino code, the python will read the signal coming in until it detects that the line is 

# _________________________________________________________________________________________________________
import speech_recognition as sr

voice = sr.Recognizer()

voice.recognize_google(audio, language=)
# now that the basics have been done, lets create a loop shall we


from time import sleep # going to use this later to slow down the program and give your computer a break

while True: # just saying that this will run infinitely
    try:
        
        distance = device.readline('\n').decode("utf-8") # read from the serial communication

        if int(distance) < 1: # need to use int because value you are getting from serial by default is String
            print("Oh No system is too close")
        elif int(distance) > 1:
            print("No danger")
        else:
            print("sweet spot")

        device.flush() # clear the serial so that a new value can be put there. Either put it here or in the arduino
    
    except:
        print("Uh something happened, thats not supposed to") 
    
    sleep(0.5) # program interrupted for 0.5 seconds before it begins again