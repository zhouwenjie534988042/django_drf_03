from django.template import Library
register = Library()
import markdown
@register.filter
def mk(value):
    return markdown.markdown(value)