from src.database.conexao import Conexao



class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def adicionar(categoria:str, login:str) -> int:
            conexao, cursor = Conexao().conectar()
            if not conexao:
                    print("Erro ao tentar conectar!")
                    return False
            
            try:
                cursor.execute("""
                                INSERT INTO tb_categorias (nome, login)
                                VALUES (%s, %s);
                                """,
                                [categoria, login])
                id_categorias = cursor.lastrowid
                conexao.commit()
                conexao.close()

                return id_categorias
            except Exception as e:
                print(f"ERRO AO INSERIR {e}")
                return False

    @staticmethod        
    def excluir(id_categoria:int) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao tentar conectar!")
            return False
          
        try:
            cursor.execute("""
                            DELETE FROM tb_categorias
                            WHERE id_categoria = %s;
                            """,
                            
                            [id_categoria])
            conexao.commit()
            conexao.close()

            return True

        except Exception as e:
            print(f"ERRO AO INSERIR {e}")
            return False
        
    @staticmethod
    def recuperar (login:str) -> list:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao tentar conectar!")
            return False

        
        cursor.execute("""
                SELECT nome, login, id_categoria FROM tb_categorias
                WHERE login = %s;
                """,
                
                [login])
        
        resultado = cursor.fetchall()
        conexao.close()

        return resultado

            