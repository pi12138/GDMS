from django import template
from user.helpers import get_role

register = template.Library()


@register.filter
def get_username(val):
    role_str, role_obj = get_role(val)

    return role_obj.name 
