from django.core.mail import send_mail
from django.conf import settings
from .celery import app


@app.task
def task_notify_new_responded(args):
    """Уведомить пользователя об ответе"""
    responded_user_name, user_email, comment_link = args['responded_user_name'], args['user_email'], args[
        'comment_link']

    return send_mail(subject='New response',
                     message='',
                     html_message=f'The user {responded_user_name} responded to your comment. \n<a href="{comment_link}">Go to comment</a>',
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[user_email])


@app.task
def task_notify_admin(args):
    """Уведомить админа о новом комментарии"""
    user_name, comment_link = args['user_name'], args['comment_link']

    return send_mail(subject='New commet',
                     message='',
                     html_message=f'User {user_name}, leave new message. \n<a href="{comment_link}">Go to comment</a>',
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[settings.EMAIL_HOST_USER])


@app.task
def task_notify_user(args):
    """Уведомить пользователя об оставленном комментарии"""
    user_email, comment_link = args['user_email'], args['comment_link']

    return send_mail(subject='Your commet',
                     message='',
                     html_message=f'You leave new message. \nYour comment will be published after moderation. \n<a href="{comment_link}">Go to comment</a>',
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[user_email])
