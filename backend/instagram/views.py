from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):  # postlist, postdetail 5가지 모두 처리
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body : ", request.body)
    #     print("request.POST : ", request.POST)
    #     return super().dispatch(request, *args, **kwargs)


class PublicListAPIView(generics.ListCreateAPIView):  # postlist 2가지만 처리
    queryset = Post.objects.all()
    serializer_class = PostSerializer
