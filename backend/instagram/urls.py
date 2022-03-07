from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include, path

router = DefaultRouter()
router.register("post", views.PostViewSet)  # 2개 url을 만들어줍니다.
# router.urls에 리스트 형태로 url이 존재.
urlpatterns = [
    # path("public/", views.PublicListAPIView.as_view()),
    # path("public/", views.public_post_list),
    path("", include(router.urls)),
]
