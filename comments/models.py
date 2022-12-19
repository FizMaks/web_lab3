from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from utils.translit import translit as tt

def gen_slug(s):
    new_slug = slugify(tt(s), allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Comment(models.Model):
    slug = models.SlugField('Ссылка, НЕ ЗАПОЛНЯТЬ', max_length=300, blank=True, unique=True)
    body = models.TextField('Текст комментария', blank=True, db_index=True)
    date_pub = models.DateTimeField('Время публикации', auto_now_add=True)

    def __str__(self):
        if len(self.body) > 15:
            return self.body[:15] + '...'
        return self.body

    def get_update_url(self):
        return reverse("news_post_update_url", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("news_post_delete_url", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.body[:15])
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'