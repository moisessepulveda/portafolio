from simplelist.models import TermsPage, SimpleListPage


def main_menu(request):
    terms_page = TermsPage.objects.live().all()
    main_page = SimpleListPage.objects.live().first()

    return {
        'menus': terms_page,
        'main_page': main_page,
    }
