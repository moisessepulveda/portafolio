from django.utils.html import format_html
from django.templatetags.static import static

from wagtail.core import hooks

@hooks.register('insert_global_admin_css')
def global_admin_css():
    print('registering global css')
    return format_html('<link rel="stylesheet" href="{}">', static('consulting/assets/css/admin.css'))


#hooks.register('global_admin_css', global_admin_css)