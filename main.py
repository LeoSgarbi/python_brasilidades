from acesso_cep import BuscaEndereco

cep = "01303060"
objeto_cep = BuscaEndereco(cep)
#print(objeto_cep)

bairro, cidade, uf = objeto_cep.acesso_via_cep()
print(bairro, cidade, uf)
