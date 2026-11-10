import flet as ft

class VisualizarDespesas(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        
        self.route = "/visualizar"
        
        self.bgcolor = "#facada"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        titulo = ft.Text(value="Suas Despesas!",
                                font_family="Times New Roman",
                                size=40,
                                color= "#a51966")



        
        self.controls = [titulo,
                        ]

        