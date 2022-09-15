import mido
import serial
arduino = serial.Serial('COM36', 115200)
while True:
    arduino.write(b'5')