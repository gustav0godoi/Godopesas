import flet as ft

class DespesasCat(ft.View):
    def __init__(self, pagina: ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/despesas_cat"
        
        self.bgcolor = "#87CEFA"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"


        titulo = ft.Text(
            value="Despesas com base nas categorias:",
            font_family="Times New Roman",
            size=20,
            color="#6495ED"
        )

        self.controls = [titulo]