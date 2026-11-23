import flet as ft
from src.model.despesas_model import Despesas

class VisualizarDespesas(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/visualizar"

        dados_usuario = self.pagina.session.store.get("usuario_logado")
        self.nome_usuario = dados_usuario.get("login")
        
        self.bgcolor = "#facada"

        titulo = ft.Text(value="Suas Despesas!",
                                font_family="Times New Roman",
                                size=40,
                                color= "#a51966")
        
        lista_despesas = []
        
        tabela = ft.DataTable(columns=[ft.DataColumn(label= "ID da categoria"),
                                       ft.DataColumn(label= "Descrição"),
                                       ft.DataColumn(label= "Categora"),
                                       ft.DataColumn(label= "Valor"),
                                       ft.DataColumn(label= "Data"),]

                                       rows= lista_despesas
                                       
                                       )
        
        self.controls = [titulo]