import os

from rembg import remove, new_session

from config import MODELS_DIR, ORIGINAL_PHOTOS_DIR, OUTPUT_MODEL_DIR, MODELOS_PARA_AVALIACAO
from script.lista_arquivos import lista_arquivos


def main():
    fotos_originais = lista_arquivos(ORIGINAL_PHOTOS_DIR)

    for modelo in MODELOS_PARA_AVALIACAO:
        print(f"Avaliando modelo: {modelo}")

        # Cria uma sessão com o modelo
        session = new_session(modelo)

        for foto in fotos_originais:
            print(f" - Processando foto: {foto}")

            input_path = os.path.join(ORIGINAL_PHOTOS_DIR, foto)
            output_path = os.path.join(OUTPUT_MODEL_DIR, modelo,foto)

            # Cria o diretório de saída se não existir
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            with open(input_path, "rb") as arquivo_entrada:
                with open(output_path, "wb") as arquivo_saida:
                    foto_original = arquivo_entrada.read()
                    # Remove o fundo da foto usando a sessão do modelo
                    foto_sem_fundo = remove(foto_original, session=session)
                    arquivo_saida.write(foto_sem_fundo)


if __name__ == "__main__":
    main()
