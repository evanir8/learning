from abc import ABCMeta, abstractclassmethod


class Estado_de_um_orcamento(object):
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractclassmethod
    def aprova(self, orcamento):
        pass

    @abstractclassmethod
    def reprova(self, orcamento):
        pass

    @abstractclassmethod
    def finaliza(self, orcamento):
        pass


class Em_aprovacao(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orcamento em aprovacao não pode ser finalizado!')


class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        print("aplicando desconto de aprovacao")
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception('Orcamento ja esta aprovado')

    def reprova(self, orcamento):
        raise Exception('Orcamento ja esta aprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos reprovados não terão descontos extras!')

    def aprova(self, orcamento):
        raise Exception('Orcamento foi Reprovado, nao pode ser Aprovado')

    def reprova(self, orcamento):
        raise Exception('Orcamento ja esta REaprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos finalizados não terão descontos extras!')

    def aprova(self, orcamento):
        raise Exception('Orcamento foi finalizado, nao pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Orcamento foi finalizado, nao pode ser REprovado')

    def finaliza(self, orcamento):
        raise Exception('Orcamento foi finalizado')


class Orcamento():
    def __init__(self):
        self.__items = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0
        self.__descontos_aplicados = []

    def aprova(self):
        self.estado_atual.aprova(orcamento)

    def reprova(self):
        print('Orcamento Reprovado')
        self.estado_atual.reprova(orcamento)

    def finaliza(self):
        print('Orcamento Finalizado')
        self.estado_atual.finaliza(orcamento)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        if not (self.estado_atual in self.__descontos_aplicados):
            print("desconto = {}".format(desconto))
            self.__desconto_extra += desconto
            self.__descontos_aplicados.append(self.estado_atual)
            print(self.__descontos_aplicados)
        else:
            print("Ja aplicado descontos extras")

    @property
    def valor(self):
        total = 0.0
        for item in self.__items:
            total += item.valor
        return total - self.__desconto_extra

    def obter_items(self):
        return tuple(self.__items)

    @property
    def total_items(self):
        return len(self.__items)

    def adiciona_item(self, item):
        self.__items.append(item)


class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item1', 100))
    orcamento.adiciona_item(Item('Item1', 50))
    orcamento.adiciona_item(Item('Item1', 400))

    print(orcamento.valor)
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)

    # orcamento.reprova()
    # orcamento.aplica_desconto_extra()

    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)
