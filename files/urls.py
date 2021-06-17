from django.urls import path
from .views import DispositionView

urlpatterns = [
    path('lib/', DispositionView.as_view(), name='download_path'),
]
