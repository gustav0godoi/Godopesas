import flet as ft

class Principal(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        
        self.route = "/principal"

        dados_usuario = pagina.session.get("usuario_logado")
        nome_usuario = dados_usuario.get("usuario")
        
        self.bgcolor = "#facada"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        titulo = ft.Text(value=f"Seja bem vindo(a) {nome_usuario}",
                                font_family="Times New Roman",
                                size=20,
                                color= "#a51966")



        
        self.controls = [titulo,
                        ]

        