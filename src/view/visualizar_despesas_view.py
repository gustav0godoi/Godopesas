import flet as ft
from src.model.despesas_model import Despesas

class VisualizarDespesas(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        self.route = "/visualizar"

        dados_usuario = self.pagina.session.store.get("usuario_logado")
        self.nome_usuario = dados_usuario.get("login")
        
        self.bgcolor = "#87CEFA"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        titulo = ft.Text(value="Suas Despesas!",
                                font_family="Times New Roman",
                                size=40,
                                color= "#6495ED")
        
        self.lista_despesas = []
        
        tabela = ft.DataTable(columns=[ft.DataColumn(label="ID da categoria"),
                                       ft.DataColumn(label="Descrição"),
                                       ft.DataColumn(label="Categoria"),
                                       ft.DataColumn(label="Valor"),
                                       ft.DataColumn(label="Data")],

                                       rows= self.lista_despesas)

        self.atualizar_despesas()

        self.controls = [titulo, tabela]

    def atualizar_despesas(self):
            despesas = Despesas().recuperar_todos(self.nome_usuario)


            for despesa in despesas:
                id_despesa = str(despesa.get("id_despesas"))
                desc = str(despesa.get("descricao"))
                valor = str(despesa.get("valor"))
                categoria = str(despesa.get("nome"))
                data = str(despesa.get("dt_cadastro"))
                

                linha = ft.DataRow(
                    color="#ADD8E6",
                    cells=[
                        ft.DataCell(ft.Text(id_despesa)),
                        ft.DataCell(ft.Text(desc)),
                        ft.DataCell(ft.Text(categoria)),
                        ft.DataCell(ft.Text(valor)),
                        ft.DataCell(ft.Text(data)),
                    ]
                )

                self.lista_despesas.append(linha)

            self.pagina.update()