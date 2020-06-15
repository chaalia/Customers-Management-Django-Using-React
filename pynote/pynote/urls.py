from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from customers import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name="index.html")),
    path('api/customers/', views.customers_list),
    path('api/customers/<pk>', views.customers_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swag', schema_view)

]
