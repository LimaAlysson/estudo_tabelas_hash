from hashlib import sha256
from math import ceil

class tabela_hash:
    class __Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor
        
        def __str__(self):
            return f'{self.chave}: {self.valor}'
        
        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self.__capacidade_atual = 5 #capacidade/tamanho da tabela interna
        self.__tabela_interna =  [[] for _ in range(self.__capacidade_atual)]
        self.__tamanho = 0 # quantidade de elementos salvos na tabela hash

        self.__limiar_expandir = 0.75
        self.__fator_expansao = 2
        self.__limiar_reduzir = 0.20
        self.__fator_reducao = 0.5

    def __str__(self):
        retorno = '{'
        total= len(self)
        i = 0
        for k, v  in self:
            if isinstance(k, str):
                retorno += f"'{k}': "
            else:
                retorno += f'{k}: '

            if isinstance(v, str):
                retorno += f"'{v}'"
            else:
                retorno += f'{v}'

            if i < total - 1:
                retorno += ', '

            i += 1

        retorno += '}'

        return retorno
    
    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.__tamanho
    
    @property
    def __fator_carga(self):
        return self.__tamanho / self.__capacidade_atual

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

        if self.__fator_carga >= self.__limiar_expandir:
            self.__atualizar_tabela(self.__capacidade_atual * self.__fator_expansao)

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
    
    def __delitem__(self,chave):
        self.__verificar_chave(chave)

        if self.__fator_carga <= self.__limiar_reduzir:
            self.__atualizar_tabela(ceil(self.__capacidade_atual * self.__fator_reducao))

        indice = self.__descobrir_indice(chave)

        for i, elemento in enumerate(self.__tabela_interna[indice]):
            if elemento.chave == chave:
                del self.__tabela_interna[indice][i]
                self.__tamanho -= 1
                return
        
        raise KeyError(f'Chave {chave} não encontrada')

    def __atualizar_tabela(self, nova_capacidade):
        tabela_antiga = self.__tabela_interna

        self.__tabela_interna = [[] for _ in range(nova_capacidade)]
        self.__capacidade_atual = nova_capacidade
        self.__tamanho = 0

        for lista in tabela_antiga:
            for elemento in lista:
                self[elemento.chave] = elemento.valor

######################################################################################################

pessoa = tabela_hash()

pessoa['nome'] = 'Alysson José'
pessoa['idade'] = 25
pessoa['sexo'] = 'Masculino'
pessoa['profissao'] = 'Desenvolvedor'
pessoa['nacionalidade'] = 'Brasileiro'
pessoa['salario'] = 12500.00
pessoa['cpf'] = '07457868399'
pessoa['estado_civil'] = 'Solteiro'
pessoa['cor'] = 'Preto'
pessoa['altura'] = 1.72
pessoa['peso'] = 100
pessoa['cor_olhos'] = 'Castanho'
pessoa['cor_cabelo'] = 'Preto'
pessoa['tipo_sanguineo'] = 'O+'
pessoa['endereco'] = 'Rua das Flores, 123'
pessoa['cidade'] = 'Crato'
pessoa['estado'] = 'CE'
pessoa['pais'] = 'Brasil'
pessoa['cep'] = '63000-000'
pessoa['telefone'] = '(88) 88888-8888'
pessoa['email'] = ' email@email.com'
pessoa['rg'] = '20087100473'

print(f'Quantidade de elementos: {len(pessoa)}')

del pessoa['email']
del pessoa['telefone']
del pessoa['cep']
del pessoa['pais']
del pessoa['estado']
del pessoa['cidade']
del pessoa['endereco']
del pessoa['tipo_sanguineo']
del pessoa['cor_cabelo']
del pessoa['cor_olhos']
del pessoa['peso']
del pessoa['altura']
del pessoa['cor']
del pessoa['estado_civil']
del pessoa['cpf']
del pessoa['salario']
del pessoa['nacionalidade']
del pessoa['profissao']
del pessoa['sexo']
del pessoa['idade']
del pessoa['nome']


print(pessoa)