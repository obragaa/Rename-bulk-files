import os
from .utils import log_operation, preview_changes, undo_rename_prepare, undo_delete_prepare

def rename_files(path, prefix="novo_", preview=False):
    """
    Renomeia arquivos em um diretório especificado.

    Args:
        path (str): Caminho para o diretório contendo os arquivos a serem renomeados.
        prefix (str): Prefixo a ser adicionado ao nome de cada arquivo. Padrão é 'novo_'.
        preview (bool): Se True, mostra o que seria renomeado sem realizar a operação. Padrão é False.
    """
    # Itera sobre cada arquivo no diretório especificado
    for filename in os.listdir(path):
        new_name = prefix + filename  # Novo nome do arquivo com o prefixo adicionado
        old_path = os.path.join(path, filename)  # Caminho atual do arquivo
        new_path = os.path.join(path, new_name)  # Novo caminho do arquivo após a renomeação

        if preview:
            # Se preview é True, mostra a previsão da renomeação sem alterar os arquivos
            preview_changes(old_path, new_path)
        else:
            # Renomeia o arquivo e registra a operação
            os.rename(old_path, new_path)
            log_operation(f"Renamed {old_path} to {new_path}")
            undo_rename_prepare(old_path, new_path)  # Prepara a possibilidade de desfazer a operação

def delete_files(path, preview=False):
    """
    Exclui arquivos em um diretório especificado.

    Args:
        path (str): Caminho para o diretório contendo os arquivos a serem excluídos.
        preview (bool): Se True, mostra os arquivos que seriam excluídos sem realizar a operação. Padrão é False.
    """
    # Itera sobre cada arquivo no diretório especificado
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)  # Caminho do arquivo a ser excluído

        if preview:
            # Se preview é True, mostra a previsão da exclusão sem remover os arquivos
            print(f"File to be deleted: {file_path}")
        else:
            # Faz backup do arquivo antes da exclusão, exclui o arquivo e registra a operação
            undo_delete_prepare(file_path)  # Backup antes da exclusão
            os.remove(file_path)
            log_operation(f"Deleted {file_path}")
