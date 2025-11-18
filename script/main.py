import os

from PIL import Image
from rembg import remove, new_session

from config import ORIGINAL_PHOTOS_DIR, OUTPUT_MODEL_DIR, MODELOS_PARA_AVALIACAO
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
            output_path = os.path.join(OUTPUT_MODEL_DIR, modelo,foto)

            # Cria o diretório de saída se não existir
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            with open(input_path, "rb") as arquivo_entrada:
                with open(output_path, "wb") as arquivo_saida:
                    foto_original = arquivo_entrada.read()
                    # Remove o fundo da foto usando a sessão do modelo
                    foto_sem_fundo = remove(foto_original, session=session)
                    arquivo_saida.write(foto_sem_fundo)

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
