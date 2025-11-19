from dataclasses import dataclass


@dataclass(frozen=True)
class Resolucao:
    altura: int
    largura: int

    def __composite_values__(self):
        return self.altura, self.largura