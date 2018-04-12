from django.contrib import admin
from  .models import Question,Choice,MyModel,Person

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(MyModel)
admin.site.register(Person)