import flet as ft
from datetime import datetime
from src.model.categorias_model import Categoria
from src.model.despesas_model import Despesas


class CadastroDespesaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina

        
        self.route = "/cadastro_desp"
        
        self.bgcolor = "#87CEFA"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        dados_usuario = self.pagina.session.store.get("usuario_logado")
        self.nome_usuario = dados_usuario.get("login")

        titulo = ft.Text(value="Cadastre a suas despesas aqui!",
                                font_family="Times New Roman",
                                size=40,
                                color= "#6495ED")
        
        self.campo_desc = ft.TextField(label="Descrição:",
                                       border_color= "#6495ED",
                                       color="#FFFFFF")

        self.campo_valor = ft.TextField(label="Valor:",
                                  keyboard_type=ft.KeyboardType.NUMBER,
                                  border_color= "#6495ED",
                                  color="#FFFFFF")

        self.campo_data = ft.TextField(label="Data:",
                                keyboard_type=ft.KeyboardType.NUMBER,
                                border_color= "#6495ED",
                                color="#FFFFFF")
        
        categorias = Categoria().recuperar(self.nome_usuario)

        opcoes = []

        for categoria in categorias:
            id_categoria = categoria.get("id_categoria")
            opcoes.append(ft.DropdownOption(key = id_categoria,
                                            text =categoria.get("nome")))

        self.campo_categoria = ft.Dropdown(options=opcoes)

        self.botao_salvar = ft.Button(content="Salvar",
                                            width=100,
                                            color="#ffffff",
                                            bgcolor= "#6495ED",
                                            on_click=self.incluir
                                            )
        
        self.controls = [titulo,                    
                        self.campo_desc,
                        self.campo_valor,
                        self.campo_data,
                        self.campo_categoria,
                        self.botao_salvar
                        ]
        
    def incluir(self):
        valor = self.campo_valor.value
        descricao = self.campo_desc.value
        data = self.campo_data.value
        categoria = self.campo_categoria.value
        data_convert = datetime.strptime(data, "%d/%m/%Y")
        
        resultado = Despesas().incluir(self.nome_usuario, categoria, descricao, valor, data_convert)

        if resultado:
            self.page.show_dialog(ft.SnackBar(ft.Text("Despesa cadastrada com sucesso!"),
                                        bgcolor="#1f992a"))
            
        else:
                self.page.show_dialog(ft.SnackBar(ft.Text("Erro ao cadastras a despesa!"),
                                                  bgcolor="#b91414"))