ROLE_CLIENTE = "CLIENTE"
ROLE_FUNCIONARIO = "FUNCIONARIO"

def is_staff_user(user) -> bool:
    return user.is_authenticated and (user.is_staff or user.is_superuser or user.groups.filter(name=ROLE_FUNCIONARIO).exists())

def is_cliente_user(user) -> bool:
    return user.is_authenticated and user.groups.filter(name=ROLE_CLIENTE).exists()
