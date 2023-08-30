from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found

"""
handler500 = curry(server_error, template_name='500.html')
handler404 = curry(page_not_found, template_name='404.html')
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('product/', include('product.urls')),
    path('api/', include('api.urls')),
    
]

urlpatterns += static(settings. MEDIA_URL, document_root = settings.MEDIA_ROOT)