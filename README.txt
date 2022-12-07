- To install the environment we need to have the pip updated
'pip install --upgrade pip'

- After the pip upgrade we need to run the requirements.txt
'pip install -r requirements.txt'

- Setup the Runserver, Makemigration e Migrate

- Rodar Makemigrations e Migrate para o banco reconhecer

- Criar um super usuário para o django

'python manage.py createsuperuser'

- Configurar o pycharm para rodar o python console com suporte ao django:

```
import sys, os, django
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings_dev")
django.setup()
```

- Instalar o ipython (para um console mais poderoso): `pip install ipython`