from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post
from rest_framework import mixins
from rest_framework.decorators import action
from .permission import IsAuthorOrReadonly

from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):  # postlist, postdetail 5가지 모두 처리
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticated,
        IsAuthorOrReadonly,
    ]

    def perform_create(self, serializer):
        author = self.request.user  # User or AnonymousUser
        ip = self.request.META["REMOTE_ADDR"]
        serializer.save(author=author, ip=ip)

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body : ", request.body)
    #     print("request.POST : ", request.POST)
    #     return super().dispatch(request, *args, **kwargs)
    @action(detail=False, methods=["GET"])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=["is_public"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# class PublicListAPIView(generics.ListCreateAPIView):  # postlist 2가지만 처리
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer


# class PublicListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)


# @api_view(["GET"])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


# class PostListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
