from rest_framework import permissions
from django.shortcuts import render
from rest_framework import generics
from note_mgmt.models import NoteHistory
from .serializers import CreateNoteSerializers, ListNoteSerializers
# Create your views here.


class CreateNoteView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreateNoteSerializers
    queryset = NoteHistory.objects.all()


class ListNoteView(generics.ListAPIView):  
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListNoteSerializers

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return NoteHistory.objects.filter(user=user_id).order_by('created_at')


class RetrieveEditView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListNoteSerializers
    queryset = NoteHistory.objects.all()
    lookup_url_kwarg = 'pk'


class DeleteNoteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListNoteSerializers
    queryset = NoteHistory.objects.all()
    lookup_url_kwarg = 'pk'
