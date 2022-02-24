lst = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lst.append([nome, [nota1, nota2], media])
    sair = str(input('Deseja Continuar? S/N ')).upper().strip().split()[0]
    if 'N' in sair:
        break
print('-' * 30)
print('N°  NOME          MÉDIA')
print('-' * 30)
for i, a in enumerate(lst):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Deseja mostrar as notas de qual aluno? (999 para sair) '))
    if opc == 999:
        print('FINALIZANDO ...')
        print("Até a próxima!")
        break
    if opc <= len(lst) - 1:
        print(f'Notas de {lst[opc][0]} são {lst[opc][1]}')
        print('VOLTE SEMPRE!')