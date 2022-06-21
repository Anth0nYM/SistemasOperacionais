#executando #finalizado
import random
import time
class Processo:
    def __init__(self,ID,status = ['pronto','bloqueado']):
        #tempoExecucao é o tempo que o processo leva para executar
        #quantum é o tempo que o processo tem na CPU
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

exibirListaDeProcessos()
limpar = input('\n\nPressione enter para continuar')
if limpar == '':
    print("\x1b[2J") #Use isso para limpar a tela no Linux/Mac
    #print("\n" * 130) Use isso para limpar a tela no Windows
for i in range(len(listaDeExecucao)):
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
            listaDeExecucao[i].prioridade = 1
            organizar(listaDeExecucao)
            print('Seu processo foi bloqueado e foi colocado no fim da fila')
            time.sleep(2)
            print("\x1b[2J") 
            listaDeExecucao = organizar(processos)
            exibirListaDeProcessos()
        else:
            listaDeExecucao[i].status = 'finalizado'
            print('Processo {} está finalizado'.format(listaDeExecucao[i].ID))
            time.sleep(2)
            print("\x1b[2J") 
    exibirListaDeProcessos()
    
            
            
            
        






