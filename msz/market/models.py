# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class Category(TimeStampedModel):
    name = models.CharField(max_length=128, verbose_name=_(u"分类名称"), unique=True)
    info = models.CharField(max_length=50, verbose_name=_(u"简短优势"))
    image = models.ImageField(upload_to='market/category/', blank=True, verbose_name=_(u"分类图片"))
    is_delete = models.BooleanField(default=False, verbose_name=_(u"是否删除"))
    code = models.CharField(max_length=50, blank=True, null=True, verbose_name=_(u"分类编号"))
    description = models.TextField(blank=True, verbose_name=_(u"描述"))

    class Meta:
        verbose_name = _(u"分类")
        verbose_name_plural = _(u"后台权限")

    def __str__(self):
        return self.name

#
# @python_2_unicode_compatible
# class Product(TimeStampedModel):
#     name = models.CharField(max_length=128, verbose_name=_(u"名称"), unique=True)
#     category = models.ForeignKey(Category, verbose_name=_(u"所属分类"))
