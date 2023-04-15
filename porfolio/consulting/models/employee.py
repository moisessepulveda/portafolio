from curses import panel
from dataclasses import Field
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    FieldRowPanel,
    TabbedInterface, 
    ObjectList,
    InlinePanel,
)
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable, Page, ClusterableModel

class JobPosition(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self) -> str:
        return self.name

class ContractType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tipo Contrato'
        verbose_name_plural = 'Tipo contratos'

    def __str__(self) -> str:
        return self.name

class AccountType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tipo de cuenta'
        verbose_name_plural = 'Tipos de cuenta'

    def __str__(self) -> str:
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'

    def __str__(self) -> str:
        return self.name



class Employee(ClusterableModel):
    rut = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    second_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Segundo nombre')
    father_last_name = models.CharField(max_length=100, verbose_name='Apellido paterno')
    mother_last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Apellido materno')

    image = models.ForeignKey(
            'wagtailimages.Image',
            null=True, blank=True,
            on_delete=models.SET_NULL,
            related_name='+',
            verbose_name='Imagen de perfil',
    )

    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name='Banco')
    account_type = models.ForeignKey(AccountType, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name='Tipo de cuenta')
    account_number = models.CharField(max_length=200, null=True, blank=True, verbose_name='Numero de cuenta')

    def full_name(self):
        return f"{self.first_name} {self.father_last_name}"

    full_name.short_description = 'Nombre completo'

    # contact
    personal_email = models.EmailField(null=True, blank=True, verbose_name='Correo personal')
    enterprise_email = models.EmailField(null=True, blank=True, verbose_name='Correo corporativo')
    phone = models.CharField(max_length=25, null=True, blank=True, verbose_name='Teléfono')
    
    
    # educational info
    university = models.CharField(max_length=100, null=True, blank=True, verbose_name='Universidad/Instituto')
    carrer = models.CharField(max_length=200, null=True, blank=True, verbose_name='Carrera')

    def __str__(self) -> str:
        return self.full_name()

    panels = [
        FieldPanel('rut'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name'),
                FieldPanel('second_name'),
            ]),
            FieldRowPanel([
                FieldPanel('father_last_name'),
                FieldPanel('mother_last_name'),
            ]),
        ], heading='Nombres'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('personal_email'),
                FieldPanel('enterprise_email'),
            ]),
            FieldPanel('phone'),
        ], heading='Información de contacto'),
        FieldPanel('image'),
    ]

    bank_panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('bank'),
                FieldPanel('account_type'),
            ]),
            FieldPanel('account_number'),
        ], heading='Información bancaria'),
    ]

    contractual_panels = [
         InlinePanel('contracts', label="Contratos"),
    ]

    payment_panels = [
        InlinePanel('payments', label='Pagos'),
    ]

    educational_info = [
        FieldPanel('university'),
        FieldPanel('carrer'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading='Información básica'),
        ObjectList(educational_info, heading='Información educacional'),
        ObjectList(bank_panels, heading='Información bancaría'),
        ObjectList(contractual_panels, heading='Información contractual'),
        ObjectList(payment_panels, heading='Pagos'),
    ])

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'


class Contract(Orderable):
    contract_type = models.ForeignKey(ContractType, on_delete=models.DO_NOTHING, verbose_name='Tipo de contrato')
    job_position = models.ForeignKey(JobPosition, on_delete=models.DO_NOTHING, verbose_name='Cargo')

    employee = ParentalKey(Employee, on_delete=models.CASCADE, related_name='contracts')

    date_start = models.DateField(verbose_name='Fecha inicio')
    date_end = models.DateField(null=True, blank=True, verbose_name='Fecha de termino')

    active = models.BooleanField(default=True, verbose_name='Activo')

    salary = models.DecimalField(
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=11,
        verbose_name='Remuneración',
    )


    panels = [
        FieldRowPanel([
            FieldPanel('contract_type'),
            FieldPanel('job_position'),
        ]),
        FieldRowPanel([
            FieldPanel('date_start'),
            FieldPanel('date_end'),
        ]),
        FieldPanel('salary'),
        FieldPanel('active'),
    ]



class Payments(Orderable):
    employee = ParentalKey(Employee, on_delete=models.CASCADE, related_name='payments')

    amount = models.DecimalField(
        verbose_name='Monto',
        max_digits=11,
        decimal_places=2,
    )
    date = models.DateField(
        verbose_name='Fecha pago',
    )

    comment = models.TextField(
        verbose_name='glosa',
        null=True,
        blank=True,
    )


    panels = [
        FieldRowPanel([
            FieldPanel('amount'),
            FieldPanel('date'),
        ]),
        FieldPanel('comment'),
    ]
