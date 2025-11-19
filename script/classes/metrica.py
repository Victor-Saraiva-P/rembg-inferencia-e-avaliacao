from __future__ import annotations

import os
from dataclasses import dataclass

import numpy as np

from config import MASKS_SUBDIR_PATH, SEGMENTED_PHOTOS_DIR
from script.utils.carregador_mascara import carregar_mascara_binaria


def _resolver_caminho_predito(model_name: str, image_name: str) -> str:
    mask_dir = MASKS_SUBDIR_PATH.format(model_name=model_name)
    return os.path.join(mask_dir, image_name)


def calcular_roi_association(image_name: str, model_name: str) -> float:
    gt_path = os.path.join(SEGMENTED_PHOTOS_DIR, image_name)
    mask_dir = MASKS_SUBDIR_PATH.format(model_name=model_name)
    pred_path = os.path.join(mask_dir, image_name)

    gt_mask = carregar_mascara_binaria(gt_path)
    pred_mask = carregar_mascara_binaria(pred_path)

    intersecao = np.logical_and(gt_mask, pred_mask).sum()
    soma_gt = gt_mask.sum()
    soma_pred = pred_mask.sum()

    denominador_dice = soma_gt + soma_pred
    if denominador_dice == 0:
        return 0.0

    dice = (2 * intersecao) / denominador_dice

    # # Cálculo do IoU ( opcional, para desempate)
    # uniao = np.logical_or(gt_mask, pred_mask).sum()
    # iou = (intersecao / uniao) if uniao else 0.0

    score = dice
    return float(round(score, 4))


def calcular_pearson_corr(image_name):
    # TODO: Implementar cálculo real
    return 0  # Valor fictício para exemplo


def calcular_spearman_corr(image_name):
    # TODO: Implementar cálculo real
    return 0  # Valor fictício para exemplo


def calcular_noise_separation_score(image_name):
    # TODO: Implementar cálculo real
    return 0  # Valor fictício para exemplo


def calcular_contour_similarity(image_name):
    # TODO: Implementar cálculo real
    return 0  # Valor fictício para exemplo


def calcular_area_diff_pct(image_name):
    # TODO: Implementar cálculo real
    return 0  # Valor fictício para exemplo


def calcular_inference_time_ms(image_name):
    # TODO: Implementar cálculo real
    return 0  # Valor fictício para exemplo


def metrificar(image_name, model_name):
    return Metrica(
        calcular_roi_association(image_name, model_name),
        calcular_pearson_corr(image_name),
        calcular_spearman_corr(image_name),
        calcular_noise_separation_score(image_name),
        calcular_contour_similarity(image_name),
        calcular_area_diff_pct(image_name),
        calcular_inference_time_ms(image_name)
    )


@dataclass(frozen=True)
class Metrica:
    roi_association: float
    pearson_corr: float
    spearman_corr: float
    noise_separation_score: float
    contour_similarity: float
    area_diff_pct: float
    inference_time_ms: float

    def __composite_values__(self):
        return (
            self.roi_association,
            self.pearson_corr,
            self.spearman_corr,
            self.noise_separation_score,
            self.contour_similarity,
            self.area_diff_pct,
            self.inference_time_ms,
        )
