from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):  # postlist, postdetail 5가지 모두 처리
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     print("request.body : ", request.body)
    #     print("request.POST : ", request.POST)
    #     return super().dispatch(request, *args, **kwargs)


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
