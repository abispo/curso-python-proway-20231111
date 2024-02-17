
from typing import List

lista_textos = [
    "João;8.5;8.0;9.0",
    "Maria;9.5;10.0;10.0",
    "José;7.0;6.0;8.5",
]

def processar_texto(texto: str) -> List[float]:
    return [float(nota) for nota in texto.split(';')[1:]]
