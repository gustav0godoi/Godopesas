from src.database.conexao import Conexao

class Despesas:
    def __init__(self):
        pass

    @staticmethod
    def incluir(id_categoria:int, descricao:str, valor:float, data:str) -> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao tentar conectar!")
            return False
        

        try:
            cursor.execute("""
                        INSERT INTO tb_despesas (dt_cadastro, valor, descricao, login)
                        VALUES = (%s, %s. %s, %s);
                        """,
                        [id_categoria, descricao, valor, data])
            
            id_despesa = cursor.lastrowid
            cursor.commit()
            cursor.close()

            return id_despesa
        except Exception as e:
                print(f"ERRO AO INSERIR {e}")
                return False

        