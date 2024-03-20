Alt = float(input('Digite sua Altura '))

sex = input('Digite seu sexo, sendo H [Homem] ou M [Mulher]')

if (sex == 'H' or 'h' ):

    peso_id=(72.7*Alt)-58

    print('\n O peso ideal é de: ', peso_id)

else:
    peso_id=(62.1*Alt)-44.7

    print('\n O peso ideal é de: ', peso_id)