from django.urls import path
from .views import IndexView, ResultsView

urlpatterns = [
path('', IndexView, name='home'),
path('results/<int:pk>', ResultsView, name='results'),
]