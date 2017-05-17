# -*- coding: utf-8 -*-
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MainImage(TimeStampedModel):
    title = models.CharField(u'제목', max_length=100)
    description = models.CharField(u'설명', max_length=200, null=True, blank=True)
    url = models.CharField(u'링크', max_length=500, null=True, blank=True, help_text='http://~')
    type = models.CharField(u'타입(검색옵션)', default='S1', max_length=500, help_text='S1,S2,S3')

    def __unicode__(self):
        return u"%s" % (self.title)

    class Meta:
        verbose_name_plural = u"메인이미지"
        verbose_name = u"메인이미지"
