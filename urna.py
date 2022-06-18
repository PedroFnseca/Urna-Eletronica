import os # Biblioteca para limpar o terminal
from time import sleep # Biblioteca para manipular tempo

# Limpa a tela para melhorar a qualidade do terminal
def limpar():
  sleep(tempo)
  os.system('cls') or None

# Menu do mesario
def menuMesario():
  print('╔═══════════════════════════════════════════════╗')
  print('║                                               ║')
  print('║            BEM VINDO A URNA ELEITORAL !       ║')
  print('║                                               ║')
  print('╠═══════════════════════════════════════════════╣')
  print('║                                               ║')
  print('║               ESCOLHA UMA OPCAO !             ║')
  print('║                                               ║')
  print('╠═══════════════════════════════════════════════╣')
  print('║                                               ║')
  print('║ ■ DIGITE 1 PARA LIBERAR NOVO VOTO.            ║')
  print('║ ■ DIGITE 2 PARA ENCERRAR O PROCESSO ELEITORAL.║')
  print('║                                               ║')
  print('╚═══════════════════════════════════════════════╝')

# Validacao de senha do mesario
def validaSenha(senha):
  contraSenha = input('Nescessario entrar com a senha: ')
  if senha != contraSenha:
    senhaIncorreta()
    limpar()
    return validaSenha(senha)
  else:
    print('\n')
    print('╔═══════════════════════════════════════════════╗')
    print('║                Acesso Liberado !              ║')
    print('╚═══════════════════════════════════════════════╝')
    print('\n')

# Cadastra a senha do mesario
def cadastraSenha():
  print()
  print('╔═══════════════════════════════════════════════╗')
  print('║         Cadastre uma senha para iniciar       ║')
  print('╚═══════════════════════════════════════════════╝')

  senha = input('\nDigite uma senha para cadastrar: ')
  if senha == '':
    senhaIncorreta()
    limpar()
    return cadastraSenha()

  senhaConfirmada = input('Confirme a senha: ')

  if senha != senhaConfirmada:
    senhaIncorreta()
    limpar()
    return cadastraSenha()
  
  print()
  print('╔═══════════════════════════════════════════════╗')
  print('║                SENHA CADASTRADA !             ║')
  print('╚═══════════════════════════════════════════════╝')

  return senha

# Caso a senha esteja incorreta 
def senhaIncorreta():
  print('\n')
  print('╔═══════════════════════════════════════════════╗')
  print('║                 Senha Invalida !              ║')
  print('╚═══════════════════════════════════════════════╝')
  print('\n')

def opcaoInvalida():
  print('\n')
  print('╔═══════════════════════════════════════════════╗')
  print('║                 Opcao invalida !              ║')
  print('╚═══════════════════════════════════════════════╝')
  print('\n')

# Liberar votos ou encerrrar processos
def opcaoMesario():
  menuMesario()
  opcao = input('Digite uma opcao: ')

  # Verifica se as opcoes estao dentro dos parametros estabelecidos
  if not(opcao == '2' or opcao == '1'):
    opcaoInvalida()
    limpar()
    return opcaoMesario()
  else:
    if opcao == '1':
      limpar()
      liberaVoto()
    if opcao == '2':
      encerraProcesso()

# valida o voto
def confirmaVoto(voto):

  # Verificacoes aninhadaas para ficar mais facil de saber visualmente para quem vai o voto
  if voto == '44':
    opcao = votos[0][0]           # Java
  elif voto == '12':
    opcao = votos[1][0]           # Python
  elif voto == '7':
    opcao = votos[2][0]           # Javascript
  elif voto == '0':
    opcao = votos[3][0]           # Branco
  else:
    opcao = votos[4][0]           # nulo 

  # Confirma para o usuarip o seu voto
  print('O seu voto será {}'.format(opcao))
  decisao = input('Aperte enter para confirmar ou digite qualquer coisa para cancelar: ')

  # Verifica se é isso mesmo que o usuario quer
  if not decisao == '':
    print('Voto cancelado !')
    limpar()
    return liberaVoto()
  else:
    return True

