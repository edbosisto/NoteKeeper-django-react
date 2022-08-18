from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from NoteKeeper.api.models import Note

# Create your views here.

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    return Response("Notes")

