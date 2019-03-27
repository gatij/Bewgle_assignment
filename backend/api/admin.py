from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('sku','rating','title', 'author', 'text','source')

admin.site.register(Review,ReviewAdmin)

