# Importa as funções rename_files e delete_files do módulo operations do pacote renamer.
from renamer.operations import rename_files, delete_files
# Importa as funções undo_last_rename e restore_files do módulo utils do pacote renamer.
from renamer.utils import undo_last_rename, restore_files

# Define a função principal do programa.
def main():
    # Define o caminho para o diretório contendo os arquivos de exemplo.
    path = "./path_example_files"
    
    # Previsualiza as renomeações.
    print("Previsualização das renomeações:")
    rename_files(path, preview=True)
    
    # Previsualiza as deleções.
    print("\nPrevisualização das deleções:")
    delete_files(path, preview=True)
    
    # Para executar as operações, remova o parâmetro 'preview=True' e execute novamente.
    # Lembre-se de usar as funções undo_last_rename e restore_files conforme necessário.

# Verifica se este script está sendo executado como o principal.
if __name__ == "__main__":
    # Chama a função principal.
    main()
