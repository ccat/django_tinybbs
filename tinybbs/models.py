from django.db import models
from django.contrib.auth.models import User, AnonymousUser

#from django.utils import translation
#from django.conf import settings
#from django.http import Http404#,HttpResponse
#from django.template import Context, Template
#from django.shortcuts import render
#from django.shortcuts import render_to_response
#from django.core.urlresolvers import reverse

from datetime import datetime

#from mptt.models import MPTTModel, TreeForeignKey

class Category(models.Model):
    name = models.CharField(max_length=2048)


class Topic(models.Model):
    """Topic of BBS.

    Variables:
    url -- Main key of Topic
    title -- Title of topic
    read_auth -- who can read
    write_auth -- who can write
    """
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=1024)
    owner = models.ForeignKey(User)
    read_auth = models.CharField(max_length=3,default="e",choices=(("e","everyone"),("s","staff"),("u","users"),))
    write_auth = models.CharField(max_length=3,default="e",choices=(("e","everyone"),("s","staff"),("u","users"),))

    def canRead(self,requestUser=AnonymousUser()):
        if(self.read_auth == "e"):
            return True
        if(self.read_auth == "s" and requestUser.is_staff == True):
            return True
        if(self.read_auth == "u" and requestUser.id != 0):
            return True
        return False

    def canWrite(self,requestUser=AnonymousUser()):
        if(self.write_auth == "e"):
            return True
        if(self.write_auth == "s" and requestUser.is_staff == True):
            return True
        if(self.write_auth == "u" and requestUser.id != 0):
            return True
        return False

    def getPosts(self,requestUser=AnonymousUser()):
        if(not self.canRead(requestUser)):
            return None

        results = Post.objects.filter(topic=self,read_auth="e").order_by("-created_at")

        if(requestUser.id != 0):
            results += Post.objects.filter(topic=self,read_auth="u").order_by("-created_at")

            if(requestUser.is_staff == True):
                results += Post.objects.filter(topic=self,read_auth="s").order_by("-created_at")

        return results

    def __unicode__(self):
        return unicode(self.title)+":"+unicode(self.url)

    @classmethod
    def getTopics(cls,requestUser=AnonymousUser()):
        results = Topic.objects.all()

        if(requestUser.id == 0):
            results = results.exclude(read_auth="u")

        if(requestUser.is_staff == False):
            results = results.exclude(read_auth="s")

        return results.order_by("-pk")


class Post(models.Model):
    """Post of BBS.

    Variables:
    topic -- Parent ot this post
    user -- who wrote this post.
    nickname -- visible name of this post
    content -- actual post content
    deletekey -- delete password. only for no-auth users
    is_disabled -- if True, staff blocks this post
    read_auth -- who can read.
    """
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User,null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    nickname = models.CharField(max_length=512)
    content = models.TextField(default="")
    deletekey = models.CharField(max_length=512,null=True,blank=True)
    is_disabled = models.BooleanField(default=False)
    read_auth = models.CharField(max_length=3,default="e",choices=(("e","everyone"),("s","staff"),("u","users"),))


