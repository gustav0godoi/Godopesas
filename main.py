import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.cadastro_categoria_view import CadastroCategoriaView

def main(pagina:ft.Page):
    pagina.window.width = 600
    pagina.window.height = 700
    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)
    tela_cadastro_categoria = CadastroCategoriaView(pagina)

    def roteamento(e=None):
        pagina.views.clear()

        if pagina.route == "/cadastro":
            pagina.views.append(tela_cadastro_usuario)
        elif pagina.route == "/login":
            pagina.views.append(tela_login_usuario)
        elif pagina.route == "/cadastro_cat":
            pagina.views.append(tela_cadastro_categoria)

        pagina.update()

    #associando a função de rotemaneto para sempre que houver uma toca de tela, esta função será chamada
    pagina.on_route_change = roteamento
    roteamento()

    #Abrindo a página inicial
    pagina.views.append(tela_cadastro_usuario)
    
ft.run(main)