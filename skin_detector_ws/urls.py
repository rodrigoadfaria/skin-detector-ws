from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_nested import routers

from skin_detector_ws.views import IndexView

from authentication.views import AccountViewSet, LoginView, LogoutView
from posts.views import AccountPostsViewSet, PostViewSet
from datasets.views import DatasetViewSet

from django.contrib import admin
admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)
router.register(r'datasets', DatasetViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'posts', AccountPostsViewSet)

print (settings.MEDIA_ROOT)
urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
	url(r'^api/v1/', include(accounts_router.urls)),
	url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
	url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
	#url(r'^datasets/', include('datasets.urls')),

	url(r'^admin/', include(admin.site.urls)),

    url('^.*$', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)