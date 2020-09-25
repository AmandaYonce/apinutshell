"""apinut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from api import views as api_views


router = routers.DefaultRouter()
router.register(r"shoe", api_views.ShoeView)
router.register(r"manufacturers", api_views.ManufacturerView)
router.register(r"shoeType", api_views.ShoeTypeView)
router.register(r"shoeColor", api_views.ShoeColorView)
router.register(r"shoeSize", api_views.ShoeSizeView)
router.register(r"brandName", api_views.BrandView)
router.register(r"material", api_views.MaterialView)
router.register(r"fastener", api_views.FastenerView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
