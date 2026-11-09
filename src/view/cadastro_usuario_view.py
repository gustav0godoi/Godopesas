import flet as ft
from src.model.usuario_model import Usuario

class CadastroUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.bgcolor = "#facada"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        titulo = ft.Text(value="Cadastro de usuario",
                        font_family="Times New Roman",
                        size=40,
                        color= "#a51966")

        self.campo_usuario = ft.TextField(label= "Usuário")
        self.campo_senha = ft.TextField(label="Senha",
                                   password= True,
                                   can_reveal_password=True)

        botao_cadastrar = ft.Button(content="Cadastrar-se",
                                    width=150,
                                    color="#ffffff",
                                    on_click=self.cadastrar,
                                    bgcolor= "#a51966"
                                    )

        botao_voltar = ft.Button(content="Voltar ao Login",
                                    width=150,
                                    color="#FFFFFF",
                                    on_click=self.cadastrar,
                                    bgcolor="#a51966"
                                    )

        self.controls = [titulo,
                         self.campo_usuario,
                         self.campo_senha,
                         botao_cadastrar,
                         botao_voltar]

    def cadastrar(self):
        usuario = self.campo_usuario.value
        senha = self.campo_senha.value

        resultado = Usuario().cadastrar(usuario,senha)

        if resultado == True:
            self.page.show_dialog(ft.SnackBar(ft.Text("Cadastro realizado com sucesso!"),
                                              ))
                                               
        else:
            self.page.show_dialog(ft.SnackBar(ft.Text("Erro ao cadastrar!")))