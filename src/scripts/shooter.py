from time import sleep
import sys
import RPi.GPIO as GPIO
import traceback

DUTY_CYCLE_MEDIUM_SPEED = 85
controlPin1 = 24
controlPin2 = 23
controlPin3 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(controlPin1, GPIO.OUT)
GPIO.setup(controlPin2, GPIO.OUT)
GPIO.setup(controlPin3, GPIO.OUT)
GPIO.output(controlPin1, GPIO.LOW)
GPIO.output(controlPin2, GPIO.LOW)
pwm = GPIO.PWM(controlPin3, 100)

pwm.start(DUTY_CYCLE_MEDIUM_SPEED)
GPIO.output(controlPin1, GPIO.LOW)
GPIO.output(controlPin2, GPIO.HIGH)

print('\nShooter started!')
print('The default direction and speed of the motor are, respectively, b (backward) and m (medium).')
print('The available commands are:\n')
print('s (stop)\nl (low)\nm (medium)\nh (high)\nf (forward)\nb (backward)\n')
sys.stdout.flush()

try:
    while True:
        x = raw_input()

        if x == 's':
            print('stop')
            sys.stdout.flush()
            GPIO.output(controlPin1, GPIO.LOW)
            GPIO.output(controlPin2, GPIO.LOW)
            break
        elif x == 'l':
            print('low')
            pwm.ChangeDutyCycle(70)
        elif x == 'm':
            print('medium')
            pwm.ChangeDutyCycle(DUTY_CYCLE_MEDIUM_SPEED)
        elif x == 'h':
            print('high')
            pwm.ChangeDutyCycle(100)
        elif x == 'f':
            print('forward')
            GPIO.output(controlPin1,GPIO.HIGH)
            GPIO.output(controlPin2,GPIO.LOW)
        elif x == 'b':
            print('backward')
            GPIO.output(controlPin1,GPIO.LOW)
            GPIO.output(controlPin2,GPIO.HIGH)
        else:
            print('unrecognized input')

        sys.stdout.flush()
except Exception:
    print('An error occurred:')
    traceback.print_exc()
    sys.stdout.flush()
finally:
    print('clean up') 
    sys.stdout.flush()
    GPIO.cleanup()