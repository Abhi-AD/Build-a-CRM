from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# auth
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

# lead
from apps.leads.views import SignupView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("leads/", include("apps.leads.urls", namespace="leads")),
    path("agents/", include("apps.agents.urls", namespace="agents")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
