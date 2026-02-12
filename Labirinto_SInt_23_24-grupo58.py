from searchPlus import *
import copy

line1 = "= = = = = = =\n"
line2 = "= x . . . . =\n"
line3 = "= . . . = . =\n"
line4 = "= . . . = . =\n"
line5 = "= = = . = . =\n"
line6 = "= ^ . . . . =\n"
line7 = "= = = = = = =\n"
grelha = line1 + line2 + line3 + line4 + line5 + line6 + line7

class Labirinto(Problem):

    def __init__(self, LabInicial=grelha, vmax=3):
        self.grelha=LabInicial
        self.vmax=vmax
        self.linhas=0
        self.colunas=0
        
        grelha=[]
        for i in self.grelha:
            if i=="\n":
                self.linhas=self.linhas+1
            if i!="\n" and i!=" ":
                grelha.append(i)
                self.colunas=self.colunas+1
        self.colunas=int(self.colunas/self.linhas)
                
        labirinto=[]
        
        for i in range(self.linhas):
            linha=grelha[i*self.colunas:(i+1)*self.colunas]
            labirinto.append(linha)
            
        for i in range(len(labirinto)):
            for j in range(len(labirinto[i])):
                if labirinto[i][j]=="x":
                    self.goal=[int(i),int(j)]
                if labirinto[i][j]=="^":
                    self.initial=[int(i),int(j),0,"N"]
                if labirinto[i][j]==">":
                    self.initial=[int(i),int(j),0,"E"]
                if labirinto[i][j]=="v":
                    self.initial=[int(i),int(j),0,"S"]
                if labirinto[i][j]=="<":
                    self.initial=[int(i),int(j),0,"O"]
            
        
        labirinto[self.initial[0]][self.initial[1]]="o" 
           
        self.labirinto=labirinto
        
        

    def actions (self, state):
        
       
        listactions=[]
        
        if state[2]==0:
            listactions.append("E")
            listactions.append("D")




        
        
        if state[3]=="N":
            newvelo=state[2]+1
            if newvelo>self.vmax:
                newvelo=self.vmax
                
            flag=False
            for i in range(newvelo):
                if state[0]-(i+1)<0:
                    flag=True
                    break
                else:
                    celula=self.labirinto[state[0]-(i+1)][state[1]]
                    if celula == "=" :
                        flag=True
            if flag==False:
                listactions.append("A")


            
                    
        if state[3]=="E":
            
            newvelo=state[2]+1
            if newvelo>self.vmax:
                newvelo=self.vmax
                
            flag=False
            for i in range(newvelo):
                if state[1]+(i+1)>=self.colunas:
                    flag=True
                    break
                else:
                    celula=self.labirinto[state[0]][state[1]+(i+1)]
                    if celula == "=" :
                        flag=True
            if flag==False:
                listactions.append("A")
            
                

        if state[3]=="S":
            
            newvelo=state[2]+1
            if newvelo>self.vmax:
                newvelo=self.vmax
                
            flag=False
            for i in range(newvelo):
                if state[0]+(i+1)>=self.linhas:
                    flag=True
                    break
                else:
                    celula=self.labirinto[state[0]+(i+1)][state[1]]
                    if celula == "=" :
                        flag=True
            if flag==False:
                listactions.append("A")
                

        if state[3]=="O":
            
            newvelo=state[2]+1
            if newvelo>self.vmax:
                newvelo=self.vmax
                
            flag=False
            for i in range(newvelo):
                if state[1]-(i+1)<0:
                    flag=True
                    break
                else:
                    celula=self.labirinto[state[0]][state[1]-(i+1)]
                    if celula == "=" :
                        flag=True
            if flag==False:
                listactions.append("A")
            
                    
                    
                            
        if state[2]-1 > 0:
            newvelod=state[2]-1
            if state[3]=="N":
                flag=False
                for i in range(newvelod):
                    if state[0]-(i+1)<0:
                        flag=True
                        break
                    else:
                        celula=self.labirinto[state[0]-(i+1)][state[1]]
                        if celula == "=" :
                            flag=True
                if flag==False:
                    listactions.append("T")
                    
        
            if state[3]=="E":
                flag=False
                for i in range(newvelod):
                    if state[1]+(i+1)>=self.colunas:
                        flag=True
                        break
                    else:
                        celula=self.labirinto[state[0]][state[1]+(i+1)]
                        if celula == "=" :
                            flag=True
                if flag==False:
                    listactions.append("T")

            if state[3]=="S":
                
                flag=False
                for i in range(newvelod):
                    if state[0]+(i+1)>=self.linhas:
                        flag=True
                        break
                    else:
                        celula=self.labirinto[state[0]+(i+1)][state[1]]
                        if celula == "=" :
                            flag=True
                if flag==False:
                    listactions.append("T")
                    
            if state[3]=="O":
                flag=False
                for i in range(newvelod):
                    if state[1]-(i+1)<0:
                        flag=True
                        break
                    else:
                        celula=self.labirinto[state[0]][state[1]-(i+1)]
                        if celula == "=" :
                            flag=True
                if flag==False:
                    listactions.append("T")
            

        if state[2] == 1:
            
            listactions.append("T")
            
        new=sorted(listactions)
        
        
        return new
         

    def result (self, state, action):
        newstate=copy.deepcopy(state)
        
        if action=="E":
            if state[3]=="N":
                
                newstate[3]="O"
                
            elif state[3]=="E":
                
                newstate[3]="N"
                
            elif state[3]=="S":
                
                newstate[3]="E"

            elif state[3]=="O":
                
                newstate[3]="S"
            else:
                print("erro")
                
            
        elif action=="D":
            
            if state[3]=="N":
                newstate[3]="E"
                
            elif state[3]=="E":
                
                
                newstate[3]="S"
                
            elif state[3]=="S":
                newstate[3]="O"
                
            elif state[3]=="O":
                newstate[3]="N"
            else:
                print("erro")
        elif action=="A":
            newstate[2]=newstate[2]+1
            if newstate[2]>self.vmax:
                newstate[2]=self.vmax
                if state[3]=="N":
                    self.labirinto[state[0]][state[1]]="."
                    
                    newstate[0]=newstate[0]-newstate[2]
                    self.labirinto[newstate[0]][newstate[1]]="o"
                
                elif state[3]=="E":
                    self.labirinto[state[0]][state[1]]="."
                    newstate[1]=newstate[1]+newstate[2]
                    self.labirinto[newstate[0]][newstate[1]]="o"
                elif state[3]=="S":
                    self.labirinto[state[0]][state[1]]="."
                    newstate[0]=newstate[0]+newstate[2]
                    self.labirinto[newstate[0]][newstate[1]]="o"
                elif state[3]=="O":
                    self.labirinto[state[0]][state[1]]="."
                    newstate[1]=newstate[1]-newstate[2]
                    self.labirinto[newstate[0]][newstate[1]]="o"
                else:
                    print("erro")
            else:
                
                if state[3]=="N":
                    self.labirinto[state[0]][state[1]]="."
                    newstate[0]=newstate[0]-newstate[2]
                    self.labirinto[newstate[0]][newstate[1]]="o"
                elif state[3]=="E":
                    self.labirinto[state[0]][state[1]]="."
                    newstate[1]=newstate[1]+newstate[2]
                    self.labirinto[newstate[0]][newstate[1]]="o"
                elif state[3]=="S":
                    self.labirinto[state[0]][state[1]]="."
                    newstate[0]=newstate[0]+newstate[2]
                    self.labirinto[newstate[0]][newstate[1]]="o"
                elif state[3]=="O":
                    self.labirinto[state[0]][state[1]]="."
                    newstate[1]=newstate[1]-newstate[2]
                    self.labirinto[newstate[0]][newstate[1]]="o"
                else:
                    print("erro")
                
        elif action=="T":

            
            newstate[2]=newstate[2]-1
            
            if state[3]=="N":
                self.labirinto[state[0]][state[1]]="."
                newstate[0]=newstate[0]-newstate[2]
                self.labirinto[newstate[0]][newstate[1]]="o"
                
            elif state[3]=="E":
                self.labirinto[state[0]][state[1]]="."
                newstate[1]=newstate[1]+newstate[2]
                self.labirinto[newstate[0]][newstate[1]]="o"
                
            elif state[3]=="S":
                self.labirinto[state[0]][state[1]]="."
                
                newstate[0]=newstate[0]+newstate[2]
                self.labirinto[newstate[0]][newstate[1]]="o"
            elif state[3]=="O":
                self.labirinto[state[0]][state[1]]="."
                
                newstate[1]=newstate[1]-newstate[2]
                self.labirinto[newstate[0]][newstate[1]]="o"
            else:
                print("erro")
        else:
            print("erro")
            
        
        if action in self.actions(state):
            return newstate
        
            

    def goal_test (self, state):
        
        if state[0:2]==self.goal:
            if state[2]==0:
                return True
            else:
                return False
        else:
            return False
            

    def display (self, state):
        
        final=""
        labirintonew=copy.deepcopy(self.labirinto)
        for i in range(self.linhas):
            for j in range(self.colunas):
                if labirintonew[i][j]=="o":
                    if state[3]=="N":
                        labirintonew[i][j]="^"
                    elif state[3]=="E":
                        labirintonew[i][j]=">"
                    elif state[3]=="S":
                        labirintonew[i][j]="v"
                    elif state[3]=="O":
                        labirintonew[i][j]="<"
                    else:
                        print("erro")
                final=final+labirintonew[i][j]+" "
                
            final=final+"\n"
        
            
        return final

    def executa(self, state, actions_list, verbose=False):
        """Executa uma sequência de acções a partir do estado devolvendo o triplo formado pelo estado, 
        pelo custo acumulado e pelo booleano que indica se o objectivo foi ou não atingido. Se o objectivo 
        for atingido antes da sequência ser atingida, devolve-se o estado e o custo corrente.
        Há o modo verboso e o não verboso, por defeito."""
        cost = 0
        for a in actions_list:
            seg = self.result(state,a)
            cost = self.path_cost(cost,state,a,seg)
            state = seg
            obj = self.goal_test(state)
            if verbose:
                print('Ação:', a)
                print(self.display(state),end='')
                print('Custo Total:',cost)
                print('Atingido o objectivo?', obj)
                print()
            if obj:
                break
        return (state, cost, obj)
