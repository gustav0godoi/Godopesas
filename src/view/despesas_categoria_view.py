import flet as ft
from src.model.categorias_model import Categoria
from src.model.despesas_model import Despesas

class DespesasCat(ft.View):
    def __init__(self, pagina: ft.Page):
        super().__init__()

        self.pagina = pagina
        self.route = "/despesas_cat"
        
        self.bgcolor = "#87CEFA"
        self.horizontal_alignment = "CENTER"
        dados_usuario = self.pagina.session.store.get("usuario_logado")
        self.nome_usuario = dados_usuario.get("login")


        titulo = ft.Text(
            value="Despesas com base nas categorias:",
            font_family="Times New Roman",
            size=20,
            color="#6495ED"
        )

        self.controls = [titulo]




        opcoes_categoria = []

        categorias = Categoria().recuperar(self.nome_usuario)
        
        for categoria in categorias:
                opcoes = ft.DropdownOption(key=categoria.get("id_categoria",
                                            text =categoria.get("nome")))
                opcoes_categoria.append(opcoes)
        
        self.campo_categoria = ft.Dropdown(options=opcoes_categoria)
        
        self.lista_despesas = []
        
        tabela = ft.DataTable(
            heading_text_style=ft.TextStyle(
                color="#FFFFFF",
                weight=ft.FontWeight.BOLD,
                size=17,
                font_family="Times New Roman"
            ),
            columns=[
                ft.DataColumn(label=ft.Text("ID da categoria")),
                ft.DataColumn(label=ft.Text("Descrição")),
                ft.DataColumn(label=ft.Text("Categoria")),
                ft.DataColumn(label=ft.Text("Valor")),
                ft.DataColumn(label=ft.Text("Data")),
                ft.DataColumn(label=ft.Text("Excluir"))
            ],

            rows=self.lista_despesas
            )

        self.atualizar_despesas()

        self.controls = [titulo,  self.campo_categoria, tabela,]

    def atualizar_despesas(self):
            self.lista_despesas.clear()
            despesas = Despesas().recuperar_todos(self.nome_usuario)


            for despesa in despesas:
                id_despesa = str(despesa.get("id_despesas"))
                desc = str(despesa.get("descricao"))
                categoria = str(despesa.get("nome"))
                valor = str(despesa.get("valor"))
                data = str(despesa.get("dt_cadastro"))
                

                linha = ft.DataRow(
                        color="#ADD8E6",
                        cells=[
                            ft.DataCell(ft.Text(id_despesa, color="#6495ED")),
                            ft.DataCell(ft.Text(desc, color="#6495ED")),
                            ft.DataCell(ft.Text(categoria, color="#6495ED")),
                            ft.DataCell(ft.Text(valor, color="#6495ED")),
                            ft.DataCell(ft.Text(data, color="#6495ED")),
                            ft.DataCell(ft.IconButton(icon=ft.Icons.DELETE,
                                                    key=id_despesa,
                                                    on_click=self.excluir_despesa))
                        ]
                    )
                                            

                self.lista_despesas.append(linha)

            self.pagina.update()


    def excluir_despesa(self, botao):
        id_despesa = botao.control.key
        Despesas().excluir(id_despesa)
        self.atualizar_despesas()