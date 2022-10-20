from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Company)
def update_company_href(sender, instance, created, **kwargs):

    # if created == False:
    #     instance.company.href = "/companies/" + str(instance.company.id)
    #     instance.company.save()

    if created:
        instance.href = "/companies/" + str(instance.id)
        instance.save()

#post_save.connect(update_company_href ,sender = Company)