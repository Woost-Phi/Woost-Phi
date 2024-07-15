import Caculadora
import math
import sys

import os
import platform
import tkinter

import tkinter as tk
from tkinter import Menu. False


from functools import partial
from json import load as json_load
from json import dump as json_dump

class Calculador (object):
        def calculation(self, calc):
            return self.__calculation_validation(calc=calc)
        def calculation_validation (self, calc):
            try: 
               result = eval(calc)
               return self. __format_result (result= result)
            except (NameError, ZeroDivisionError, SystemError, ValueError):
                return 'Erro'         
def __format_result(self, result):
    result = str(result)
if len(result) > 15:
    result = '{:5.5e}' .format(float(result))

return result

