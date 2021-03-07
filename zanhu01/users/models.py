#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from __future__ import unicode_literals
#为了让python2象3一样处理unicode字符
# from django.utils.encoding import python_2_unicode_compatible
from six import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


@python_2_unicode_compatible
class User(AbstractUser):
    """自定义用户模型"""
    nickname = models.CharField(null=True, blank=True, max_length=255, verbose_name='昵称')
    job_title = models.CharField(max_length=50, null=True, blank=True, verbose_name='职称')
    introduction = models.TextField(blank=True, null=True, verbose_name='简介')
    # upload_to要填路径
    picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name='头像')
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='城市')
    personal_url = models.URLField(max_length=555, blank=True, null=True, verbose_name='个人链接')
    weibo = models.URLField(max_length=255, blank=True, null=True, verbose_name='微博链接')
    zhihu = models.URLField(max_length=255, blank=True, null=True, verbose_name='知乎链接')
    github = models.URLField(max_length=255, blank=True, null=True, verbose_name='Github链接')
    linkedin = models.URLField(max_length=255, blank=True, null=True, verbose_name='LinkedIn链接')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 设置元数据
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    # 模型类实例，直观可读的方法
    def __str__(self):
        return self.username
    # 返回用户详情页中url的路径，因为每个用户的详情页都是不一样的
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
    # 个人信息中返回用户的名字
    def get_profile_name(self):
        if self.nickname:
            return self.nickname
        return self.username
