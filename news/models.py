from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    type = models.SmallIntegerField(
        choices=((1, '原创'), (2, '转载')),
        default=1
    )
    school = models.ForeignKey(to='School', on_delete=models.CASCADE)
    tag = models.ManyToManyField(to='Tag')


class School(models.Model):
    name = models.CharField(max_length=32)


class Tag(models.Model):
    name = models.CharField(max_length=32)
