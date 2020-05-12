from django.db import models
from blog.models import Post


class User(models.Model):
    name = models.CharField(max_length=75, db_index=True)
    email = models.EmailField(db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    replys = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments_replys', default=None,
                               null=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, null=True, default='', related_name='post_comments')

    # def save(self, *args, **kwargs):
    #     if self.published and self.replys:
    #         task_notify_new_responded({'responded_user_name': self.user.name,
    #                                    'user_email': self.replys.user.email,
    #                                    'comment_link': '{}#comment_{}'.format(self.post.get_absolute_url(), self.id)})
    #
    #         super().save(*args, **kwargs)

    def __str__(self):
        return self.user.name
