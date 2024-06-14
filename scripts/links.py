import datetime

def Atualiza_Parametros():
    # Abre o arquivo
    with open('Criar_URL.txt', 'r', encoding='utf-8') as arquivo:
        # Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

    # Cria um dicionário para armazenar as variáveis
    variaveis = {}

    # Itera sobre cada linha do arquivo
    for linha in linhas:
        # Separa o nome da variável e seu valor
        nome, valor = linha.strip().split(' = ')
        # Armazena a variável no dicionário
        valor = valor.replace(" ", "%20").replace("'", "")
        variaveis[nome] = valor

    query = variaveis['Busca']

    inicio = variaveis['Inicio']
    start_date = datetime.datetime.strptime(inicio, '%d-%m-%Y')
    end_date = start_date + datetime.timedelta(days=1)

    fim = variaveis['Final']
    finish_date = datetime.datetime.strptime(fim, '%d-%m-%Y')

    # Lista para armazenar as URLs
    urls = []

    # Loop através de cada dia em 2023
    current_date = start_date

    while end_date != finish_date:
        # Formate a data no formato yyyy-mm-dd
        formatted_date = current_date.strftime("%Y-%m-%d")
        formatted_end_date = end_date.strftime("%Y-%m-%d")
        
        # Crie a URL para o dia atual
        url = f"https://twitter.com/search?q={query}%20lang%3Apt%20until%3A{formatted_end_date}%20since%3A{formatted_date}%20-filter%3Areplies&src=typed_query&f=live"
        # url = f"https://twitter.com/search?q="gostei%20dessa%20propaganda"%20OR%20"gostei%20da%20propaganda"%20lang%3Apt%20until%3A{formatted_end_date}%20since%3A{formatted_date}%20-filter%3Areplies&src=typed_query"        # Adicione a URL à lista de URLs
        
        # Adicione a URL à lista de URLs
        urls.append(url)
        
        # Avance para o próximo dia
        current_date += datetime.timedelta(days=1)
        end_date += datetime.timedelta(days=1)

    # Imprima as URLs geradas
    for url in urls:
        open("files/URLs.txt", "w").write("\n".join(urls))