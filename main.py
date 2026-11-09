import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView

def main(pagina:ft.Page):
    pagina.window.width = 600
    pagina.window.height = 700
    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    pagina.views.append(tela_cadastro_usuario)

ft.run(main)