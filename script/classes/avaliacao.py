from typing import Any

from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, composite

from script.classes.base_orm import Base
from script.classes.metrica import Metrica, metrificar
from script.tipos.resolution import Resolucao


class Avaliacao(Base):
    __tablename__ = "avaliacao"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    image_name: Mapped[str] = mapped_column(String, index=True)
    model_name: Mapped[str] = mapped_column(String, index=True)

    # Resolução
    # colunas físicas da resolução
    resolucao_altura: Mapped[int] = mapped_column(Integer, nullable=False)
    resolucao_largura: Mapped[int] = mapped_column(Integer, nullable=False)
    # atributo composto
    resolution: Mapped[Resolucao] = composite(Resolucao, resolucao_altura, resolucao_largura)

    # Métrica
    # colunas físicas da métrica
    roi_association: Mapped[float] = mapped_column(Float, nullable=False)
    pearson_corr: Mapped[float] = mapped_column(Float, nullable=False)
    spearman_corr: Mapped[float] = mapped_column(Float, nullable=False)
    noise_separation_score: Mapped[float] = mapped_column(Float, nullable=False)
    contour_similarity: Mapped[float] = mapped_column(Float, nullable=False)
    area_diff_pct: Mapped[float] = mapped_column(Float, nullable=False)
    inference_time_ms: Mapped[float] = mapped_column(Float, nullable=False)
    # atributo composto
    metrica: Mapped[Metrica] = composite(
        Metrica,
        roi_association, pearson_corr, spearman_corr,
        noise_separation_score, contour_similarity,
        area_diff_pct, inference_time_ms
    )

    def __init__(self, image_name, model_name, resolution: Resolucao, **kw: Any):
        super().__init__(**kw)
        self.image_name = image_name
        self.model_name = model_name
        self.resolution = resolution
        self.metrica = metrificar(image_name)