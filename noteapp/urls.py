from django.urls import path
from .import views

urlpatterns = [
    path('notes/',views.notes,name='notes'),
    path('notes/<slug:slug>/',views.note_detail,name='note_detail'),
    path('notes-search/',views.search_notes,name='notes-search'),
]

# endpoints:
# GET_ALL_NOTES and CREATE_NEW_NOTE= 'http://127.0.0.1:8000/notes/'
# GET_ANY_ONE_NOTE and UPDATE, DELETE= 'http://127.0.0.1:8000/notes/slug/'
# slug is in object(specific for each object)