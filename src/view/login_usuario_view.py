import flet as ft
from src.model.usuario_model import Usuario

class LoginUsuarioView(ft.View):
    def __init__(self, pagina:ft.Page):
        super().__init__()

        self.pagina = pagina
        
        self.route = "/login"
        
        self.bgcolor = "#facada"
        self.vertical_alignment = "CENTER"
        self.horizontal_alignment = "CENTER"

        titulo = ft.Text(value="Faça Login",
                        font_family="Times New Roman",
                        size=40,
                        color= "#a51966")
        
        titulo02 = ft.Text(value="Bem Vindo!",
                                        font_family="Times New Roman",
                                        size=20,
                                        color= "#a51966")

        self.campo_usuario = ft.TextField(label= "Usuário")
        self.campo_senha = ft.TextField(label="Senha",
                                           password= True,
                                           can_reveal_password=True)

        botao_login = ft.Button(content="Entrar",
                                            width=150,
                                            color="#ffffff",
                                            bgcolor= "#a51966",
                                            on_click= self.Login
                                            )

        texto01 = ft.Text(value="Ainda não tem uma conta?",
                                font_family="Times New Roman",
                                color= "#a51966")

        botao_cadastro = ft.Button(content="Se Cadastre!",
                                            width=150,
                                            color="#ffffff",
                                            bgcolor= "#a51966",
                                            on_click=self.cadastro
                                            )

        self.controls = [titulo,
                         titulo02,
                         self.campo_usuario,
                         self.campo_senha,
                         botao_login,
                         texto01,
                         botao_cadastro]

    def Login(self):
            usuario = self.campo_usuario.value
            senha = self.campo_senha.value
    
            resultado = Usuario().Verificar(usuario,senha)
    
            if resultado :  
                #função para ir para a página principal
                self.page.show_dialog(ft.SnackBar(ft.Text("Login realizado!"),
                                        bgcolor="#1f992a"))
                self.pagina.navigate("/cadastro_cat")
                                                   
            else:
                self.page.show_dialog(ft.SnackBar(ft.Text("Usuário ou senha incorreta!"),
                                                  bgcolor="#b91414"))

    async def cadastro(self):
        await self.pagina.push_route("/cadastro")


    

    