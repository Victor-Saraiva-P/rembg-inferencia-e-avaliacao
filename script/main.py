import os

from PIL import Image
from rembg import new_session, remove

from config import (
    MASKS_SUBDIR_PATH,
    MODELOS_PARA_AVALIACAO,
    ORIGINAL_PHOTOS_DIR,
    OUTPUT_MODEL_DIR,
)
from script.avaliacao_repositorio import adicionar_avaliacao
from script.classes.avaliacao import Avaliacao
from script.lista_arquivos import lista_arquivos
from script.tipos.resolution import Resolucao


def main():
    fotos_originais = lista_arquivos(ORIGINAL_PHOTOS_DIR)

    for modelo in MODELOS_PARA_AVALIACAO:
        print(f"Avaliando modelo: {modelo}")

        # Cria uma sessão com o modelo
        session = new_session(modelo)

        for foto in fotos_originais:
            print(f" - Processando foto: {foto}")

            input_path = os.path.join(ORIGINAL_PHOTOS_DIR, foto)
            output_path = os.path.join(OUTPUT_MODEL_DIR, modelo, foto)
            mask_dir = MASKS_SUBDIR_PATH.format(model_name=modelo)
            mask_output_path = os.path.join(mask_dir, foto)

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            os.makedirs(mask_dir, exist_ok=True)

            with open(input_path, "rb") as arquivo_entrada:
                foto_original = arquivo_entrada.read()

            foto_sem_fundo = remove(foto_original, session=session)
            with open(output_path, "wb") as arquivo_saida:
                arquivo_saida.write(foto_sem_fundo)

            mask_bytes = remove(foto_original, session=session, only_mask=True)
            with open(mask_output_path, "wb") as arquivo_mask:
                arquivo_mask.write(mask_bytes)

            # Calcula a resolução
            imagem_path = os.path.join(ORIGINAL_PHOTOS_DIR, foto)
            if not os.path.exists(imagem_path):
                raise FileNotFoundError(f"Imagem não encontrada em {imagem_path}")

            with Image.open(imagem_path) as imagem:
                largura_img, altura_img = imagem.size

            resolucao = Resolucao(altura=altura_img, largura=largura_img)

            # Avalia o modelo
            avaliacao = Avaliacao(foto, modelo, resolucao)
            adicionar_avaliacao(avaliacao)


if __name__ == "__main__":
    main()
