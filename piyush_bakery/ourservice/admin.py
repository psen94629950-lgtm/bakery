from django.contrib import admin

# Register your models here.
from .models import Contactform
class ContactformAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

admin.site.register(Contactform, ContactformAdmin)


from .models import About_d
class AboutAdmin(admin.ModelAdmin):
    list_display = ('About_d_title', 'About_d_description', 'About_d_img1', 'About_d_img2')

admin.site.register(About_d, AboutAdmin)


from .models import Product_d
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_d_price', 'Product_d_name', 'Product_d_img', 'Product_d_description')
admin.site.register(Product_d, ProductAdmin)


from .models import Team_d
class TeamAdmin(admin.ModelAdmin):
    list_display = ('Team_d_name', 'Team_d_position', 'Team_d_img')
admin.site.register(Team_d, TeamAdmin)

from .models import Review_d
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('Review_d_name', 'Review_d_position', 'Review_d_img', 'Review_d_message')
admin.site.register(Review_d, ReviewAdmin)