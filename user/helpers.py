def get_role(auth_user):
    """
    获取用户角色
    :param auth_user: 系统用户
    :return:
    """
    if hasattr(auth_user, 'teacher'):
        return "teacher"
    elif hasattr(auth_user, 'student'):
        return "student"
    elif hasattr(auth_user, 'administrator'):
        return "administrator"
    elif auth_user.is_superuser:
        return "superuser"
    else:
        return ""
