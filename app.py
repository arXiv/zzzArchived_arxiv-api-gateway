import os
from arxiv.docs.factory import create_web_app as base_create

os.environ['SITE_NAME'] = 'api'
os.environ['STATIC_ROOT'] = os.path.abspath('./api/static/') + '/'
os.environ['TEMPLATE_ROOT'] = os.path.abspath('./api/templates/') + '/'

def create_web_app():
    return base_create() 

app = create_web_app()
