from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from base.models import Profile, Review, User
from base.serializers import ProfileSerializer, ReviewSerializer

import mimetypes
import os

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profiles(request):
    user = request.user
    query = request.query_params.get('keyword')
    if query is None:
        query = ''

    profiles = Profile.objects.filter(
        user=user,
        headline__icontains=query
    ).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(profiles, 5)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        profiles = paginator.page(1)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)

    if page is None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = ProfileSerializer(profiles, many=True)
    return Response({'profiles': serializer.data, 'page': page, 'pages': paginator.num_pages})

@api_view(['GET'])
def get_profiles(request):
    query = request.query_params.get('keyword')
    if query is None:
        query = ''

    profiles = Profile.objects.filter(
        headline__icontains=query).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(profiles, 5)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        profiles = paginator.page(1)
    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)

    if page is None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = ProfileSerializer(profiles, many=True)
    return Response({'profiles': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def get_top_profiles(request):
    profiles = Profile.objects.filter(rating__gte=4).order_by('-rating')[:5]
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_profile_details(request, pk):
    profile = Profile.objects.get(_id=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_profile(request):
    user = request.user
    is_verified = request.data['isVerified']

    profile = Profile.objects.create(
        user=user,
        email=user,
        isVerified=is_verified,
        headline='Sample Job',
        image=None,
        description='Sample Job Description',
        rating=None,
        numReviews=0,
        createdAt='Sample Date of Job'
    )

    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)



# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_profile(request, pk):
#     profile = get_object_or_404(New, id=pk)
#     serializer = profileerializer(instance=profile, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_profile(request, pk):
    user = request.data
    data = request.data
    profile = Profile.objects.get(_id=pk)

    # Check if the authenticated user is the owner of the profile item
    if request.user != profile.user:
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    profile.isVerified = data['isVerified']

    profile.headline = data['headline']
    profile.description = data['description']
    profile.category = data['category']

    profile.save()

    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_profile(request, pk):
    profile = get_object_or_404(Profile, _id=pk)

    # Check if the authenticated user is the owner of the profile
    if request.user != profile.user:
        return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

    profile.delete()
    return Response('Profile deleted')



@api_view(['POST'])
def upload_image(request):
    data = request.data

    profile_id = data['profile_id']
    profile = Profile.objects.get(_id=profile_id)

    profile.image = request.FILES.get('image')
    profile.save()

    return Response('Image was uploaded')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_profile_review(request, pk):
    user = request.user
    profile = get_object_or_404(Profile, _id=pk)
    data = request.data

    # Create the review
    review = Review.objects.create(
        user=user,
        name=user,
        profile=profile,
        rating=None,
        comment=data.get('comment', ''),
    )

    reviews = profile.review_set.all()
    profile.num_reviews = len(reviews)
    profile.save()

    return Response('Review added')




@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile_review(request, pk):
    user = request.user
    review = get_object_or_404(Review, _id=pk, user=user)
    data = request.data
    review.rating = data['rating']
    review.comment = data['comment']
    review.save()

    profile = review.profile
    reviews = profile.review_set.all()
    profile.num_reviews = len(reviews)
    profile.save()

    return Response('Review updated')

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_profile_review(request, pk):
    user = request.user
    review = get_object_or_404(Review, _id=pk, user=user)
    profile = review.profile
    review.delete()
    reviews = profile.review_set.all()
    profile.num_reviews = len(reviews)
    profile.save()

    return Response('Review deleted')

@api_view(['GET'])
def get_user_profile_reviews(request):
    user = request.user
    reviews = user.profile_review_set.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
