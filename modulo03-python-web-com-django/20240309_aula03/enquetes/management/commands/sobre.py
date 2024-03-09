
from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Mostra informações sobre o projeto"

    def handle(self, *args: Any, **options: Any) -> str | None:
        saida = "Projeto Enquetes. Proway 2024"

        self.stdout.write(saida)
