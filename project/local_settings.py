# # type: ignore
# # flake8: noqa

# # Comando:
# # python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
# SECRET_KEY = 'CHANGE ME'


# # DEBUG DEVE SER False em produção
# DEBUG = False

# # Seu domínio ou IP devem vir aqui
# ALLOWED_HOSTS = [
#     'SEU_DOMINIO_OU_IP',
# ]  # Troque * para seu domínio ou IP

# # Config para postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'base_de_dados',
#         'USER': 'meu_usuario',
#         'PASSWORD': 'senha_do_usuario',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
