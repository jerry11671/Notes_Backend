from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET'])
def getNote(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def viewNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    new_note = Note.objects.create(
        title=request.data['title'],
        body=request.data['body'],
    )
    serializer = NoteSerializer(new_note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    
    return Response("Item was deleted successfully!!")
    
    
    
    
    
    
# class NoteView(APIView):
#     def get(self, request):
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
    
#     def get(self, request, pk):
#         note = Note.objects.get(id=pk)
#         serializer = NoteSerializer(note, many=False)
#         return Response(serializer.data)
    
#     def post(self, request):
#         new_note = Note.objects.create(
#             title = request.data['title'],
#             body = request.data['body'],
#         )
#         serializer = NoteSerializer(new_note, many=True)
           
#         return Response(serializer.data)
        
            
    


