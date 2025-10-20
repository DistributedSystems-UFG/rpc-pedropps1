import rpyc
from constRPYC import *

conn = rpyc.connect(SERVER, PORT)
print("Conectado ao servidor RPyC.")
print("="*30)

db_list = conn.root

print("Limpando a lista para um novo começo...")
db_list.exposed_clear()
print(f"Lista inicial: {db_list.exposed_value()}")
print("="*30)

print("Adicionando elementos: 10, 30, 5...")
db_list.exposed_append(10)
db_list.exposed_append(30)
db_list.exposed_append(5)
print(f"Lista após adições: {db_list.exposed_value()}")
print("="*30)

print("Inserindo o elemento '20' no índice 1...")
db_list.exposed_insert(1, 20)
print(f"Lista após inserção: {db_list.exposed_value()}")
print("="*30)

print("Ordenando a lista...")
db_list.exposed_sort()
print(f"Lista ordenada: {db_list.exposed_value()}")
print("="*30)

print("Pesquisando pelo elemento '30' (deve existir)...")
found = db_list.exposed_search(30)
print(f"Resultado da busca por '30': {found}")

print("\nPesquisando pelo elemento '99' (não deve existir)...")
not_found = db_list.exposed_search(99)
print(f"Resultado da busca por '99': {not_found}")
print("="*30)

print("Removendo o elemento '20'...")
was_removed = db_list.exposed_remove(20)
print(f"Remoção bem-sucedida: {was_removed}")
print(f"Lista após remoção: {db_list.exposed_value()}")
print("="*30)

print("Tentando remover o elemento '99' (deve falhar)...")
was_removed_again = db_list.exposed_remove(99)
print(f"Remoção bem-sucedida: {was_removed_again}")
print(f"Lista final: {db_list.exposed_value()}")
print("="*30)

conn.close()
print("Conexão fechada.")
