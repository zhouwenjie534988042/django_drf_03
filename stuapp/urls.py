from django.conf.urls import url
from stuapp import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # url(r'^actors/$', views.ActorListView.as_view()),
    # url(r'^actors/(?P<pk>\d+)/$', views.ActorDetailView.as_view()),
]


# router = DefaultRouter()  # 可以处理视图的路由器
# router.register('actors', views.ActorListView, basename='actors')  # 向路由器中注册视图集
#
#
# urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
