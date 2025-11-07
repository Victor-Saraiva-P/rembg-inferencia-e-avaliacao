import os


def lista_arquivos(diretorio):
    modelos = []

    # Lista todos os arquivos no diretório de modelos
    for arquivo_modelo in os.listdir(diretorio):
        # Verifica se é um arquivo (não um diretório)
        caminho_completo = os.path.join(diretorio, arquivo_modelo)
        if os.path.isfile(caminho_completo):
            modelos.append(arquivo_modelo)

    return modelos
