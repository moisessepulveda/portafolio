

from .models import (
    InfoPage,
    FormPage,
    ServiceConsultingPage,
)


def consulting_menu(request):
    simple_pages = [
        *InfoPage.objects.filter(show_in_menus=True).live(),
        *FormPage.objects.filter(show_in_menus=True).live(),
    ]

    services_page = ServiceConsultingPage.objects.filter(show_in_menus=True).live()
    #main_page = SimpleListPage.objects.live().first()

    return {
        'pages_menu': simple_pages,
        'services_menu': services_page,
    }