# Caso o voto tenha sido liberado
def liberaVoto():
  print('╔═══════════════════════════════════════════════╗')
  print('║                                               ║')
  print('║    OLA CIDADAO, BEM VINDO A URNA ELEITORAL    ║')
  print('║                                               ║')
  print('╠══════════════════════╦════════════════════════╣')
  print('║       CANDIDATO      ║   NUMERO DO CANDIDATO  ║')
  print('╠══════════════════════╬════════════════════════╣')
  print('║ ■ JAVA               ║           44           ║')
  print('║ ■ PYTHON             ║           12           ║')
  print('║ ■ JAVASCRIPT         ║           7            ║')
  print('║ ■ BRANCO             ║           0            ║')
  print('╚══════════════════════╩════════════════════════╝')

  voto = input('digite o seu voto: ')

  # Ficará em loop ate o usuario confirmar o voto dele
  if confirmaVoto(voto):
    if voto == '44':
      votos[0][1] += 1      # Java
    elif voto == '12':
      votos[1][1] += 1      # Python
    elif voto == '7':
      votos[2][1] += 1      # Javascript
    elif voto == '0':
      votos[3][1] += 1      # Branco
    else:
      votos[4][1] += 1      # nulo

    print('\n')
    print('╔═══════════════════════════════════════════════╗')
    print('║                 Voto realizado !              ║')
    print('╚═══════════════════════════════════════════════╝')
    print('\n')

# calcula a porcentagem dos votos
def percent(votosTotais, votos):
  # Calcula a porcentagem e ja devolve com as casas decimais ja limitadas
  return round(votos / votosTotais * 100, 2) 

def encerraProcesso():
  limpar()
  print('╔═══════════════════════════════════════════════╗')
  print('║              Encerrando processo ...          ║')
  print('╚═══════════════════════════════════════════════╝')
  limpar()


  # Calcula a quantidade total de votos 
  votosAbsolutos = 0
  for i in range(5):
    votosAbsolutos += votos[i][1]

  # Caso nao tenha votos suficientes e crashe o programa
  if votosAbsolutos == 0:
    print('╔═══════════════════════════════════════════════╗')
    print('║             Sem votos suficientes ...         ║')
    print('╚═══════════════════════════════════════════════╝')
    limpar()
    return 
  
  # Manda a porcentagem absoluta para os respectivos candidatos
  for i in range(5):
    votos[i][2] = percent(votosAbsolutos, votos[i][1])

  # Calcula o total de votos sem contar 'branco' e 'nulo'
  votosValidos = 0
  for i in range(3):
    votosValidos += votos[i][1]

  # Para nao crashar o programa caso nao tenha nenhum voto
  if votosValidos == 0:
    print('╔═══════════════════════════════════════════════╗')
    print('║             Sem votos suficientes ...         ║')
    print('╚═══════════════════════════════════════════════╝')
    limpar()
    return

  # Manda a porcentagem valida para os respectivos canditos
  for i in range(3):
    votos[i][3] = percent(votosValidos, votos[i][1])


  # Esse print ta me dando agonia :( todo torto, mas garanto que ta certinho
  print('╔════════════════════════════════════════════════════════════════╗')
  print('║                          VOTOS ABSOLUTOS                       ║')
  print('║═══════════════╦════════════════╦══════════════╦════════════════║')
  print('║    PARTIDO    ║   CANDIDATO    ║     VOTOS    ║   % DE VOTOS   ║')
  print('╠═══════════════╬════════════════╬══════════════╬════════════════╣')
  print('║      44       ║      JAVA      ║      {}\t║     {}%\t ║'.format(votos[0][1], votos[0][2]))
  print('║      12       ║     PYTHON     ║      {}\t║     {}%\t ║'.format(votos[1][1], votos[1][2]))
  print('║      07       ║   JAVASCRIPT   ║      {}\t║     {}%\t ║'.format(votos[2][1], votos[2][2]))
  print('║      00       ║     BRANCO     ║      {}\t║     {}%\t ║'.format(votos[3][1], votos[3][2]))
  print('║      --       ║      NULO      ║      {}\t║     {}%\t ║'.format(votos[4][1], votos[4][2]))
  print('╚═══════════════╩════════════════╩══════════════╩════════════════╝', '\n')


  print('╔════════════════════════════════════════════════════════════════╗')
  print('║                            VOTOS VALIDOS                       ║')
  print('║═══════════════╦════════════════╦══════════════╦════════════════║')
  print('║    PARTIDO    ║   CANDIDATO    ║     VOTOS    ║   % DE VOTOS   ║')
  print('╠═══════════════╬════════════════╬══════════════╬════════════════╣')
  print('║      44       ║      JAVA      ║      {}\t║     {}%\t ║'.format(votos[0][1], votos[0][3]))
  print('║      12       ║     PYTHON     ║      {}\t║     {}%\t ║'.format(votos[1][1], votos[1][3]))
  print('║      07       ║   JAVASCRIPT   ║      {}\t║     {}%\t ║'.format(votos[2][1], votos[2][3]))
  print('╚═══════════════╩════════════════╩══════════════╩════════════════╝', '\n')

  if verifica2Turno():
    segundoTurno()
  else:
    # Verifica quem ganhou
    ganhador = 'Ninguem'
    votosGanhador = 0
    for i in range(3):
      if votosGanhador < votos[i][1]:
        votosGanhador = votos[i][1]
        ganhador = votos[i][0]

    print('╔═══════════════════════════════════════╗')
    print('║        {} ganhou! Com {} votos\t║'.format(ganhador, votosGanhador))
    print('╚═══════════════════════════════════════╝\n')

    input('Aperte enter para finalizar.')

  exit()

