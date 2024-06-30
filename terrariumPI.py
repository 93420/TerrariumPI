# -*- coding: utf-8 -*-
__version__ = "4.10.0"

from gevent import monkey

monkey.patch_all()

import sys

try:
    sys.modules["bluepy"] = __import__("bluepy3")
except Exception:
    # Import should only be working on a Bookworm OS
    pass

import gettext

gettext.install("terrariumpi", "locales/")

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

from terrariumEngine import terrariumEngine

if __name__ == "__main__":
    terrariumEngine = terrariumEngine(__version__)
    # This keeps running until CTRL-C is entered or given
    terrariumEngine.stop()
