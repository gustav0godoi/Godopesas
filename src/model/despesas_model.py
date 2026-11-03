from src.database.conexao import Conexao

class Despesas:
    def __init__(self):
        pass

    @staticmethod
    def incluir(login: str, id_categoria: int, descricao: str, valor: float, dt_cadastro: str) -> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao tentar conectar!")
            return False

        try:
            cursor.execute("""
                INSERT INTO tb_despesas (login, id_categoria, descricao, valor, dt_cadastro)
                VALUES (%s, %s, %s, %s, %s);
            """, [login, id_categoria, descricao, valor, dt_cadastro])
            
            id_despesas = cursor.lastrowid
            conexao.commit()
            conexao.close()

            return id_despesas
        except Exception as e:
            print(f"ERRO AO INSERIR: {e}")
            return False

    @staticmethod
    def recuperar_todos(login: str) -> list:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao tentar conectar!")
            return False

        try:
            cursor.execute("""
                SELECT id_despesas, login, id_categoria, descricao, valor, dt_cadastro
                FROM tb_despesas
                WHERE login = %s;
            """, [login])

            despesas = cursor.fetchall()
            conexao.close()

            return despesas
        except Exception as e:
            print(f"ERRO AO RECUPERAR TODOS: {e}")
            return False

    @staticmethod
    def recuperar_categoria(login: str, id_categoria: int) -> list:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao tentar conectar!")
            return False

        try:
            cursor.execute("""
                SELECT id_despesas, login, valor, dt_cadastro, descricao, id_categoria
                FROM tb_despesas
                WHERE login = %s
                AND id_categoria = %s;
            """, [login, id_categoria])

            despesas = cursor.fetchall()
            conexao.close()

            return despesas
        except Exception as e:
            print(f"ERRO AO RECUPERAR CATEGORIA: {e}")
            return False

    @staticmethod
    def excluir(id_despesas: int) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao tentar conectar!")
            return False

        try:
            cursor.execute("""
                DELETE FROM tb_despesas
                WHERE id_despesas = %s;
            """, [id_despesas])

            conexao.commit()
            conexao.close()

            return True
        except Exception as e:
            print(f"ERRO AO EXCLUIR: {e}")
            return False

    @staticmethod
    def alterar(id_despesas: int, login: str, id_categoria: int, descricao: str, valor: float, dt_cadastro: str) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("Erro ao tentar conectar!")
            return False

        try:
            cursor.execute("""
                UPDATE tb_despesas SET
                    id_categoria = %s,
                    descricao = %s,
                    valor = %s,
                    dt_cadastro = %s
                WHERE
                    id_despesas = %s
                    AND login = %s;
            """, [id_categoria, descricao, valor, dt_cadastro, id_despesas, login])

            conexao.commit()
            conexao.close()

            return True
        except Exception as e:
            print(f"ERRO AO ALTERAR: {e}")
            return False