# Verifica se possui necessidade de ter um segundo turno
def verifica2Turno():
  if votos[0][1] == votos[1][1] and votos[0][1] > 0:   # Java / Python
    votosSegundoTurno[0] = ['Java', 44, 0, 0]        # nome / partido / votos / %
    votosSegundoTurno[1] = ['Python', 12, 0, 0]      # nome / partido / votos / %
    return True

  elif votos[0][1] == votos[2][1]and votos[0][1] > 0:   # Java / JavaScript
    votosSegundoTurno[0] = ['Java', 44, 0, 0]         # nome / partido / votos / %
    votosSegundoTurno[1] = ['JavaScript', 7, 0, 0]    # nome / partido / votos / %
    return True

  elif votos[1][1] == votos[2][1] and votos[1][1] > 0:  # Python / JavaScript
    votosSegundoTurno[0] = ['Python', 12, 0, 0]       # nome / partido / votos / %
    votosSegundoTurno[1] = ['JavaScript', 7, 0, 0]    # nome / partido / votos / %
    return True

  else:
    return False

# realiza o segundo turno se precisar
def segundoTurno():
  print('╔═══════════════════════════════════════════════╗')
  print('║           Precisa de segundo turno ...        ║')
  print('╚═══════════════════════════════════════════════╝\n')

  input('Aperte enter para continuar.')
  limpar()

  while True:
    limpar()
    global senha
    validaSenha(senha)
    limpar()
    opcaoMesario2Turno()

# Opcoes do mesario segundo turno
def opcaoMesario2Turno():
  menuMesario()
  opcao = input('Digite uma opcao: ')

  # Verifica se as opcoes estao dentro dos parametros estabelecidos
  if not(opcao == '2' or opcao == '1'):
    opcaoInvalida()
    limpar()
    return opcaoMesario2Turno()
  else:
    if opcao == '1':
      limpar()
      liberaVoto2Turno()
    elif opcao == '2':
      limpar()
      encerraProcesso2Turno()

# Libera votos para o segundo turno
def liberaVoto2Turno():
  print('╔═══════════════════════════════════════════════╗')
  print('║                                               ║')
  print('║     OLA CIDADAO, BEM VINDO A URNA ELEITORAL   ║')
  print('║                                               ║')
  print('╠═══════════════════════╦═══════════════════════╣')
  print('║        CANDIDATO      ║  NUMERO DO CANDIDATO  ║')
  print('╠═══════════════════════╬═══════════════════════╣')
  print('║ ■ {}\t \t║          {}\t\t║'.format(votosSegundoTurno[0][0], votosSegundoTurno[0][1]))
  print('║ ■ {}\t \t║          {}\t\t║'.format(votosSegundoTurno[1][0], votosSegundoTurno[1][1]))
  print('╚═══════════════════════╩═══════════════════════╝')

  voto = input('digite o seu voto: ')
  confirmaVoto = input('Aperte enter para confirmar ou digite algo para cancelar: ')

  if len(confirmaVoto) != '':
    
    # Caso esteja tudo certo manda o voto para o respctivo lugar
    if voto == str(votosSegundoTurno[0][1]):
      votosSegundoTurno[0][2] += 1
    elif voto == str(votosSegundoTurno[1][1]):
      votosSegundoTurno[1][2] += 1

    # Caso o voto seja fora das opcoes
    else:
      print('Voto invalido!')
      limpar()
      return liberaVoto2Turno()

    print('\n')
    print('╔═══════════════════════════════════════════════╗')
    print('║                 Voto realizado !              ║')
    print('╚═══════════════════════════════════════════════╝')
    print('\n')

    # Volta para o mesario
    return
  else:
    print('\n╔═══════════════════════════════════════════════╗')
    print('║                  Voto Invalido !              ║')
    print('╚═══════════════════════════════════════════════╝')
    limpar()
    return liberaVoto2Turno()

