from clinica_veterinaria.dados.entidade_dao import EntidadeDAO


class FabricaDAO:

    _daos = {}

    @staticmethod
    def obter_dao(classe_entidade):
        if classe_entidade not in FabricaDAO._daos:
            dao = EntidadeDAO(classe_entidade)
            dao.recuperar()
            FabricaDAO._daos[classe_entidade] = dao
        return FabricaDAO._daos[classe_entidade]
