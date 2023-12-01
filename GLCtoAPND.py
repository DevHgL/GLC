# Lê as regras GLC de um arquivo texto
arquivo = 'glc.txt'
regras = {}

# Analisa as regras GLC
# Armazena no dicionário, onde os não terminais são as chaves e 
# o resto armazena como listas de strings
with open(arquivo, 'r') as file:
    for linha in file:
        linha = linha.strip()
        if linha:
            esq, dir = linha.split('->') 
            esq = esq.strip()
            dir = dir.strip().split('|')

            # confere se a chave do lado esquerdo já existe
            if esq not in regras:
                regras[esq] = []

            # itera sobre cada lado direito e a anexa à lista à chave esq correspondente
            #no dicionário
            for elem in dir:
                # Substitui "e" por "ε"
                elem = elem.replace("e", "ε")
                regras[esq].append(elem)


#Inicializa a lista de transições
transicoes = []

# Define as transições do APND baseado nas regras do GLC
# Formato (q, a, A) = (p, B) , em que A -> B
for esq in regras: 
    for dir in regras[esq]:
      transicao = f"(q, ε, {esq}) = (q, {dir})"
      transicoes.append(transicao) # 

# Armazena os terminais (símbolos minúsculos) encontrados
terminais = set()
for esq in regras: 
    for dir in regras[esq]:
        for simb in dir:
            if (simb.islower() and simb != 'ε'):
                terminais.add(simb)

for terminal in terminais: # itera sobre cada símbolo terminal e adiciona uma transição
    transicao = f"(q, {terminal}, {terminal}) = (q, ε)"
    transicoes.append(transicao)

# Imprime
for transition in transicoes:
    print(transition)
