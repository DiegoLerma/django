from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from orders.views import router as orders_router

api = NinjaAPI(urls_namespace="orders")
api.add_router("/orders", orders_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
