cidade=["joivile","blumenau","curitiba","lages","florianopolis"]
print("lista original")
print(cidade)

cidade.insert(2,"joão Pessoa")

nova=input("digite a nova cidade: ")
cidade[1]=nova
print('\nLista atualizada:')
print(cidade)
