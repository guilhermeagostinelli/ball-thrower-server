import threading
import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

controlPins = [13,12,15,11]

for pin in controlPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

# Half stepping mode sequence.
seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

print('\nFeeder started!')
print('The default speed of the motor is m (medium).\n')
print('The available commands are:\n')
print('s (stop)\nl (low)\nm (medium)\nh (high)\n')
sys.stdout.flush()

SLEEP_TIME_MEDIUM_SPEED = 0.0075
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
        sleepTime = 0.009
    elif x == 'm':
        print('medium')
        sleepTime = SLEEP_TIME_MEDIUM_SPEED
    elif x == 'h':
        print('high')
        sleepTime = 0.006
    else:
        print('unrecognized input')

    sys.stdout.flush()

    receivedNewKey = True

try:
    while True:
        print 'motorOn: {}'.format(motorOn)
        print 'sleepTime: {}'.format(sleepTime)
        sys.stdout.flush()

        if not motorOn:
            GPIO.cleanup()
            break

        if receivedNewKey:
            receivedNewKey = False
            listener = threading.Thread(target=keyboardListener)
            listener.daemon = True # Forces the thread to be stopped in case the main thread is killed.
            listener.start()
            
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(controlPins[pin], seq[halfstep][pin])
            time.sleep(sleepTime)
except KeyboardInterrupt:
    print('CTRL + C pressed, stopping...')
    sys.stdout.flush()
    GPIO.cleanup()