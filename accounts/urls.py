from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import AccountsViewSet, ProfilesListCreateView, ProfilesRetrieveUpdateView

router = routers.DefaultRouter()
router.register(r'users', AccountsViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url(r'^profiles/$', ProfilesListCreateView.as_view()),
    url(r'^profiles/(?P<pk>\d+)/$', ProfilesRetrieveUpdateView.as_view()),
]