import RPi.GPIO as GPIO
import can
import time
import os
from threading import Thread

import numpy as np

rolls = np.arange(0.0, 91.0, 1.0)

def get_motor_position(roll)
