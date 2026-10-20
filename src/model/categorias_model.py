from src.database.conexao import Conexao



class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(categoria:str) -> bool:
            conexao, cursor = Conexao().conectar()
            if not conexao:
                    print("Erro ao tentar conectar!")
                    return False
            try:
                cursor.execute("""
                                INSERT INTO tb_usuarios(categoria)
                                VALUES (%s)
                                """,
                                [categoria])
                conexao.commit()
                conexao.close()

                return True
            except Exception as e:
                 print(f"ERRO AO INSERIR {e}")
                 return False