from django_uwsgi.decorators import spool
from readitcomments.services import notify_user, notify_admin, notify_new_responded


@spool
def task_notify_new_responded(args):
    return notify_new_responded(args)


@spool
def task_notify_user(args):
    return notify_user(args)


@spool
def task_notify_admin(args):
    return notify_admin(args)
