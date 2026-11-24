import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.cadastro_categoria_view import CadastroCategoriaView
from src.view.visualizar_despesas_view import VisualizarDespesas
from src.view.cadastro_despesa_view import CadastroDespesaView
from src.view.principal_view import Principal
from src.view.despesas_categoria_view import DespesasCat

def main(pagina: ft.Page):
    pagina.window.width = 900
    pagina.window.height = 800

    pagina.theme = ft.Theme(
    navigation_bar_theme=ft.NavigationBarTheme(
        label_text_style={
            ft.ControlState.DEFAULT: ft.TextStyle(
                color="#ffffff",
                size=12,
                weight=ft.FontWeight.BOLD
            ),
            ft.ControlState.SELECTED: ft.TextStyle(
                color="#FFFFFF",
                size=12,
                weight=ft.FontWeight.BOLD
            ),
        },
    )
)


    def navegacao(e):
        item_clicado = e.control.selected_index     
        if item_clicado == 0:
            pagina.navigate("/principal")
        if item_clicado == 1:
            pagina.navigate("/cadastro_cat")
        elif item_clicado == 2:
            pagina.navigate("/cadastro_desp")
        elif item_clicado == 3:
            pagina.navigate("/visualizar")
        elif item_clicado == 4:
            pagina.navigate("/despesas_cat")
        elif item_clicado == 5:
            pagina.navigate("/login")

    barra_navegacao = ft.NavigationBar(
    bgcolor="#34495E",
    indicator_color="#34495E",
    destinations=[
        ft.NavigationBarDestination(
            icon=ft.Icon(ft.Icons.HOME_OUTLINED, color="#87CEFA"),
            label="Início"
        ),
        ft.NavigationBarDestination(
            icon=ft.Icon(ft.Icons.CIRCLE, color="#87CEFA"),
            label="Categoria"
        ),
        ft.NavigationBarDestination(
            icon=ft.Icon(ft.Icons.ADD_BOX_OUTLINED, color="#87CEFA"),
            label="Adicionar Despesas"
        ),
        ft.NavigationBarDestination(
            icon=ft.Icon(ft.Icons.DONE_ALL_ROUNDED, color="#87CEFA"),
            label="Todas as Despesas"
        ),
        ft.NavigationBarDestination(
            icon=ft.Icon(ft.Icons.EXPLORE, color="#87CEFA"),
            label="Despesas por Categoria"
        ),
        ft.NavigationBarDestination(
            icon=ft.Icon(ft.Icons.EXIT_TO_APP, color="#87CEFA"),
            label="Sair"
        ),
    ],

    on_change=navegacao
)

    def roteamento(e=None):
        pagina.views.clear()

       
        if pagina.route == "/login":
            tela_login_usuario = LoginUsuarioView(pagina)
            pagina.views.append(tela_login_usuario)
        elif pagina.route == "/cadastro":
            tela_cadastro_usuario = CadastroUsuarioView(pagina)
            pagina.views.append(tela_cadastro_usuario)
        elif pagina.route == "/cadastro_cat":
            tela_cadastro_categoria = CadastroCategoriaView(pagina)
            tela_cadastro_categoria.navigation_bar = barra_navegacao
            pagina.views.append(tela_cadastro_categoria)
        elif pagina.route == "/visualizar":
            tela_visualizar_despesas = VisualizarDespesas(pagina)
            tela_visualizar_despesas.navigation_bar = barra_navegacao
            pagina.views.append(tela_visualizar_despesas)
        elif pagina.route == "/cadastro_desp":
            tela_cadastro_despesa = CadastroDespesaView(pagina)
            tela_cadastro_despesa.navigation_bar = barra_navegacao
            pagina.views.append(tela_cadastro_despesa)
        elif pagina.route == "/principal":
            tela_principal = Principal(pagina)
            tela_principal.navigation_bar = barra_navegacao
            pagina.views.append(tela_principal)
        elif pagina.route == "/despesas_cat":
            despesas_cat = DespesasCat(pagina)
            despesas_cat.navigation_bar = barra_navegacao
            pagina.views.append(despesas_cat)

        pagina.update()

    # Associa a função de roteamento ao evento de mudança de rota
    pagina.on_route_change = roteamento
    roteamento()
    
    
    pagina.navigate("/login")

ft.run(main)