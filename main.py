import random
import time
class Processo:
    def __init__(self,ID,status = ['pronto','bloqueado']):
        self.prioridade = random.randint(1,5)
        self.tempo_execucao = random.randint(1,8) 
        self.status = random.choice(status)
        self.ID = ID
    def __str__(self):
        return f'ID: {self.ID}, prioridade: {self.prioridade}, tempo de execucao: {self.tempo_execucao}, status: {self.status}'

processos = [Processo(i) for i in range(5)] 

def organizar(processos):
    processos.sort(reverse = True,key = lambda x: x.prioridade)
    return processos

listaDeExecucao = organizar(processos)

def exibirListaDeProcessos():
    print('_'*155)
    print('LISTA DE EXECUCAO:')
    print('\n',listaDeExecucao[0],'\n',listaDeExecucao[1],'\n',listaDeExecucao[2],'\n',listaDeExecucao[3],'\n',listaDeExecucao[4])
    print('_'*155)


def verificacaoDeParada():
    if  listaDeExecucao[0].status == 'finalizado' and listaDeExecucao[1].status == 'finalizado' and listaDeExecucao[2].status=='finalizado' and listaDeExecucao[3].status == 'finalizado'and listaDeExecucao[4].status == 'finalizado':
        return True
    else:
        return False
    

exibirListaDeProcessos()
limpar = input('\nPressione enter para prosseguir \n>')
if limpar == '':
    print("\n" * 130)

while verificacaoDeParada() == False:
    for i in range(0,5):
        if listaDeExecucao[i].status == 'pronto':
            print('Processo {} está pronto'.format(listaDeExecucao[i].ID))
            time.sleep(2)
            listaDeExecucao[i].status = 'executando'
            print('Processo {} está executando'.format(listaDeExecucao[i].ID))
            time.sleep(2)
            if listaDeExecucao[i].tempo_execucao > 6:
                listaDeExecucao[i].tempo_execucao -= 6
                listaDeExecucao[i].status = 'bloqueado' 
                print('Processo {} está bloqueado'.format(listaDeExecucao[i].ID))
                time.sleep(2)
                for p in range(5):
                    if listaDeExecucao[p].ID != listaDeExecucao[i].ID and listaDeExecucao[p].status != 'bloqueado' and listaDeExecucao[p].status != 'finalizado':
                        listaDeExecucao[p].prioridade += 1
                listaDeExecucao = organizar(listaDeExecucao)
                print('Seu processo foi bloqueado')
                time.sleep(2)
                print("\n" * 130) 
                exibirListaDeProcessos()
                input('\nPressione enter para prosseguir \n>')
                time.sleep(2)
            else:
                listaDeExecucao[i].status = 'finalizado'
                print('Processo {} está finalizado'.format(listaDeExecucao[i].ID))
                for p in range(5):
                    if listaDeExecucao[p].ID != listaDeExecucao[i].ID and listaDeExecucao[p].status != 'bloqueado' and listaDeExecucao[p].status != 'finalizado':
                        listaDeExecucao[p].prioridade += 1
                time.sleep(2)
                print("\n" * 130)
                exibirListaDeProcessos() 
                input('\nPressione enter para prosseguir \n>')
    for i in range(0,5):
        if listaDeExecucao[i].status == 'bloqueado':
            listaDeExecucao[i].status = 'pronto'
        elif listaDeExecucao[i].status == 'finalizado':
            continue
    exibirListaDeProcessos()   