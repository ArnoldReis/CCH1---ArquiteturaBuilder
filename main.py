
class Pedido:
    def __init__(self):
        self.sanduiche = None
        self.tipo_pao = None         
        self.bebida = None
        self.tamanho_bebida = None  
        self.acompanhamento = None
        self.sobremesa = None

    def mostrar_pedido(self):
        return (
            f"Pedido: Sanduiche: {self.sanduiche} (Pao: {self.tipo_pao}), "
            f"Bebida: {self.bebida} (Tamanho: {self.tamanho_bebida}), "
            f"Acompanhamento: {self.acompanhamento}, Sobremesa: {self.sobremesa}"
        )

class PedidoBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.pedido = Pedido()
        return self

    def set_sanduiche(self, tipo):
        self.pedido.sanduiche = tipo
        return self

    def set_tipo_pao(self, tipo):
        self.pedido.tipo_pao = tipo
        return self

    def set_bebida(self, bebida):
        self.pedido.bebida = bebida
        return self

    def set_tamanho_bebida(self, tamanho):
        self.pedido.tamanho_bebida = tamanho
        return self

    def set_acompanhamento(self, acompanhamento):
        self.pedido.acompanhamento = acompanhamento
        return self

    def set_sobremesa(self, sobremesa):
        self.pedido.sobremesa = sobremesa
        return self

    def build(self):
        return self.pedido

class Diretor:
    @staticmethod
    def criar_combo_vegetariano():
        builder = PedidoBuilder()
        return (
            builder.reset()
                   .set_sanduiche("Sanduiche Vegetariano")
                   .set_tipo_pao("Integral")
                   .set_bebida("Suco de Laranja")
                   .set_tamanho_bebida("Médio")
                   .set_acompanhamento("Salada de Folhas")
                   .set_sobremesa("Salada de Frutas")
                   .build()
        )

    @staticmethod
    def criar_combo_carnivoro():
        builder = PedidoBuilder()
        return (
            builder.reset()
                   .set_sanduiche("Sanduiche de Carne")
                   .set_tipo_pao("Brioche")
                   .set_bebida("Refrigerante")
                   .set_tamanho_bebida("Grande")
                   .set_acompanhamento("Batata Frita")
                   .set_sobremesa("Sorvete")
                   .build()
        )

    @staticmethod
    def criar_combo_especial():
        builder = PedidoBuilder()
        return (
            builder.reset()
                   .set_sanduiche("Sanduiche Especial")
                   .set_tipo_pao("Centeio")
                   .set_bebida("Cha Gelado")
                   .set_tamanho_bebida("Medio")
                   .set_acompanhamento("Chips")
                   .set_sobremesa("Cookie")
                   .build()
        )

    @staticmethod
    def criar_pedido_customizado(sanduiche, tipo_pao, bebida, tamanho_bebida, acompanhamento, sobremesa):
        builder = PedidoBuilder()
        return (
            builder.reset()
                   .set_sanduiche(sanduiche)
                   .set_tipo_pao(tipo_pao)
                   .set_bebida(bebida)
                   .set_tamanho_bebida(tamanho_bebida)
                   .set_acompanhamento(acompanhamento)
                   .set_sobremesa(sobremesa)
                   .build()
        )

if __name__ == "__main__":
    combo_veg = Diretor.criar_combo_vegetariano()
    combo_carni = Diretor.criar_combo_carnivoro()
    combo_especial = Diretor.criar_combo_especial()

    pedido_custom = Diretor.criar_pedido_customizado(
        sanduiche="Sanduiche de Frango Defumado",
        tipo_pao="Ciabatta",
        bebida="Suco de Maracuja",
        tamanho_bebida="Pequeno",
        acompanhamento="Mix de Vegetais",
        sobremesa="Brownie"
    )

    print("Combo Vegetariano:")
    print(combo_veg.mostrar_pedido())
    print("\nCombo Carnivoro:")
    print(combo_carni.mostrar_pedido())
    print("\nCombo Especial:")
    print(combo_especial.mostrar_pedido())
    print("\nPedido Customizado:")
    print(pedido_custom.mostrar_pedido())
