import serial
from time import sleep
sleep(3) #initialise sleeping time to get arduino settled in
# import speech_recognition as sr

arduino = serial.Serial(port='COM14',baudrate=9600,timeout=1) #Always the outgoing Com port with Protocol for data Transfer
r = sr.Recognizer()
while (True):
    with sr.Microphone() as source:
        print("Enter a command")
        audio = r.listen(source,phrase_time_limit= 3.0)
        print("time Ran out")

    try:
        command = r.recognize_google(audio)
        print(f"Command: {command}")
        if "on" in command.lower():
            arduino.write('y'.encode('utf-8'))
        elif "off" in command.lower():
            arduino.write('n'.encode('utf-8'))
    except Exception:
        print ("Unknown error occured")
        pass
while (1):
    command = input("Enter Command: ")
    try:
        arduino.write(command.encode("ascii"))
    except Exception as e:
        print(f'The following Command was not sent due to the following error\n {e}')     
    

    

    


