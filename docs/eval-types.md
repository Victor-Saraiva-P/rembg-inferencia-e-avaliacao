# Critérios de Avaliação dos Modelos de Remoção de Fundo

> Este arquivo descreve de forma clara e padronizada como os critérios de avaliação dos modelos de remoção de fundo são definidos, calculados e interpretados.

## ROI association

A **Região de Interesse (ROI)**, neste projeto, corresponde à segmentação manual realizada pelos especialistas e armazenada em `dados/fotos segmentadas/`. Essa segmentação manual é considerada a representação mais fiel do contorno corporal do animal, servindo como **Ground Truth (GT)** para todas as avaliações.

A ROI (nosso GT) será então comparada com a segmentação prevista pelo modelo para calcular métricas de similaridade. A principal abordagem será:

**Dice Coefficient**: métrica principal de similaridade entre as máscaras, usada para ranquear os modelos de forma geral. O Dice é escolhido como métrica principal porque ele é mais estável e sensível à similaridade global entre as máscaras, dando maior peso à interseção real entre a segmentação prevista e a ROI. Isso o torna ideal para avaliar formas orgânicas, como o contorno corporal dos búfalos, onde pequenas imperfeições nas bordas não devem penalizar excessivamente o modelo.

Caso muitos modelos tenham um Dice bom, o que será usado é o **IoU (Intersection over Union)**: métrica complementar, mais rígida, utilizada como "pente fino" quando vários modelos apresentam valores de Dice semelhantes. O IoU funciona como "pente fino" porque é uma métrica mais rígida, pequenas diferenças entre a previsão e a ROI reduzem seu valor de forma mais acentuada. Assim, enquanto o Dice é ótimo para identificar modelos bons no geral, o IoU destaca qual deles alcança realmente a melhor sobreposição precisa, sendo útil para desempatar modelos com Dice semelhantes.

Na prática, os modelos serão primeiro avaliados e filtrados com base no Dice; em seguida, entre aqueles com desempenho considerado satisfatório, o IoU será usado para desempate e análise mais detalhada da qualidade da segmentação. 
