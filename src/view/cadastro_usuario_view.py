import flet as ft

class CadastroUsuarioView(ft.View):
    def __init__(self, pg:ft.Page):
        super().__init__()

    def main(page:ft.Page):
        page.title = "GodoPesas!!"
        page.bgcolor = "#FFFFFF" 
        page.window.height = 700 
        page.window.width = 800 
        page.horizontal_alignment = "center"

        titulo = ft.Text(value = "Cadastro do Usuário",
                        size=40,
                        font_family= "Times New Roman",
                        color= "#000000")


        page.controls = [titulo               
                     ]
        page.update()
    ft.run(main)