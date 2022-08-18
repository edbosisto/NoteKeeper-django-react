from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer):
    model = Note
    fields = "__all__"
