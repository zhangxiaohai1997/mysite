from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200,verbose_name="问题")
    pub_date = models.DateTimeField('date published')
    #pub_date=models.DateField(auto_now_add=True)
    def was_published_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date<=now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text
    class Meta:  #设置模型别称
        verbose_name="问题"
        verbose_name_plural="问题"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,verbose_name="选项")
    votes = models.IntegerField(default=0,verbose_name="票数")

    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name="选项"
        verbose_name_plural="选项"

class MyModel(models.Model):
    # 文件被传至`MEDIA_ROOT/uploads`目录，MEDIA_ROOT由你在settings文件中设置
    upload = models.FileField(upload_to='uploads/')

class Person(models.Model):
    SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="个人"
        verbose_name_plural="个人"



