from src.model.despesas_model import Despesas

resultado = Despesas().alterar("1", "Felizberta", "1", "Transporte", "10.30", "01/11/2026")
print(resultado)