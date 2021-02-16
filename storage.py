#!/usr/bin/env python3

from ev3dev.ev3 import *
import os
from time import sleep

m = LargeMotor('outB')
n = LargeMotor('outC')
ts = TouchSensor()
cl = ColorSensor()

print('''
  
Time to get fucked bitch boy.''')


while not ts.value():
    m.run_forever(speed_sp=-1000)
    n.run_forever(speed_sp=-1000)



#Light sensor testing
cl.mode='COL-COLOR'
'''
colors=('unknown','black','blue','green','yellow','red','white','brown')
while colors[cl.value()] != 'black':
    m.run_forever(speed_sp=-1000)
    n.run_forever(speed_sp=-1000)

m.stop_action="hold"
n.stop_action="hold"
       ''' 


'''
while not ts.value():
    m.run_forever(speed_sp=-1000)
    n.run_forever(speed_sp=1000)
'''
#Sound.speak('Time to get fucked bitch boy.').wait()


'''

while not ts.value():
    m.run_forever(speed_sp=-1000)
    n.run_forever(speed_sp=1000)
'''
'''
# Sounds and speaking and beeps, Megalavania
Sound.speak('Time to get fucked bitch boy.').wait()
Sound.tone([(1174, 100, 100),
(1174, 100, 100),
(2349, 150, 100),
(1760, 150, 100),
(1661, 100, 100),
(1567, 150, 100),
(1396, 150, 100),
(1174, 150, 100),
(1396, 100, 100),
(1567, 100, 100),
(1046, 100, 100),
(1046, 100, 100),
(2349, 100, 100),
(1760, 150, 150),
(1661, 150, 100),
(1567, 150, 100),
(1396, 150, 100),
(1174, 100, 100),
(1396, 100, 100),
(1576, 100, 100),
(1975, 100, 100),
(1975, 100, 100),
(2349, 150, 100),
(1760, 150, 150),
(1661, 150, 100),
(1567, 150, 100),
(1396, 150, 100),
(1174, 100, 100),
(1396, 100, 100),
(1567, 100, 100)
]).wait()
'''

# Sound.speak('Hi Maya, you may die now').wait()

# Move forward tiny bit
#m.run_timed(time_sp=1000, speed_sp=-900)
#n.run_timed(time_sp=1000, speed_sp=-900)
# Spinny around to find source of touch


# Speed for time and amount of speed
#m.run_timed(time_sp=5000, speed_sp=-1000)
#n.run_timed(time_sp=5000, speed_sp=-1000)


#Turns touch sensor on and off, see if it shall turn motor on or not
#while not ts.value():
 #   m.run_forever(speed_sp=-900)
  #  n.run_forever(speed_sp=-900)


  #!/usr/bin/env python3

# NOTE FOR STEPHEN CHECK IF SPIN AND TURNS ARE WHAT THEY ARE

from ev3dev.ev3 import *
import os
from time import sleep

m = LargeMotor('outB')
n = LargeMotor('outC')
tsfront = TouchSensor('in3')
tsback = TouchSensor('in2')
cl = ColorSensor()
btn = Button()

# Function go forward for time and speed

def forward(time,speed):
    m.run_timed(time_sp=time, speed_sp=speed*-1)
    n.run_timed(time_sp=time, speed_sp=speed*-1)

# Function spin left for time and speed

def spin_left(time,speed):
    m.run_timed(time_sp=time, speed_sp=speed*-1)
    n.run_timed(time_sp=time, speed_sp=speed)

# Function spin right for time and speed

def spin_right(time,speed):
    m.run_timed(time_sp=time, speed_sp=speed)
    n.run_timed(time_sp=time, speed_sp=speed*-1)

# Function turn left for time and speed

def turn_left(time,speed):
    m.run_timed(time_sp=time, speed_sp=speed*-1)

# Function turn left for time and speed

def turn_right(time,speed):
    n.run_timed(time_sp=time, speed_sp=speed*-1)

# Function to sense black and travel forward, going backward so don't exit arena

def blackforward(time,speed):
    while colors[cl.value()] != 'white':
        m.run_forever(speed_sp=-1000)
        n.run_forever(speed_sp=-1000)
    m.run_timed(time_sp=time, speed_sp=speed)
    n.run_timed(time_sp=time, speed_sp=speed)

