from django.contrib import admin
from myapp.models import Student, Product,Patient,Appointment,Contact,Member,ImageModel
# Register your models here.
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(Member)
admin.site.register(ImageModel)