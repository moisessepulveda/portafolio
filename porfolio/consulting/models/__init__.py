from wagtail.contrib.modeladmin.options import (
    ModelAdmin, 
    modeladmin_register,
    ModelAdminGroup,
    )
from .info_page import InfoPage
from .home_consulting import HomeConsulting
from .service_consulting_page import ServiceConsultingPage
from .form_page import FormPage
from .footer_snippet import Footer
from .settings import GeneralInfo
from .employee import (
    Bank,
    AccountType,
    Employee,
    JobPosition,
    ContractType,
    Contract,
)

class BankAdmin(ModelAdmin):
    model = Bank
    menu_label = 'Bancos'
    menu_icon = 'site'
    list_display = ('name',)
    search_fields = ('name',)
    add_to_settings_menu = True


class AccountTypeAdmin(ModelAdmin):
    model = AccountType
    menu_label = 'Tipos de cuenta bancaría'
    menu_icon = 'bars'
    list_display = ('name',)
    search_fields = ('name',)
    add_to_settings_menu = True

class JobPositionAdmin(ModelAdmin):
    model = JobPosition
    menu_label = 'Cargos'
    menu_icon = 'bars'
    list_display = ('name',)
    search_fields = ('name',)
    add_to_settings_menu = True

class EmployeeAdmin(ModelAdmin):
    model = Employee
    menu_label = 'Colaboradores'
    menu_icon = 'group'
    list_display = ('rut', 'full_name')
    search_fields = ('name', 'rut')

class ContractTypeAdmin(ModelAdmin):
    model = ContractType
    menu_label = 'Tipos de contrato'
    menu_icon = 'bars'
    list_display = ('name',)
    search_fields = ('name',)
    add_to_settings_menu=True

"""

class EmployeeSettings(ModelAdminGroup):

    menu_label = 'Configuración módulo colaboradores'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (BankAdmin, AccountTypeAdmin)
    add_to_settings_menu = True
"""


modeladmin_register(BankAdmin)
modeladmin_register(AccountTypeAdmin)
modeladmin_register(EmployeeAdmin)
modeladmin_register(JobPositionAdmin)
modeladmin_register(ContractTypeAdmin)
#modeladmin_register(EmployeeSettings)


