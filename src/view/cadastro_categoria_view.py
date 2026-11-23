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

        self.lista_categorias = []
        self.coluna = ft.Column(controls = self.lista_categorias)
        
        self.controls = [self.titulo,
                         self.nome_cat,
                         self.botao_salvar,
                         self.texto01,
                         self.coluna
                        ]

    def adicionar(self, e):
        dados_usuario = self.pagina.session.store.get("usuario_logado")
        nome_usuario = dados_usuario.get("login")
        categoria = self.nome_cat.value
        id_categoria = Categoria.adicionar(categoria, nome_usuario)

        if id_categoria:
            texto = ft.Text(value=f"{categoria}", color="#ffffff", size=20)
            historico = ft.Row(alignment=ft.MainAxisAlignment.CENTER)
            
            excluir = ft.FloatingActionButton(
                icon=ft.Icons.DELETE_OUTLINE_ROUNDED,
                foreground_color="#ffffff",
                bgcolor = "#a51966",
                width=50,
                height=35,
                on_click=lambda e, id_cat=id_categoria, row=historico: self.excluir(e, id_cat, row)
            )
            
            historico.controls = [texto, excluir]
            self.lista_categorias.append(historico)

            self.page.show_dialog(ft.SnackBar(ft.Text("Categoria cadastrada com sucesso!"),
                                        bgcolor="#1f992a"))
            self.pagina.update()

    def excluir(self, e, id_categoria, linha):
        resultado = Categoria.excluir(id_categoria)
        
        if resultado:
            self.lista_categorias.remove(linha)
            self.pagina.update()

    def atualizar_lista_categorias(self):
        dados_usuario = self.pagina.session.store.get("usuario_logado")
        nome_usuario = dados_usuario.get("login")
        categorias = Categoria.recuperar(nome_usuario)

        for categoria in categorias:
            nome_categoria = categoria.get("nome")
            delete = ft.FloatingActionButton(
                icon=ft.Icons.DELETE_OUTLINE_ROUNDED,
                foreground_color="#ffffff",
                bgcolor = "#a51966",
                width=50, 
                height=35,
                key= categoria.get("id_categoria"))
            
            texto = ft.Text(value=nome_categoria, color="#ffffff")
            historico = ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                               controls=[texto, delete])
            
        
            
            historico.controls = [texto, delete]
            self.lista_categorias.append(historico)

        self.pagina.update()

    def excluir_categoria(self,botao):
        id_categoria = botao.control.key
        Categoria().excluir(id_categoria)
        self.atualizar_lista_categorias