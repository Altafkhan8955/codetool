from django.contrib import admin
from app.models import Review,ClientQuery,Service,ImageModel,ResizableImage,ResizedImage

# Register your models here.
class AdminReview(admin.ModelAdmin):
    list_display = ['id','name','email','comment','ip','date']
    list_filter = ['name','date','id']

class AdminClienquery(admin.ModelAdmin):
    list_display = ['id','name','email','message','ip','date']
    list_filter = ['name','date','id']
#class AdminService(admin.ModelAdmin):
    #list_display = ['id','name','description','image', 'link']
    #list_filter = ['name','id']
admin.site.register(Review, AdminReview)
admin.site.register(ClientQuery, AdminClienquery)
admin.site.register(Service)
admin.site.register(ImageModel)
admin.site.register(ResizableImage)
admin.site.register(ResizedImage)


