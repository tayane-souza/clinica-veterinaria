import os
import pickle


class EntidadeDAO:

    def __init__(self, classe_entidade, pasta_dados="dados_persistidos"):
        self._classe_entidade = classe_entidade
        self._conjunto = set()
        self._pasta_dados = pasta_dados
        nome_arquivo = classe_entidade.__name__.lower() + ".dat"
        self._caminho_arquivo = os.path.join(pasta_dados, nome_arquivo)

    def salvar(self, objeto):
        if self.buscar(objeto.obter_id()) is not None:
            return False
        self._conjunto.add(objeto)
        return True

    def atualizar(self, objeto):
        existente = self.buscar(objeto.obter_id())
        if existente is None:
            return False
        self._conjunto.discard(existente)
        self._conjunto.add(objeto)
        return True

    def apagar(self, id_entidade):
        existente = self.buscar(id_entidade)
        if existente is None:
            return None
        self._conjunto.discard(existente)
        return existente

    def buscar(self, id_entidade):
        for objeto in self._conjunto:
            if objeto.obter_id() == id_entidade:
                return objeto
        return None

    def carregar(self):
        """Devolve uma lista (o "array" pedido no enunciado), ordenada por id."""
        lista = list(self._conjunto)
        lista.sort(key=lambda objeto: objeto.obter_id())
        return lista

    def persistir(self):
        """Salva o conjunto inteiro em um arquivo, na pasta dados_persistidos/."""
        os.makedirs(self._pasta_dados, exist_ok=True)
        arquivo = open(self._caminho_arquivo, "wb")
        pickle.dump(self._conjunto, arquivo)
        arquivo.close()

    def recuperar(self):
        """Le o conjunto salvo em arquivo, se ele existir."""
        if os.path.exists(self._caminho_arquivo):
            arquivo = open(self._caminho_arquivo, "rb")
            self._conjunto = pickle.load(arquivo)
            arquivo.close()
