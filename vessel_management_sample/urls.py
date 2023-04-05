from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("admin1/", admin.site.urls),
    path("api/", include("auth0.urls")),
    path("api/", include("vessel_managet_net_sample.urls")),
    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
]
