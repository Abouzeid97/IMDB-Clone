from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.api.serializers import WatchlistSerializer, StreamPlatformSerializer
from watchlist_app.models import Watchlist, StreamPlatform

class StreamPlatformListAV(APIView):
    
    def get(self, request):
        streamplatforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streamplatforms, many=True, context={"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            streamplatform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'does not found'} ,status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(streamplatform, context={"request": request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            streamplatform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'does not found'} ,status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(streamplatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        streamplatform = StreamPlatform.objects.get(pk=pk)
        streamplatform.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class WhatchlistListAV(APIView):

    def get(self, request):
        watchlists = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchlistDetailAV(APIView):

    def get(self, request, pk):
        try:
            watchlist = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'Error': 'does not found'} ,status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(watchlist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            watchlist = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'Error': 'does not found'} ,status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        watchlist = Watchlist.objects.get(pk=pk)
        watchlist.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    



#### FUNCTION BASED VIEW

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie does not found'} ,status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status.HTTP_204_NO_CONTENT)
    