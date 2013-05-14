
def setup_env():
    """
    assume we are running with the correct setting - some commands will enforce
    explicit --setting.

    Always generate a new app.yaml by instanciating the template
    """
    import os
    import subprocess
    from django.conf import settings

    from django.template import Template, Context

    version = subprocess.check_output(['git', 'describe'])
    with open(os.path.join(settings.BASE_DIR, 'VERSION'), 'w') as f:
        f.write(version)
    context = {
            'env_name': settings.ENV_NAME,
            'version': version.replace('.', '-').replace('/', '-'),
            'tmp': os.environ.get('TMP', ''),
            }
    with open(os.path.join(settings.BASE_DIR, 'app.template.yaml'), 'r') as template:
        with open(os.path.join(settings.BASE_DIR, 'app.yaml'), 'w') as target:
            target.write(Template(template.read()).render(Context(context)))


setup_env()
