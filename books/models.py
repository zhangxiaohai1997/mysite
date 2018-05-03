from django.db import models

# Create your models here.
class Publisher(models.Model):
    """一个模型对应于一个数据库表，
    模型中的各个属性分别对应于数据库表中的一列。
    属性的名称对应于列的名称，
    字段的类型（如CharField）对应于数据库列的类型（如 varchar）。"""
    name=models.CharField(max_length=30,verbose_name="名称")
    address=models.CharField(max_length=50,verbose_name="地址")  #自定义字段的标注
    city=models.CharField(max_length=60,verbose_name="城市")
    state_provice=models.CharField(max_length=60,verbose_name="省份")
    country=models.CharField(max_length=60,verbose_name="国家")
    website=models.URLField(verbose_name="网址")   #用于输入 URL 的 CharField。可选 max_length 选项

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = "出版社"
        ordering=['name']  #按name排序

class Author(models.Model):
    first_name=models.CharField(max_length=30,verbose_name="姓氏")
    last_name=models.CharField(max_length=40,verbose_name="名字")
    email=models.EmailField(blank=True,verbose_name='邮箱地址')  #输入邮件地址的字段,设置blank=True允许该邮件字段为空,默认情况下blank=False
    class Meta:
        verbose_name="作者"
        verbose_name_plural="作者"
    def __str__(self):
        return u"%s %s" % (self.first_name,self.last_name)

class Book(models.Model):
    title=models.CharField(max_length=100,verbose_name="标题")
    authors=models.ManyToManyField(Author,verbose_name="作者")  #建立多对多关系
    publisher=models.ForeignKey(Publisher,verbose_name="出版社")  #建立一对多关系
    publication_date=models.DateField(blank=True,null=True,verbose_name="出版日期")   #出版时间  将时间设为可选字段
    class Meta:
        verbose_name="书籍"
        verbose_name_plural="书籍"
    def __str__(self):
        return self.title