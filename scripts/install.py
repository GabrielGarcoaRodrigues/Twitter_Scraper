# import subprocess
# import sys
# import importlib.util
# import venv  # Importando o módulo venv para criar o ambiente virtual
# import os
# def check_and_install_package(package_name):
#     """
#     Verifica se o pacote está instalado e, se não estiver, o instala.
#     """
#     spec = importlib.util.find_spec(package_name)
#     if spec is None:
#         try:
#             subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
#             print(f"{package_name} foi instalado com sucesso.")
#         except subprocess.CalledProcessError:
#             print(f"Erro ao instalar {package_name}. Verifique sua conexão com a internet ou tente novamente mais tarde.")

# # Lista de bibliotecas que você deseja verificar e instalar (se necessário)
# bibliotecas_necessarias = ["selenium", "termcolor", "chromedriver_autoinstaller", "xlwt", "openpyxl"]

# # Verifica e instala as bibliotecas
# for biblioteca in bibliotecas_necessarias:
#     check_and_install_package(biblioteca)

# # Agora você pode usar as bibliotecas normalmente em seu código!
import subprocess
import sys
import os

def check_and_install_packages(requirements_file):
    """
    Verifica se os pacotes especificados no arquivo requirements.txt estão instalados
    e os instala se necessário.
    """
    # Verifica o caminho absoluto do diretório atual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Concatena o caminho absoluto com o nome do arquivo requirements.txt
    requirements_path = os.path.join(current_dir, requirements_file)

    # Verifica se o arquivo requirements.txt existe
    if not os.path.exists(requirements_path):
        print(f"O arquivo de requisitos '{requirements_file}' não foi encontrado.")
        return
    
    # Tenta instalar os pacotes listados no arquivo requirements.txt
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        print("As dependências foram instaladas com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar as dependências: {e}")

# Nome do arquivo requirements.txt
requirements_file = "requirements.txt"

# Verifica e instala os pacotes
check_and_install_packages(requirements_file)


