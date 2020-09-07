from django.urls import path
from my_note.views import *

urlpatterns = [
    path('', index, name='index-url'),
    path('add-contact/', add_contact, name='add-contact-url'),
    path('view-contact/<int:contact_id>/', view_contact, name='view-contact'),
    path('add-number/<int:contact_id>/', add_phone_number, name='add-number'),

    path('view-history/<int:contact_id>/', view_history, name='view-history'),
    path('add-history/<int:contact_id>/', add_history, name='add-history'),
]
