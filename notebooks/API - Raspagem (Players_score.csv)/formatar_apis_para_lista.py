# Abre o arquivo 'unique_urls777.txt' que contém os links das APIs, uma por linha
with open('unique_urls777.txt', 'r') as file:
    apis = file.readlines()  # Lê todas as linhas do arquivo, cada linha contendo uma URL

# Processa cada linha para remover caracteres como quebras de linha e adiciona aspas em volta de cada URL
formatted_apis = ['"' + api.strip() + '"' for api in apis]

# Junta todos os links formatados em uma única string, separando-os por vírgulas e espaços
result = ', '.join(formatted_apis)

# Exibe a string formatada com as APIs, pronta para ser usada ou copiada
print(result)
