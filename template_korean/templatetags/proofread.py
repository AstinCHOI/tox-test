import korean
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def proofread(value):
    return korean.l10n.proofread(value)
