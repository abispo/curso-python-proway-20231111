from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from registro.models import Perfil

@receiver(post_save, sender=User)
def salvar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)