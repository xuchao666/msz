# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class Company(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name=_(u"名称"))
    mobile = models.CharField(max_length=20, verbose_name=_(u'手机号'), blank=True)
    tel = models.CharField(max_length=20, verbose_name=_(u"联系方式"), blank=True)
    image = models.ImageField(upload_to='market/category/', blank=True, verbose_name=_(u"公司图片"))
    description = models.TextField(blank=True, verbose_name=_(u"描述"))
    address = models.CharField(max_length=128, verbose_name=_(u"地址"), blank=True)
    manager = models.CharField(max_length=20, verbose_name=_(u"负责人"))

    class Meta:
        verbose_name = _(u"公司")
        verbose_name_plural = _(u"公司")

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


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
        verbose_name_plural = _(u"分类")

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''

    @property
    def products(self):
        return Product.objects.filter(category=self)


@python_2_unicode_compatible
class Product(TimeStampedModel):
    name = models.CharField(max_length=128, verbose_name=_(u"名称"), unique=True)
    code = models.CharField(max_length=50, blank=True, null=True, verbose_name=_(u"商品编码"))
    category = models.ForeignKey(Category, verbose_name=_(u"所属分类"))
    info = models.CharField(max_length=50, verbose_name=_(u"简短优势"))
    image = models.ImageField(upload_to='market/product/', blank=True, verbose_name=_(u"商品图片图片"))
    is_delete = models.BooleanField(default=False, verbose_name=_(u"是否删除"))
    description = models.TextField(blank=True, verbose_name=_(u"描述"))
    materials = models.TextField(blank=True, verbose_name=_(u"配料"))

    class Meta:
        verbose_name = _(u"商品表")
        verbose_name_plural = _(u"商品表")

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


@python_2_unicode_compatible
class HomePic(TimeStampedModel):
    name = models.CharField(max_length=64, verbose_name=_(u"名称"))
    image = models.ImageField(upload_to='market/', blank=True, verbose_name=_(u"首页轮播图片"))
    is_active = models.BooleanField(default=False, verbose_name=_(u"是否是首张图片"))

    class Meta:
        verbose_name = _(u"首页轮播图")
        verbose_name_plural = _(u"首页轮播图")

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''
