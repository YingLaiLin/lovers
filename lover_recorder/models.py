from django.db import models
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, verbose_name='登录名')
    icon = models.ImageField(width_field=200, height_field=200,
                             verbose_name='头像', default=None)
    nickname = models.CharField(max_length=40, verbose_name='昵称')
    authority = models.IntegerField(verbose_name='在网站中的权限', default=0)
    level = models.IntegerField(verbose_name='用户等级', default=0)
    # 定义网站的用户类别
    USER_TYPE = ((0, '游客'), (1, '用户'), (2, '管理员'), (3, '网站所有者'))
    type = models.IntegerField(verbose_name='用户类别', default=0,
                               choices=USER_TYPE)

    # TODO 增加用户之间的关系显示,这里应当新创建一个类来描述这种关系
    # RELATIONSHIP = (
    #             (0, '朋友'), (1, '同学'), (2, '基友'), (3, '闺蜜'), (4, '男/女朋友'), (5, '夫妻'))
    # relationship = ()

    register_date = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    login_time = models.DateTimeField(verbose_name='上次登录时间', auto_now_add=True)


class Event(models.Model):
    # TODO 像朋友圈一样，使用 cardview.
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    abstract = models.TextField(max_length=100)
    date = models.DateTimeField(verbose_name='发生时间')
    content = models.TextField()
