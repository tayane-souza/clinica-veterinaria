from clinica_veterinaria.visao.interface import InterfaceLinhaComando


class Programa:

    @staticmethod
    def main():
        interface = InterfaceLinhaComando()
        interface.executar()


if __name__ == "__main__":
    Programa.main()
