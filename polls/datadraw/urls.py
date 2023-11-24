from django.urls import path
from .views import IndexView, ResultsView

urlpatterns = [
path('', IndexView, name='home'),
path('results/', ResultsView, name='results'),
]