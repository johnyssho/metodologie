from django.urls import path
from .views import IndexView, ResultsView, AddRandView, DeleteChoicesView

urlpatterns = [
path('', IndexView, name='home'),
path('results/<int:pk>', ResultsView, name='results'),
path('random/<int:pk>', AddRandView, name='random'),
path('delete_all_choices', DeleteChoicesView, name='delete_all_choices'),
]