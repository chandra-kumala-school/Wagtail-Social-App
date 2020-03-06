from django import template
from social.models import Links

register = template.Library()

# Social snippets
@register.inclusion_tag('tags/links.html', takes_context=True)
def socials(context):
    return {
        'socials': Links.objects.all(),
        'request': context['request'],
    }