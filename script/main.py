from config import MODELS_DIR, ORIGINAL_PHOTOS_DIR
from script.lista_arquivos import lista_arquivos


def main():
    modelos = lista_arquivos(MODELS_DIR)
    fotos_originais = lista_arquivos(ORIGINAL_PHOTOS_DIR)

    for modelo in modelos:
        print(f"Avaliando modelo: {modelo}")
        for foto in fotos_originais:
            print(f" - Processando foto: {foto}")


if __name__ == "__main__":
    main()
