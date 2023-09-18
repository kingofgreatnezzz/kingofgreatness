# blog/urls.py
from django.urls import path
from .views import *




# Path to each page.s
urlpatterns = [
    path('', index, name='index'),
    path('base', base, name='base'),
    path('blogcontent', blogcontent, name='blogcontent'),
    path('faq', faq, name='faq'),
    path('portfolio', portfolio, name='portfolio'),
    path('blogcontent', blogcontent, name='blogcontent'),
    path('contact', contact, name='contact'),
    path('fotter', fotter, name='fotter'),    
    path('features', features, name='features'),
]

