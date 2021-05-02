# ！/user/bin/env python
# encoding:utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

#创建一个 pwm 实例，需要两个参数，第一个是 GPIO 引脚号，这里用 2 脚,因为 2 脚与 A Enable 相连。
#第二个是频率(HZ)
pwm = GPIO.PWM(2,100)
# 以输出 90%占空比开始
pwm.start(100)

GPIO.output(2,True)
GPIO.output(3,True)
GPIO.output(4,False)

#  输出 90% 占空比的方波 3 秒，输出 30% 占空比的方波 3秒。如此往复。可以明显看到电机转速的变化。
while True:
	pwm.ChangeDutyCycle(80)
	time.sleep(3)
	pwm.ChangeDutyCycle(20)
	time.sleep(3)
