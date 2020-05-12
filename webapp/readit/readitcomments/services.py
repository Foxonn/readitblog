from django.core.mail import send_mail
from django.conf import settings


def notify_new_responded(args):
    """Уведомить пользователя об ответе"""
    responded_user_name, user_email, comment_link = args['responded_user_name'], args['user_email'], args['comment_link']

    return send_mail(subject='New response',
                     message='',
                     html_message=f'The user {responded_user_name} responded to your comment. \n<a href="{comment_link}">Go to comment</a>',
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[user_email])


def notify_admin(args):
    """Уведомить админа о новом комментарии"""
    user_name, comment_link = args['user_name'], args['comment_link']

    return send_mail(subject='New commet',
                     message='',
                     html_message=f'User {user_name}, leave new message. \n<a href="{comment_link}">Go to comment</a>',
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[settings.EMAIL_HOST_USER])


def notify_user(args):
    """Уведомить пользователя об оставленном комментарии"""
    user_email, comment_link = args['user_email'], args['comment_link']

    return send_mail(subject='Your commet',
                     message='',
                     html_message=f'You leave new message. \nYour comment will be published after moderation. \n<a href="{comment_link}">Go to comment</a>',
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[user_email])


def exist_user(user_name, user_email):
    from readitcomments.models import User
    """Зарегистрировать нового юзера"""
    user = User.objects.filter(email=user_email).first()

    if not user:
        user = User(name=user_name, email=user_email)
        user.save()

    return user
