# -*- coding: utf-8 -*-

class neighborss(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def neighborss_neighbors(self, neighbors):
        self.neighbors = neighbors

    def __repr__(self):
        return self.name


joao_pessoa = neighborss("João Pessoa", 460)
campina_grande = neighborss("Campina Grande", 300)
itabaiana = neighborss("Itabaiana", 360)
santa_rita = neighborss("Santa Rita", 451)
mamanguape = neighborss("Mamanguape", 380)
guarabira = neighborss("Guarabira", 340)
areia = neighborss("Areia", 316)
picui = neighborss("Picui", 250)
soledade = neighborss("Soledade", 243)
coxixola = neighborss("Coxixola", 232)
patos = neighborss("Patos", 122)
monteiro = neighborss("Monteiro", 195)
catole = neighborss("Catolé do Rocha", 110)
pombal = neighborss("Pombal", 55)
itaporanga = neighborss("Itaporanga", 65)
sousa = neighborss("Sousa", 20)
cajazeiras = neighborss("Cajazeiras", 0)


joao_pessoa.neighborss_neighbors([[itabaiana, 68], [campina_grande, 125], [santa_rita, 26]])
itabaiana.neighborss_neighbors([[joao_pessoa, 68], [campina_grande, 65]])
santa_rita.neighborss_neighbors([[joao_pessoa, 26], [mamanguape, 38]])
campina_grande.neighborss_neighbors([[joao_pessoa, 125], [itabaiana, 65], [coxixola, 128], [areia, 40], [soledade, 58]])
mamanguape.neighborss_neighbors([[santa_rita, 38], [guarabira, 42]])
guarabira.neighborss_neighbors([[mamanguape, 42], [areia, 41]])
areia.neighborss_neighbors([[guarabira, 41], [campina_grande, 40]])
soledade.neighborss_neighbors([[campina_grande, 58], [picui, 69], [patos, 117]])
coxixola.neighborss_neighbors([[campina_grande, 128], [monteiro, 83]])
picui.neighborss_neighbors([[soledade, 69]])
patos.neighborss_neighbors([[soledade, 117], [pombal, 71], [itaporanga, 108]])
monteiro.neighborss_neighbors([[coxixola, 83], [itaporanga, 224]])
pombal.neighborss_neighbors([[patos, 71], [catole, 57], [sousa, 56]])
catole.neighborss_neighbors([[pombal, 57]])
itaporanga.neighborss_neighbors([[patos, 108], [cajazeiras, 121], [monteiro, 224]])
sousa.neighborss_neighbors([[pombal, 56], [cajazeiras, 43]])
cajazeiras.neighborss_neighbors([[sousa, 43], [itaporanga, 121]])

def search( fist_state, last_state):
    frontier= [[fist_state, 0]]
    explored= set()
    
    while True:
        print("frontier")
        print(frontier)
        if len(frontier)== 0:
            return False

        newState= choiceState(frontier)
        explored.add(newState[0])
        print("choice")
        print(newState[0])

        if newState[0]== last_state:
            return newState
        
        for state in newState[0].neighbors:
            neighbors= state[0]
            price= state[1]

            if neighbors not in explored:
                if inFrontier( frontier, neighbors):
                    exchangeFrontier( frontier, neighbors, price+newState[1])
                else:
                    frontier.append([neighbors,price+ newState[1]])
    

def choiceState(frontier):
    littleValue = frontier[0][1]+ frontier[0][0].value
    indexState= 0
     
    for i in range(len(frontier)):
        state= frontier[i]
        price= state[1]+ state[0].value
         
        if price < littleValue:
            littleValue= price
            indexState= i

    return frontier.pop(indexState)

def inFrontier(frontier,neighbors):
    for state in frontier:
        if neighbors== state[0]:
            return True
    
    return False

def exchangeFrontier(frontier,neighbors, price):
    for help in frontier:
        if neighbors == help[0]:
            if price+ help[0].value< help[1]+ help[0].value:
                help[1]= price
	
objective= search(joao_pessoa, cajazeiras)
print(objective)