import json
import os

pessoa = {}

try:
    arquivo = input("Informe o arquivo: ").strip().lower()
    
    # Lê os dados existentes
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        pessoas = json.load(f)
    
    # Coleta os dados da nova pessoa
    pessoa['nome'] = input("Informe o nome: ").strip().title()
    pessoa['idade'] = int(input("Informe a idade: "))
    pessoa['cpf'] = input("Informe o CPF: ").strip()
    pessoa['rg'] = input("Informe o RG: ").strip()
    pessoa['data_nasc'] = input("Informe data de nascimento: ").strip()
    pessoa['sexo'] = input("Informe o gênero: ").strip()
    pessoa['signo'] = input("Informe o signo: ").strip().capitalize()
    pessoa['mae'] = input("Informe o nome da mãe: ").strip().title()
    pessoa['pai'] = input("Informe o nome do pai: ").strip().title()
    pessoa['email'] = input("Informe o e-mail: ").strip().lower()
    pessoa['senha'] = input("Informe a senha: ")
    pessoa['cep'] = input("Informe o CEP: ").strip()
    pessoa['endereco'] = input("Informe o endereço: ").strip().title()
    pessoa['numero'] = int(input("Informe o número do endereço: "))
    pessoa['bairro'] = input("Informe o bairro: ").strip().capitalize()
    pessoa['cidade'] = input("Informe a cidade: ").strip().title()
    pessoa['estado'] = input("Informe o estado: ").strip().upper()
    pessoa['telefone_fixo'] = input("Informe o telefone: ").strip()
    pessoa['celular'] = input("Informe o celular: ").strip()
    pessoa['altura'] = float(input("Informe a altura: ").replace(",", "."))
    pessoa['peso'] = float(input("Informe o peso: ").replace(",", "."))
    pessoa['tipo_sanguineo'] = input("Informe o tipo sanguíneo: ").strip().capitalize()
    pessoa['cor'] = input("Informe a cor favorita: ").strip()

    # Adiciona a nova pessoa e salva no JSON
    pessoas.append(pessoa)

    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(pessoas, f, ensure_ascii=False, indent=4)

    # Exibe a lista atualizada de pessoas
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        pessoas = json.load(f)
    
    print(f"{'-'*20} LISTA DE PESSOAS {'-'*20}")
    for pessoa in pessoas:
        for chave in pessoa:
            print(f"{chave.capitalize()}: {pessoa.get(chave)}")
        print('-'*40)

except Exception as e:
    print(f"Não foi possível inserir pessoa. {e}.")