import flet as ft

class CadastroDespesaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        
        self.route = "/cadastro_desp"
        
        self.bgcolor = "#facada"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        titulo = ft.Text(value="Cadastre a suas despesas aqui!",
                                font_family="Times New Roman",
                                size=40,
                                color= "#a51966")
        
        self.desc = ft.TextField(label="Descrição:")

        self.valor = ft.TextField(label="Valor:")

        self.data = ft.TextField(label="Data:")

        self.botao_salvar = ft.Button(content="Salvar",
                                            width=100,
                                            color="#ffffff",
                                            bgcolor= "#a51966"
                                            )
        self.controls = [titulo,                    
                        self.desc,
                        self.valor,
                        self.data,
                        self.botao_salvar,
                        ]
