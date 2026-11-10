import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.cadastro_categoria_view import CadastroCategoriaView

def main(pagina:ft.Page):
    pagina.window.width = 600
    pagina.window.height = 700

    def navegacao(e):
        item_clicado = e.control.selected_index
        if item_clicado == 0:
            pagina.navigate("/categoria")
        elif item_clicado == 1:
            pagina.navigate("/")
        elif item_clicado == 2:
            pagina.navigate("/")
        elif item_clicado == 3:
            pagina.navigate("/")
        elif item_clicado == 4:
            pagina.navigate("/")

    barra_navegacao = ft.NavigationBar(destinations=[
                                        ft.NavigationBarDestination(icon =ft.Icons.CIRCLE, label = "Categoria"),
                                        ft.NavigationBarDestination(icon =ft.Icons.ADD_BOX_OUTLINED, label = "Adicionar Despesas"),
                                        ft.NavigationBarDestination(icon =ft.Icons.DONE_ALL_ROUNDED, label = "Todas as Despesas"),
                                        ft.NavigationBarDestination(icon =ft.Icons.EXPLORE, label = "Despesas por Categoria"),],
                                        on_change = navegacao
    )

    tela_cadastro_usuario = CadastroUsuarioView(pagina)
    tela_login_usuario = LoginUsuarioView(pagina)
    tela_cadastro_categoria = CadastroCategoriaView(pagina)
    tela_cadastro_categoria.navigation_bar = barra_navegacao

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