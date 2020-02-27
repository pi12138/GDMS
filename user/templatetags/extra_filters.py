from django import template
from user.helpers import get_role

register = template.Library()


@register.filter
def get_username(val):
    role_str, role_obj = get_role(val)

    return role_obj.name 


@register.filter
def handler_none(val):
    """
    当模版中返回None时将其处理为空字符串
    """
    return ""
