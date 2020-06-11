from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from customers import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name="index.html")),
    path('api/customers/', views.customers_list),
    path('api/customers/<pk>', views.customers_detail),
]
