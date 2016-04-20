from django import template

from detransapp.models import Sistema

# TODO criar um metodo no manager para 'Sistema.objects.order_by('data')' esta duplicando codigo
register = template.Library()


@register.simple_tag
def logo():
    sis = Sistema.objects.order_by('data').last()
    if sis:
        return sis.logo
    return None


@register.simple_tag
def sigla():
    sis = Sistema.objects.order_by('data').last()
    if sis:
        return sis.sigla
    return None


@register.simple_tag
def nome_completo():
    sis = Sistema.objects.order_by('data').last()
    if sis:
        return sis.nome_completo.upper()
    return None
