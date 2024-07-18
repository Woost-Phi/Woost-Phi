n1 = int(input('Number one?' )) #SOmente números inteiros
n2 = int(input('Number tWO? ')) #Somente números inteiros
from deep_translator import ChatGptTranslator
tradudor = ChatGptTranslator
SOMA = n1 + n2 #Soma de dois numeros 
SUBT = n1 - n2 #Subtação de dois numeros
MULT = n1*n2  #Multiplicação de Dois numeros
DIV = round(n1/n2)  #Div with float number rounded
DIV2 = n1/n2 #Division with float of two numers decimals
#DIVINT = n1//n2 #Div with Whole number 
MOD = n1%n2 #Division with rest
MOD2 = float(n1%n2) #Division two
POT = n1**n2 #Power between two number, where first number is it elavated to second number

(print("The sum of numbers {} and {} is of: {} ".format(n1, n2, SOMA)))
print("Then subtraction of numbers {} and {} is of: {} " .format (n1, n2, SUBT))
print("The mutiplication beteween {} and {} is of: {}" .format(n1,n2, MULT))
print ("The division of {} by {} it has value: {}" .format(n1, n2, DIV))
print ("The division of {} by {} it has value: {: .2f}" .format(n1, n2, DIV2))
#print("That same one division of {} by {} it has whole value: {}" ,format(n1, n2, DIVINT))
print("The division of {} with {} it was rest value: {}" .format(n1, n2, MOD))
print("The division of {} was {} it was reset value float: {}" .format(n1,n2, MOD2))
print("The {} elevated a {} is {} " .format(n1,n2, POT))
