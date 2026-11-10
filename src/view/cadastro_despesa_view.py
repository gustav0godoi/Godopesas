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



        
        self.controls = [titulo,
                        ]
