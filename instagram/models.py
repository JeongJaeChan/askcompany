from distutils.command.upload import upload
from django.conf import settings
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # java toString
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        # return "Custom Post object ({})".format(self.id)
        return self.message

    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"

class Comment(models.Model):
    post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE,
    limit_choices_to={'is_public': True}) #post_id 필드가 생성
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)