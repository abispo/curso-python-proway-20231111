
from typing import Dict, Optional

import requests

def pegar_frase_anime(nome_anime: Optional[str] = "") -> Dict[str, str]:

    url: str = "https://animechan.xyz/api/random"

    if nome_anime:
        url = f"{url}/anime?title={nome_anime}"

    return requests.get(url=url).json()

if __name__ == "__main__":
    print(pegar_frase_anime("gintama"))
    print(pegar_frase_anime())