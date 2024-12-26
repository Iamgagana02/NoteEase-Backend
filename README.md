
Backend Project - NoteEase-Django rest framework project
This is a Django-based backend project for managing notes. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on notes, as well as search for notes using various filters. The project uses Django Rest Framework (DRF) and is designed for ease of use and scalability.

Features
Create new notes with details such as title, body, and category.
Retrieve all notes or a specific note by its unique slug.
Update and delete notes based on their slug.
Search for notes based on title, body, or category.

Endpoints
1. GET_ALL_NOTES and CREATE_NEW_NOTE
URL: http://127.0.0.1:8000/notes/
Methods:
GET: Fetch all notes.
POST: Create a new note by providing the following data:
title: The title of the note.
body: The content of the note.
category: The category of the note (e.g., Business, Personal, Important).
Example Request (POST):
json
Copy code
{
  "title": "Meeting Notes",
  "body": "Discussed project deadlines and next steps.",
  "category": "Business"
}
Example Response (GET):
json
Copy code
[
  {
    "title": "Meeting Notes",
    "body": "Discussed project deadlines and next steps.",
    "category": "Business",
    "slug": "meeting-notes"
  },
  {
    "title": "Workout Plan",
    "body": "Daily cardio and strength training.",
    "category": "Personal",
    "slug": "workout-plan"
  }
]
2. GET_ANY_ONE_NOTE, UPDATE, DELETE
URL: http://127.0.0.1:8000/notes/slug/
Methods:
GET: Retrieve a specific note by its slug.
PUT: Update an existing note by its slug with the following data:
title: The updated title.
body: The updated content.
category: The updated category.
DELETE: Delete a specific note by its slug.
Example Request (PUT):
json
Copy code
{
  "title": "Updated Meeting Notes",
  "body": "Added new tasks and deadlines.",
  "category": "Business"
}
Example Response (GET):
json
Copy code
{
  "title": "Meeting Notes",
  "body": "Discussed project deadlines and next steps.",
  "category": "Business",
  "slug": "meeting-notes"
}
3. SEARCH_ANY_NOTE
URL: http://127.0.0.1:8000/notes-search/?search=${search}
Methods:
GET: Search for notes based on a query parameter (search) that can match the title, body, or category.
Example search queries:
?search=Business
?search=meeting
Example Request:
bash
Copy code
GET http://127.0.0.1:8000/notes-search/?search=Business
Example Response:
json
Copy code
[
  {
    "title": "Meeting Notes",
    "body": "Discussed project deadlines and next steps.",
    "category": "Business",
    "slug": "meeting-notes"
  }
]
Technologies Used
Python 3.12.0
Django 5.1.4
Django Rest Framework 3.15.2
django-cors-headers 4.6.0 for handling cross-origin requests.
