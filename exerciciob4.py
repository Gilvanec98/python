anocar = int(input('Digite ano do veículo'))
precar = float(input('Digite o valor do veículo'))





if (anocar <= 1990 ):
    tax = precar * 0.01 


else:
    tax = precar * 0.015 

    
print('A taxa é de', tax)