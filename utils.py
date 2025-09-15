def boas_vindas(nome: str) -> str:
    """
    Retorna uma mensagem de boas-vindas personalizada.
    """
    if not nome.strip():
        return "Olá, visitante!"
    return f"Olá, {nome}! Bem-vindo ao projeto DevOps 🚀 Esse é um teste."