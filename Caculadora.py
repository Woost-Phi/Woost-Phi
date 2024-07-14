import Caculadora
import math


class Calculador (object):
        def calculation(self, calc):
            return self.__calculation_validation(calc=calc)
        def calculation_validation (self, calc):
            try: 
               result = eval(calc)
               return self. __format_result (result=result)
            except (NameError, ZeroDivisionError, SystemError, ValueError):
                return 'Erro'         
def __format_result(self, result):
    result = str(result)
if len(result) > 15:
    result = '{:5.5e}' .format(float(result))

return result

