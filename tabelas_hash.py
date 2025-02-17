from hashlib import sha256

class tabela_hash:
    class __Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor

    def __init__(self):
        self.__capacidade_atual = 5 #capacidade/tamanho da tabela interna
        self.__tabela_interna =  [[] for _ in range(self.__capacidade_atual)]
        self.__tamanho = 0 # quantidade de elementos salvos na tabela hash

    def __len__(self):
        return self.__tamanho

    @staticmethod
    def __verificar_chave(chave):
        hash(chave)

    @staticmethod
    def __hash_deterministico(chave):
        codificado = str(chave).encode()
        return int(sha256(codificado).hexdigest(), 16)

    def __descobrir_indice(self, chave):
        return self.__hash_deterministico(chave) % self.__capacidade_atual

    def __setitem__(self, chave, valor):
        self.__verificar_chave(chave)

        indice = self.__descobrir_indice(chave)

        #Verifica se a chave já existe na tabela 
        for elemento in self.__tabela_interna[indice]:
            if elemento.chave == chave:
                elemento.valor = valor #atualiza o valor no índice
                return 

        #Se não encontrar, adiciona um novo elemento
        novo_elemento = self.__Elemento(chave, valor)
        self.__tabela_interna[indice].append(novo_elemento)
        self.__tamanho += 1

    def __iter__(self):
        for lista in self.__tabela_interna:
            for elemento in lista:
                yield elemento.chave, elemento.valor

    def __getitem__(self, chave):
        self.__verificar_chave(chave)

        indice = self.__descobrir_indice(chave)
        
        for elemento in self.__tabela_interna[indice]:
            if elemento.chave == chave:
                return elemento.valor

        raise KeyError(f'Chave {chave} não encontrada')


pessoa = tabela_hash()

pessoa['nome'] = 'Alysson José'
pessoa['idade'] = 25
pessoa['sexo'] = 'Masculino'
pessoa['profissao'] = 'Desenvolvedor'
pessoa['nacionalidade'] = 'Brasileiro'
pessoa['salario'] = 12500.00
pessoa['cpf'] = '07457868399'

print(f'Quantidade de elementos: {len(pessoa)}')
#print(f'Nome: {pessoa["salario"]}')

for k, v in pessoa:
    print(f'{k} = {v}')