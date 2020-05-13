from rest_framework.response import Response

from rest_framework.views import APIView

from .models import Movies, Reviews
from .Serialazer import MoviesSerializer, MoviesSerializerDetail, ReviewSerialazaerCreate, ReviewSerialazerView, RatingSerialazerCreate

class MovieSerialazerView(APIView):
    def get (self,request):
        movies = Movies.objects.all()
        serialazer = MoviesSerializer(movies, many=True)
        return  Response(serialazer.data)



class MovieSerialazerViewDetail(APIView):

    def get (self,request, pk):
        movies = Movies.objects.get(id=pk)
        serialazer = MoviesSerializerDetail(movies)
        return  Response(serialazer.data)


class ReviewCreateView(APIView):
    def post(self, request):
        review = ReviewSerialazaerCreate(data= request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)

class ReviewALLView(APIView):
    def get(self, request):
        reviews = Reviews.objects.all()
        serialazer =  ReviewSerialazerView(many=True)
        return Response(serialazer.data)


class RatingCreateView(APIView):
    def get_client_ip(self, request):
        x_forward_for = request.META.get('HTTP_X_FORWARDED')
        if x_forward_for:
            ip = x_forward_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip



    def post(self,request):
        serialazer = RatingSerialazerCreate(request= request.data)
        if serialazer.is_valid():
            serialazer.save(id=self.get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)