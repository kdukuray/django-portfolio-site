import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def mdconverter(text):
    return markdown.markdown(text)


@register.filter
def parse_aws_url(text):
    index_of_url_params = text.find("?")
    url_of_image = text[:index_of_url_params]
    return url_of_image

