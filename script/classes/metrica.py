from dataclasses import dataclass


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
