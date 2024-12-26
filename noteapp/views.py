from django.shortcuts import render
from .serializers import NoteSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def search_notes(request):
    query = request.query_params.get('search')
    notes = Note.objects.filter(
        Q(title__icontains=query) | 
        Q(body__icontains=query) | 
        Q(category__icontains=query)
    )
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def notes(request):
    # get all item
    if request.method=='GET':
        notes=Note.objects.all()
        serializer=NoteSerializer(notes,many=True)
        return Response(serializer.data)
    # post any item
    elif request.method=='POST':
        serializer=NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET','PUT','DELETE'])
def note_detail(request,slug):
    try:
        note=Note.objects.get(slug=slug)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # get any specific item --based on slug
    if request.method=='GET':
        serializer=NoteSerializer(note)
        return Response(serializer.data)
    # update any specific item --based on slug 
    elif request.method=='PUT':
        serializer=NoteSerializer(note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        # delete any item --based on slug
        if request.method=='DELETE':
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

