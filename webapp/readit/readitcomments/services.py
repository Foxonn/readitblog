def exist_user(user_name, user_email):
    from readitcomments.models import User
    """Зарегистрировать нового юзера"""
    user = User.objects.filter(email=user_email).first()

    if not user:
        user = User(name=user_name, email=user_email)
        user.save()

    return user
