from clinica_veterinaria.modelo.veterinario import Veterinario
from clinica_veterinaria.modelo.tutor import Tutor
from clinica_veterinaria.modelo.animal import Animal
from clinica_veterinaria.modelo.procedimento import Procedimento
from clinica_veterinaria.modelo.consulta import Consulta
from clinica_veterinaria.modelo.item_consulta import ItemConsulta
from clinica_veterinaria.dados.fabrica_dao import FabricaDAO


class InterfaceLinhaComando:

    def __init__(self):
        self._dao_veterinario = FabricaDAO.obter_dao(Veterinario)
        self._dao_tutor = FabricaDAO.obter_dao(Tutor)
        self._dao_animal = FabricaDAO.obter_dao(Animal)
        self._dao_procedimento = FabricaDAO.obter_dao(Procedimento)
        self._dao_consulta = FabricaDAO.obter_dao(Consulta)

    def executar(self):
        continuar = True
        while continuar:
            print("\n=== Clinica Veterinaria ===")
            print("1 - Veterinarios")
            print("2 - Tutores")
            print("3 - Animais")
            print("4 - Procedimentos")
            print("5 - Consultas")
            print("0 - Sair")
            opcao = input("Escolha uma opcao: ").strip()
            if opcao == "1":
                self._menu_veterinario()
            elif opcao == "2":
                self._menu_tutor()
            elif opcao == "3":
                self._menu_animal()
            elif opcao == "4":
                self._menu_procedimento()
            elif opcao == "5":
                self._menu_consulta()
            elif opcao == "0":
                self._persistir_tudo()
                continuar = False
            else:
                print("Opcao invalida.")

    def _persistir_tudo(self):
        self._dao_veterinario.persistir()
        self._dao_tutor.persistir()
        self._dao_animal.persistir()
        self._dao_procedimento.persistir()
        self._dao_consulta.persistir()
        print("Dados salvos. Ate logo!")

    def _ler_inteiro(self, mensagem):
        return int(input(mensagem).strip())

    def _selecionar_veterinario(self, mensagem):
        entrada = input(mensagem).strip()
        if entrada == "":
            return None
        veterinario = self._dao_veterinario.buscar(int(entrada))
        if veterinario is None:
            print("Veterinario nao encontrado, ficara vazio.")
        return veterinario

    # ---------------- Veterinario ----------------

    def _menu_veterinario(self):
        continuar = True
        while continuar:
            print("\n--- Veterinarios ---")
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Apagar")
            print("4 - Visualizar por id")
            print("5 - Visualizar todos")
            print("0 - Voltar")
            opcao = input("Escolha uma opcao: ").strip()
            if opcao == "1":
                self._inserir_veterinario()
            elif opcao == "2":
                self._alterar_veterinario()
            elif opcao == "3":
                self._apagar_veterinario()
            elif opcao == "4":
                self._visualizar_por_id(self._dao_veterinario, "veterinario")
            elif opcao == "5":
                self._visualizar_todos(self._dao_veterinario, "veterinario")
            elif opcao == "0":
                continuar = False
            else:
                print("Opcao invalida.")

    def _inserir_veterinario(self):
        id_entidade = self._ler_inteiro("Id: ")
        nome = input("Nome: ").strip()
        crmv = input("CRMV: ").strip()
        especialidade = input("Especialidade: ").strip()
        coordenador = self._selecionar_veterinario("Id do veterinario coordenador (vazio para nenhum): ")
        veterinario = Veterinario(id_entidade, nome, crmv, especialidade, coordenador)
        if self._dao_veterinario.salvar(veterinario):
            print("Veterinario inserido com sucesso.")
        else:
            print("Ja existe um veterinario com esse id.")

    def _alterar_veterinario(self):
        id_entidade = self._ler_inteiro("Id do veterinario a alterar: ")
        nome = input("Novo nome: ").strip()
        crmv = input("Novo CRMV: ").strip()
        especialidade = input("Nova especialidade: ").strip()
        coordenador = self._selecionar_veterinario("Id do veterinario coordenador (vazio para nenhum): ")
        veterinario = Veterinario(id_entidade, nome, crmv, especialidade, coordenador)
        if self._dao_veterinario.atualizar(veterinario):
            print("Veterinario atualizado com sucesso.")
        else:
            print("Veterinario nao encontrado.")

    def _apagar_veterinario(self):
        id_entidade = self._ler_inteiro("Id do veterinario a apagar: ")
        removido = self._dao_veterinario.apagar(id_entidade)
        print("Veterinario removido." if removido else "Veterinario nao encontrado.")

    # ---------------- Tutor ----------------

    def _menu_tutor(self):
        continuar = True
        while continuar:
            print("\n--- Tutores ---")
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Apagar")
            print("4 - Visualizar por id")
            print("5 - Visualizar todos")
            print("0 - Voltar")
            opcao = input("Escolha uma opcao: ").strip()
            if opcao == "1":
                self._inserir_tutor()
            elif opcao == "2":
                self._alterar_tutor()
            elif opcao == "3":
                self._apagar_tutor()
            elif opcao == "4":
                self._visualizar_por_id(self._dao_tutor, "tutor")
            elif opcao == "5":
                self._visualizar_todos(self._dao_tutor, "tutor")
            elif opcao == "0":
                continuar = False
            else:
                print("Opcao invalida.")

    def _inserir_tutor(self):
        id_entidade = self._ler_inteiro("Id: ")
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        telefone = input("Telefone: ").strip()
        veterinario_responsavel = self._selecionar_veterinario(
            "Id do veterinario responsavel (vazio para nenhum): "
        )
        tutor = Tutor(id_entidade, nome, cpf, telefone, veterinario_responsavel)
        if self._dao_tutor.salvar(tutor):
            print("Tutor inserido com sucesso.")
        else:
            print("Ja existe um tutor com esse id.")

    def _alterar_tutor(self):
        id_entidade = self._ler_inteiro("Id do tutor a alterar: ")
        nome = input("Novo nome: ").strip()
        cpf = input("Novo CPF: ").strip()
        telefone = input("Novo telefone: ").strip()
        veterinario_responsavel = self._selecionar_veterinario(
            "Id do veterinario responsavel (vazio para nenhum): "
        )
        tutor = Tutor(id_entidade, nome, cpf, telefone, veterinario_responsavel)
        if self._dao_tutor.atualizar(tutor):
            print("Tutor atualizado com sucesso.")
        else:
            print("Tutor nao encontrado.")

    def _apagar_tutor(self):
        id_entidade = self._ler_inteiro("Id do tutor a apagar: ")
        removido = self._dao_tutor.apagar(id_entidade)
        print("Tutor removido." if removido else "Tutor nao encontrado.")

    # ---------------- Animal ----------------

    def _menu_animal(self):
        continuar = True
        while continuar:
            print("\n--- Animais ---")
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Apagar")
            print("4 - Visualizar por id")
            print("5 - Visualizar todos")
            print("0 - Voltar")
            opcao = input("Escolha uma opcao: ").strip()
            if opcao == "1":
                self._inserir_animal()
            elif opcao == "2":
                self._alterar_animal()
            elif opcao == "3":
                self._apagar_animal()
            elif opcao == "4":
                self._visualizar_por_id(self._dao_animal, "animal")
            elif opcao == "5":
                self._visualizar_todos(self._dao_animal, "animal")
            elif opcao == "0":
                continuar = False
            else:
                print("Opcao invalida.")

    def _selecionar_tutor(self, mensagem):
        id_entidade = self._ler_inteiro(mensagem)
        tutor = self._dao_tutor.buscar(id_entidade)
        if tutor is None:
            print("Tutor nao encontrado.")
        return tutor

    def _inserir_animal(self):
        id_entidade = self._ler_inteiro("Id: ")
        nome = input("Nome: ").strip()
        especie = input("Especie: ").strip()
        raca = input("Raca: ").strip()
        idade = self._ler_inteiro("Idade: ")
        tutor = self._selecionar_tutor("Id do tutor: ")
        if tutor is None:
            return
        animal = Animal(id_entidade, nome, especie, raca, idade, tutor)
        if self._dao_animal.salvar(animal):
            print("Animal inserido com sucesso.")
        else:
            print("Ja existe um animal com esse id.")

    def _alterar_animal(self):
        id_entidade = self._ler_inteiro("Id do animal a alterar: ")
        nome = input("Novo nome: ").strip()
        especie = input("Nova especie: ").strip()
        raca = input("Nova raca: ").strip()
        idade = self._ler_inteiro("Nova idade: ")
        tutor = self._selecionar_tutor("Id do tutor: ")
        if tutor is None:
            return
        animal = Animal(id_entidade, nome, especie, raca, idade, tutor)
        if self._dao_animal.atualizar(animal):
            print("Animal atualizado com sucesso.")
        else:
            print("Animal nao encontrado.")

    def _apagar_animal(self):
        id_entidade = self._ler_inteiro("Id do animal a apagar: ")
        removido = self._dao_animal.apagar(id_entidade)
        print("Animal removido." if removido else "Animal nao encontrado.")

    # ---------------- Procedimento ----------------

    def _menu_procedimento(self):
        continuar = True
        while continuar:
            print("\n--- Procedimentos ---")
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Apagar")
            print("4 - Visualizar por id")
            print("5 - Visualizar todos")
            print("0 - Voltar")
            opcao = input("Escolha uma opcao: ").strip()
            if opcao == "1":
                self._inserir_procedimento()
            elif opcao == "2":
                self._alterar_procedimento()
            elif opcao == "3":
                self._apagar_procedimento()
            elif opcao == "4":
                self._visualizar_por_id(self._dao_procedimento, "procedimento")
            elif opcao == "5":
                self._visualizar_todos(self._dao_procedimento, "procedimento")
            elif opcao == "0":
                continuar = False
            else:
                print("Opcao invalida.")

    def _inserir_procedimento(self):
        id_entidade = self._ler_inteiro("Id: ")
        nome = input("Nome do procedimento: ").strip()
        descricao = input("Descricao: ").strip()
        valor_base = float(input("Valor base: ").strip())
        veterinario_responsavel = self._selecionar_veterinario(
            "Id do veterinario responsavel (vazio para nenhum): "
        )
        procedimento = Procedimento(id_entidade, nome, descricao, valor_base, veterinario_responsavel)
        if self._dao_procedimento.salvar(procedimento):
            print("Procedimento inserido com sucesso.")
        else:
            print("Ja existe um procedimento com esse id.")

    def _alterar_procedimento(self):
        id_entidade = self._ler_inteiro("Id do procedimento a alterar: ")
        nome = input("Novo nome do procedimento: ").strip()
        descricao = input("Nova descricao: ").strip()
        valor_base = float(input("Novo valor base: ").strip())
        veterinario_responsavel = self._selecionar_veterinario(
            "Id do veterinario responsavel (vazio para nenhum): "
        )
        procedimento = Procedimento(id_entidade, nome, descricao, valor_base, veterinario_responsavel)
        if self._dao_procedimento.atualizar(procedimento):
            print("Procedimento atualizado com sucesso.")
        else:
            print("Procedimento nao encontrado.")

    def _apagar_procedimento(self):
        id_entidade = self._ler_inteiro("Id do procedimento a apagar: ")
        removido = self._dao_procedimento.apagar(id_entidade)
        print("Procedimento removido." if removido else "Procedimento nao encontrado.")

    # ---------------- Consulta ----------------

    def _menu_consulta(self):
        continuar = True
        while continuar:
            print("\n--- Consultas ---")
            print("1 - Inserir")
            print("2 - Alterar")
            print("3 - Apagar")
            print("4 - Visualizar por id")
            print("5 - Visualizar todas")
            print("0 - Voltar")
            opcao = input("Escolha uma opcao: ").strip()
            if opcao == "1":
                self._inserir_consulta()
            elif opcao == "2":
                self._alterar_consulta()
            elif opcao == "3":
                self._apagar_consulta()
            elif opcao == "4":
                self._visualizar_por_id(self._dao_consulta, "consulta")
            elif opcao == "5":
                self._visualizar_todos(self._dao_consulta, "consulta")
            elif opcao == "0":
                continuar = False
            else:
                print("Opcao invalida.")

    def _inserir_consulta(self):
        id_entidade = self._ler_inteiro("Id: ")
        data_consulta = input("Data da consulta (dd/mm/aaaa): ").strip()
        diagnostico = input("Diagnostico: ").strip()
        id_animal = self._ler_inteiro("Id do animal: ")
        animal = self._dao_animal.buscar(id_animal)
        if animal is None:
            print("Animal nao encontrado.")
            return
        id_veterinario = self._ler_inteiro("Id do veterinario: ")
        veterinario = self._dao_veterinario.buscar(id_veterinario)
        if veterinario is None:
            print("Veterinario nao encontrado.")
            return
        consulta = Consulta(id_entidade, data_consulta, diagnostico, animal, veterinario)
        self._gerenciar_itens_consulta(consulta)
        if self._dao_consulta.salvar(consulta):
            print("Consulta inserida com sucesso.")
        else:
            print("Ja existe uma consulta com esse id.")

    def _alterar_consulta(self):
        id_entidade = self._ler_inteiro("Id da consulta a alterar: ")
        consulta = self._dao_consulta.buscar(id_entidade)
        if consulta is None:
            print("Consulta nao encontrada.")
            return
        self._gerenciar_itens_consulta(consulta)
        self._dao_consulta.atualizar(consulta)
        print("Consulta atualizada com sucesso.")

    def _gerenciar_itens_consulta(self, consulta):
        continuar = True
        while continuar:
            print(f"\nProcedimentos atuais: {consulta}")
            print("1 - Adicionar procedimento")
            print("2 - Remover procedimento")
            print("0 - Concluir")
            opcao = input("Escolha uma opcao: ").strip()
            if opcao == "1":
                id_procedimento = self._ler_inteiro("Id do procedimento: ")
                procedimento = self._dao_procedimento.buscar(id_procedimento)
                if procedimento is None:
                    print("Procedimento nao encontrado.")
                    continue
                valor_texto = input("Valor cobrado (vazio para usar o valor base): ").strip()
                valor_cobrado = float(valor_texto) if valor_texto != "" else None
                consulta.adicionar_item(ItemConsulta(procedimento, valor_cobrado))
            elif opcao == "2":
                id_procedimento = self._ler_inteiro("Id do procedimento a remover: ")
                if not consulta.remover_item(id_procedimento):
                    print("Procedimento nao encontrado na consulta.")
            elif opcao == "0":
                continuar = False
            else:
                print("Opcao invalida.")

    def _apagar_consulta(self):
        id_entidade = self._ler_inteiro("Id da consulta a apagar: ")
        removida = self._dao_consulta.apagar(id_entidade)
        print("Consulta removida." if removida else "Consulta nao encontrada.")

    # ---------------- Auxiliares genericos ----------------

    def _visualizar_por_id(self, dao, nome_entidade):
        id_entidade = self._ler_inteiro(f"Id do {nome_entidade}: ")
        objeto = dao.buscar(id_entidade)
        print(objeto if objeto else f"{nome_entidade.capitalize()} nao encontrado.")

    def _visualizar_todos(self, dao, nome_entidade):
        objetos = dao.carregar()
        if not objetos:
            print(f"Nenhum(a) {nome_entidade} cadastrado(a).")
        for objeto in objetos:
            print(objeto)
