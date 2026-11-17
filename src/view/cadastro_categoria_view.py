import flet as ft
from src.model.categorias_model import Categoria

class CadastroCategoriaView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        
        self.route = "/cadastro_cat"
        
        self.bgcolor = "#facada"
        self.titulo = ft.Text(value="Cadastrar Categoria",
                                font_family="Times New Roman",
                                size=30,
                                color= "#a51966")

        self.texto01 = ft.Text(value="Categorias Cadastradas:",
                                        font_family="Times New Roman",
                                        size=30,
                                        color= "#a51966")

        self.botao_salvar = ft.Button(content="Salvar",
                                            width=100,
                                            color="#ffffff",
                                            bgcolor= "#a51966",
                                            on_click= self.adicionar
                                            )

        self.nome_cat = ft.TextField(label="Nome da Categoria")

        self.historico = []
        self.coluna = ft.Column(controls = self.historico)
        
        self.controls = [self.titulo,
                         self.nome_cat,
                         self.botao_salvar,
                         self.texto01,
                         self.coluna
                        ]

    def adicionar(self):
        dados_usuario = self.pagina.session.store.get("usuario_logado")
        nome_usuario = dados_usuario.get("login")
        categoria = self.nome_cat.value
        resultado = Categoria().adicionar(categoria,nome_usuario)

        if resultado:
            self.historico.append(ft.Text(value = f"{categoria}",
                                          color = "#ffffff",
                                          size = 25))
            self.page.show_dialog(ft.SnackBar(ft.Text("Categoria cadastrada com sucesso!"),
                                        bgcolor="#1f992a"))
            self.pagina.update()