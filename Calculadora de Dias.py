D1= int(input('Digite o dia do MÊS que iniciará a contagem: '))
if D1>31:
        print('Data incorreta:')
        
else:
            D1<=31
    
D2= int(input('Digite o Mês: '))

if D2>12:
        print('Mês invalido)')
        
else:
            D1<=12
D3= int(input('Digite o ano de inicio: '))
D4= int(input('Digite o dia que finaliza a contagem: '))
if D4>31:
        print('Data incorreta)')
        
else:
            D4<=31
    
D5= int(input('Digite o mês que finaliza a contagem: '))
if D5>12:
        print('Mês invalido)')
        
else:
            D5<=12
D6= int(input('Digite o ano que finaliza a contagem: '))

if D1 == 1 or 3 and 5 or 7 and 8 or 9:   
        DF1 = 31 - D1 
else: DF1 = 2 or 4 and 6 or 10 and 11

if D1== 2:
        DF1= 28 - D1
else: D1 != 2
if D1 == 4 or 6 and 10 or 11:   
        DF1 = 31 - D1 
else: DF1 != 4 or 6 and 10 or 11
      
if D4 == 1 or 3 and 5 or 7 and 8 or 9:   
        DF1 = 31 - D1 
else: DF2 = 2 or 4 and 6 or 10 and 11

if D4== 2:
        DF2= 28 - D1
else: D1 != 2
if D1 == 4 or 6 and 10 or 11:   
        DF2 = 31 - D1 
else: DF2 != 4 or 6 and 10 or 11
      

DF3= DF1 + DF2 
#Meses = {1 : 'janeiro', 2 : 'Fevereiro', 3: 'Março', 4: 'Abril', 5} (Não consigui integrar isso aqui :/)
DFA = D6 - D3
DFA2= DFA * 365 + DF3

print (" Do dia {} do {} do ano {} ao dia {} do {} ao ano {} tem {} dias".format(D1, D2, D3, D4, D5, D6, DFA2))


