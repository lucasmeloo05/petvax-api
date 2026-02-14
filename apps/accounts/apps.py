from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts"

    def ready(self):
        from django.db.models.signals import post_migrate
        from django.dispatch import receiver
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType

        from apps.accounts.roles import ROLE_CLIENTE, ROLE_FUNCIONARIO
        from apps.vaccines.models import Vaccine
        from apps.vaccinations.models import VaccinationRecord

        @receiver(post_migrate)
        def ensure_roles_and_perms(sender, **kwargs):
            #Grupos
            cliente_group, _ = Group.objects.get_or_create(name=ROLE_CLIENTE)
            func_group, _ = Group.objects.get_or_create(name=ROLE_FUNCIONARIO)

            #Permissoes (add/change/delete/view)
            vaccine_ct = ContentType.objects.get_for_model(Vaccine)
            vacc_record_ct = ContentType.objects.get_for_model(VaccinationRecord)

            #Permissoes Funcionário
            perms = Permission.objects.filter(
                content_type__in=[vaccine_ct, vacc_record_ct],
                codename__in=[
                    "add_vaccine", "change_vaccine", "delete_vaccine", "view_vaccine",
                    "add_vaccinationrecord", "change_vaccinationrecord", "delete_vaccinationrecord", "view_vaccinationrecord",
                ]
            )
            func_group.permissions.set(perms)

            #Permissoes Cliente
            cliente_perms = Permission.objects.filter(
                content_type__in=[vaccine_ct, vacc_record_ct],
                codename__in=["view_vaccine", "view_vaccinationrecord"]
            )
            cliente_group.permissions.set(cliente_perms)
