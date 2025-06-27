# dicionário
usuario = {
    'nome': "Alex Machado",
    'idade': 40,
    'email': "alex@gmail.com"
}

# exibir os dados atuais
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# adicionar nova chave fora do laço
usuario['profissão'] = input("Informe a profissão: ").strip()

# separador visual
print("-" * 40)

# exibir os dados atualizados
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")