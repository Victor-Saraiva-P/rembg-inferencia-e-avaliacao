from dataclasses import dataclass


def calcular_roi_association(image_name):
    # TODO: Implementar cálculo real
    return 0  # Valor fictício para exemplo


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


def metrificar(image_name):
    return Metrica(
        calcular_roi_association(image_name),
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