# Function to sense black and turn left, going backward so don't exit arena

def blackleft(time,speed):
    while colors[cl.value()] != 'white':
        n.run_forever(speed_sp=-800)
    m.run_timed(time_sp=time, speed_sp=speed)
    n.run_timed(time_sp=time, speed_sp=speed)

# Function to sense black and turn right, going backward so don't exit arena

def blackright(time,speed):
    while colors[cl.value()] != 'white':
        m.run_forever(speed_sp=-800)
    m.run_timed(time_sp=time, speed_sp=speed)
    n.run_timed(time_sp=time, speed_sp=speed)

# Setting up color sensor

cl.mode='COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')

# When turned on, move forward and spin at first

forward(1000,1000)
spin_left(2000,1000)

#Allowing for code to work forever until it is manually turned off

while not btn.any():
    while not tsfront.value() or not tsback.value():
        spin_right(10000,1000)
        blackforward(10000,1000)
        spin_left(10000,1000)
        blackforward(1000,1000)
    if tsfront.value():
        blackforward(10000,1000)
    elif tsback.value():
        blackforward(10000,-1000)
    spin_left(10000,1000)
    blackleft(10000,1000)
    spin_right(10000,1000)
    blackright(10000,1000)

# For fun add some beeps and speech

#!/usr/bin/env python3

# NOTE FOR STEPHEN CHECK IF SPIN AND TURNS ARE WHAT THEY ARE

from ev3dev.ev3 import *
import os
from time import sleep

m = LargeMotor('outB')
n = LargeMotor('outC')
tsfront = TouchSensor('in3')
tsback = TouchSensor('in2')
cl = ColorSensor()
btn = Button()

# Function go forward for time and speed

def forward(time,speed):
    m.run_timed(time_sp=time, speed_sp=speed*-1)
    n.run_timed(time_sp=time, speed_sp=speed*-1)

# Function spin left for time and speed

def spin_left(time,speed):
    m.run_timed(time_sp=time, speed_sp=speed*-1)
    n.run_timed(time_sp=time, speed_sp=speed)

# Function spin right for time and speed

def spin_right(time,speed):
    m.run_timed(time_sp=time, speed_sp=speed)
    n.run_timed(time_sp=time, speed_sp=speed*-1)

# Function to sense black and travel forward, going backward so don't exit arena

def blackforward():
    while colors[cl.value()] != 'black':
        m.run_forever(speed_sp=-1000)
        n.run_forever(speed_sp=-1000)
    m.stop()
    n.stop()
    m.run_forever(speed_sp=0)
    n.run_forever(speed_sp=0)
    m.run_timed(time_sp=1000, speed_sp=100)
    n.run_timed(time_sp=1000, speed_sp=100)

# Function to sense black and turn left, going backward so don't exit arena

def blackleft(time,speed):
    while colors[cl.value()] != 'black':
        n.run_forever(speed_sp=-100)
    m.stop()
    n.stop()
    m.run_forever(speed_sp=speed)
    n.run_forever(speed_sp=speed)

# Function to sense black and turn right, going backward so don't exit arena

def blackright(time,speed):
    while colors[cl.value()] != 'black':
        m.run_forever(speed_sp=-100)
    m.stop()
    n.stop()
    m.run_forever(speed_sp=speed)
    n.run_forever(speed_sp=speed)

# Setting up color sensor

cl.mode='COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')

# When turned on, move forward and spin at first
while not tsfront.value():
    m.run_forever(speed_sp=100)
    n.run_forever(speed_sp=-100)

#Allowing for code to work forever until it is manually turned off
'''
while not btn.any():
    while not tsfront.value() or not tsback.value():
        spin_right(10000,1000)
        blackforward(10000,1000)
        spin_left(10000,1000)
        blackforward(1000,1000)
    if tsfront.value():
        blackforward(10000,1000)
    elif tsback.value():
        blackforward(10000,-1000)
    spin_left(10000,1000)
    blackleft(10000,1000)
    spin_right(10000,1000)
    blackright(10000,1000)
'''
# For fun add some beeps and speech