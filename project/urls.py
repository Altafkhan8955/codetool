"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#admin.site.site_header = "CODETOOL Administrator"
#admin.site.site_title = "CODETOOL Administrator"
#admin.site.index_title = "CODETOOL Administrator"

handler400 = 'app.views.custom_bad_request_view'
handler401 = 'app.views.custom_unthorized_view'
handler403 = 'app.views.custom_permission_denied_view'
handler404 = 'app.views.custom_page_not_found_view'
handler500 = 'app.views.custom_server_error_view'

urlpatterns = [
    path('code_tool_khan89/', admin.site.urls),
    path('',include("app.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
