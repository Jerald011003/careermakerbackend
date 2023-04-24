# from django.http import Http404, HttpResponse
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.shortcuts import get_object_or_404

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.response import Response
# from rest_framework import status

# from base.models import Song, Review, User
# from base.serializers import SongSerializer, ReviewSerializer

# import mimetypes
# import os


# @api_view(['GET'])
# def get_songs(request):
#     keyword = request.query_params.get('keyword') or ''
#     songs = Song.objects.filter(name__icontains=keyword).order_by('-_id')

#     paginator = Paginator(songs, 5)
#     page = request.query_params.get('page') or 1

#     try:
#         songs = paginator.page(page)
#     except PageNotAnInteger:
#         songs = paginator.page(1)
#     except EmptyPage:
#         songs = paginator.page(paginator.num_pages)

#     serializer = SongSerializer(songs, many=True)
#     return Response({
#         'songs': serializer.data,
#         'page': songs.number,
#         'pages': paginator.num_pages,
#     })



# @api_view(['GET'])
# def get_top_songs(request):
#     songs = Song.objects.filter(rating__gte=4).order_by('-rating')[:5]
#     serializer = SongSerializer(songs, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_song(request, pk):
#     song = get_object_or_404(Song, _id=pk)
#     serializer = SongSerializer(song)
#     return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAdminUser])
# def create_song(request):
#     user = request.user
#     song = Song.objects.create(user=user, title='Sample Title')

#     serializer = SongSerializer(song)
#     return Response(serializer.data)


# @api_view(['PUT'])
# @permission_classes([IsAdminUser])
# def update_song(request, pk):
#     song = get_object_or_404(Song, id=pk)
#     serializer = SongSerializer(instance=song, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def delete_song(request, pk):
#     song = get_object_or_404(Song, id=pk)
#     song.delete()
#     return Response('Song deleted')


# @api_view(['POST'])
# def upload_image(request):
#     data = request.data
#     song_id = data.get('song_id')
#     song = get_object_or_404(Song, id=song_id)

#     song.image = request.FILES.get('image')
#     song.save()

#     return Response('Image uploaded')


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_song_review(request, pk):
#     user = request.user
#     song = get_object_or_404(Song, _id=pk)
#     data = request.data

#     review = Review.objects.create(
#         user=user,
#         song=song,
#         rating=data['rating'],
#         comment=data['comment'],
#     )

#     reviews = song.review_set.all()
#     song.num_reviews = len(reviews)
#     song.save()

#     return Response('Review added')