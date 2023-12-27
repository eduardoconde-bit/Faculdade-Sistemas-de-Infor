import socket

try:
    site = str(input('Digite o nome do site: '))
    ip = socket.gethostbyname(site)
except socket.gaierror:
    print('Está fora do ar ou Não existe')
else:
    print(f'Consegui acessar o site {site}')
