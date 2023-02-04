from django.shortcuts import render
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password

# Create your views here.


@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_category(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except:
        return Response({"bad_request": "category doesnt exist"}, status=status.HTTP_400_BAD_REQUEST)


class CreatePost(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


@api_view(['POST'])
def postCreate(request):
    categoria = Category.objects.get(id=request.data['categoria'])
    user = User.objects.get(id=request.data['ususario'])
    post = Post.objects.create(
        imagen=request.data['imagen'],
        usuario_creador=user,
        titulo=request.data['titulo'],
        descripcion=request.data['descripcion'],
        body=request.data['body'],
        categoria=categoria,
    )
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
