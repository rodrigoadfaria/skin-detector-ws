from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_nested import routers

from skin_detector_ws.views import IndexView

from authentication.views import AccountViewSet, LoginView, LogoutView
from datasets.views import DatasetViewSet

from django.contrib import admin
admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'datasets', DatasetViewSet)

urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
	url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
	url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

	url(r'^admin/', include(admin.site.urls)),

    url('^.*$', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)