# Encerra o processo do segundo turno
def encerraProcesso2Turno():

  # Calcula o total de votos do segundo turno
  votosTotais = 0
  for i in range(2):
    votosTotais += votosSegundoTurno[i][2]

  if votosSegundoTurno[0][2] == votosSegundoTurno[1][2]:
    print('╔═══════════════════════════════════════════════╗')
    print('║               Precisa desempatar ...          ║')
    print('╚═══════════════════════════════════════════════╝\n')
    limpar()
    return opcaoMesario2Turno()
  
  # Para nao deixar finalizar sem ter votos
  if votosTotais == 0:
    print('╔═══════════════════════════════════════════════╗')
    print('║             Sem votos suficientes ...         ║')
    print('╚═══════════════════════════════════════════════╝\n')
    return
 
  # Calcula a porcentagem de cada candidato
  for i in range(2):
    votosSegundoTurno[i][3] = percent(votosTotais, votosSegundoTurno[i][2])

  print('╔═══════════════════════════════════════════════════════════════╗')
  print('║                          VOTOS ABSOLUTOS                      ║')
  print('║═══════════════╦═══════════════╦════════════╦══════════════════║')
  print('║    PARTIDO    ║   CANDIDATO   ║   VOTOS    ║   % DE VOTOS     ║')
  print('╠═══════════════╬═══════════════╬════════════╬══════════════════╣')
  print('║   {}\t║       {}\t║      {}     ║      {}%\t║'.format(votosSegundoTurno[0][0], votosSegundoTurno[0][1], votosSegundoTurno[0][2], votosSegundoTurno[0][3]))
  print('║   {}\t║       {}\t║      {}     ║      {}%\t║'.format(votosSegundoTurno[1][0], votosSegundoTurno[1][1], votosSegundoTurno[1][2], votosSegundoTurno[1][3]))
  print('╚═══════════════╩═══════════════╩════════════╩══════════════════╝', '\n')

  exit()

# Variaveis globais para melhor controle

# Opcoes voto
votos = [['Java', 0, 0, 0],           # Nome / votos / % absoluta / % valida
         ['Python', 0, 0, 0],         # Nome / votos / % absoluta / % valida
         ['JavaScript', 0, 0, 0],     # Nome / votos / % absoluta / % valida
         ['Branco', 0, 0, 0],         # Nome / votos / % absoluta / % valida
         ['Nulo', 0, 0, 0]]           # Nome / votos / % absoluta / % valida

# vetor onde irá armazenar os dados de quem ir para o segundo turno
votosSegundoTurno = [['nome', 'partido', 0, 0],
                     ['nome', 'partido', 0, 0]] 

# Para ficar mais facil a verificacao de votos válidos
opcVotos = [44, 12, 7, 0]       

# Tempo para trocar entre as telas
tempo = 1.2                  

# Para o algoritmo saber se tem que cadastrar senha ou não
aux = True
senha = '123'

# funcao principal onde fica todo o algoritmo
def main():
  limpar()

  global aux
  global senha

  if aux:             # Caso nao exista uma senha ele faz o mesario cadastrar
    senha = cadastraSenha()
    aux = False

  limpar()
  validaSenha(senha)

  limpar()
  opcaoMesario()

# deixa a votação em loop ate o mesario decidir parar
while True:  
  main()