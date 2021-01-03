import threading
import time
import sys
import RPi.GPIO as GPIO
import traceback

GPIO.setmode(GPIO.BOARD)

controlPins = [13,12,15,11]

for pin in controlPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

# Single phase stepping mode sequence.
seq = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

print('\nFeeder started!')
print('The default speed of the motor is m (medium).\n')
print('The available commands are:\n')
print('s (stop)\nl (low)\nm (medium)\nh (high)\n')
sys.stdout.flush()

SLEEP_TIME_MEDIUM_SPEED = 0.015
motorOn = True
sleepTime = SLEEP_TIME_MEDIUM_SPEED
receivedNewKey = True

def keyboardListener():
    global motorOn, sleepTime, receivedNewKey

    x = raw_input()

    if x == 's':
        print('stop')
        motorOn = False
    elif x == 'l':
        print('low')
        sleepTime = 0.02
    elif x == 'm':
        print('medium')
        sleepTime = SLEEP_TIME_MEDIUM_SPEED
    elif x == 'h':
        print('high')
        sleepTime = 0.01
    else:
        print('unrecognized input')

    sys.stdout.flush()

    receivedNewKey = True

try:
    while True:
        sys.stdout.flush()

        if not motorOn:
            break

        if receivedNewKey:
            receivedNewKey = False
            listener = threading.Thread(target=keyboardListener)
            listener.daemon = True # Forces the thread to be stopped in case the main thread is killed.
            listener.start()
            
        for step in range(4):
            for pin in range(4):
                GPIO.output(controlPins[pin], seq[step][pin])
            time.sleep(sleepTime)
except Exception:
    print('An error occurred:')
    traceback.print_exc()
    sys.stdout.flush()
finally:
    print('clean up') 
    sys.stdout.flush()
    GPIO.cleanup()