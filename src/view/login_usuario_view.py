import flet as ft

class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        
        self.route = "/login"
        
        self.bgcolor = "#facada"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        titulo = ft.Text(value="Faça Login",
                        font_family="Times New Roman",
                        size=40,
                        color= "#a51966")

        self.controls = [titulo]