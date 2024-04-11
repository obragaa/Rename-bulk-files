# Importa os módulos shutil e os para operações de arquivo.
import shutil
import os

# Inicializa listas vazias para armazenar operações de renomear e excluir.
rename_operations = []
delete_operations = []

# Define uma função para registrar os detalhes de uma operação em um arquivo de log.
def log_operation(operation_details):
    # Abre o arquivo de log no modo de anexar.
    with open("./logs/rename_log.txt", "a") as log_file:
        # Escreve os detalhes da operação no arquivo de log e adiciona um caractere de nova linha.
        log_file.write(operation_details + "\n")

# Define uma função para imprimir uma prévia das mudanças de renomeação.
def preview_changes(old_name, new_name):
    # Imprime a prévia da operação de renomeação.
    print(f"Visualização: {old_name} -> {new_name}")

# Define uma função para preparar o cancelamento de uma operação de renomeação.
def undo_rename_prepare(old_path, new_path):
    # Adiciona os detalhes da operação de renomeação à lista rename_operations.
    rename_operations.append({'old': old_path, 'new': new_path})

# Define uma função para preparar o cancelamento de uma operação de exclusão.
def undo_delete_prepare(file_path):
    # Cria um caminho de backup acrescentando ".bak" ao caminho do arquivo original.
    backup_path = file_path + ".bak"
    # Copia o arquivo original para o caminho de backup.
    shutil.copy(file_path, backup_path)
    # Adiciona os detalhes da operação de exclusão à lista delete_operations.
    delete_operations.append({'original': file_path, 'backup': backup_path})

# Define uma função para desfazer a última operação de renomeação.
def undo_last_rename():
    # Verifica se há operações de renomeação para desfazer.
    if rename_operations:
        # Retira a última operação de renomeação da lista rename_operations.
        last_operation = rename_operations.pop()
        # Renomeia o novo arquivo de volta para o nome original.
        os.rename(last_operation['new'], last_operation['old'])
        # Registra os detalhes da operação de renomeação desfeita.
        log_operation(f"Renomeação desfeita: {last_operation['new']} -> {last_operation['old']}")

# Define uma função para restaurar arquivos que foram previamente excluídos.
def restore_files():
    # Verifica se há operações de exclusão para restaurar.
    if delete_operations:
        # Retira a última operação de exclusão da lista delete_operations.
        last_operation = delete_operations.pop()
        # Move o arquivo de backup de volta para sua localização original.
        shutil.move(last_operation['backup'], last_operation['original'])
        # Registra os detalhes do arquivo restaurado.
        log_operation(f"Arquivo restaurado: {last_operation['original']}")
