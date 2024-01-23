from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from base.models import Book
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['emailllll'] = user.email
        token['username'] = user.username
        token['waga'] = "baga"
        # ...
        print("testtttttttttttt")
        return token


@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = False
    user.save()
    return Response("new user born")

    # author = models.CharField(max_length=50,null=True,blank=True)
    # book_name = models.CharField(max_length=50,null=True,blank=True)
    # image = models.ImageField(null=True,blank=True,default='/placeholder.png')



@api_view(['GET'])
def getImages(request):
    res=[] #create an empty list
    for img in Book.objects.all(): #run on every row in the table...
        res.append({"title":img.author,
                "description":img.book_name,
                "completed":False,
               "image":str( img.image)
                }) #append row by to row to res list
    return Response(res) #return array as json response


class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=BookSerializer(data=request.data)
       
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',api_serializer.errors)
            return Response(api_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

@api_view(['GET'])
def index(req):
    return Response('hello')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(req):
    return Response('secret')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_book(req):
        bk_serializer = BookSerializer(data=req.data)
        if bk_serializer.is_valid():
            bk_serializer.save()
            return Response ("post...")
        else:
            return Response (bk_serializer.errors)


@api_view(['GET','POST','DELETE','PUT','PATCH'])
def books_view(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_book=Book.objects.get(id=id)
                return Response (BookSerializer(temp_book,many=False).data)
            except Book.DoesNotExist:
                return Response ("not found")
        all_Books=BookSerializer(Book.objects.all(),many=True).data
        return Response ( all_Books)
    
    if req.method =='DELETE':
        try:
            temp_book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")    
       
        temp_book.delete()
        return Response ("del...")
    if req.method =='PUT':
        try:
            temp_book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")
       
        ser = BookSerializer(data=req.data)
        old_Book = Book.objects.get(id=id)
        res = ser.update(old_Book, req.data)
        return Response(res)

