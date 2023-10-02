from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes),

    path('batches/', views.getAllBatches),
    path('batch/', views.getSelectedBatch),
    path('active_batch/', views.getActiveBatch),

    path('tags/', views.getAllTags),
    
    path('streams/', views.getBatchStreams),
    path('update_streams/', views.uploadData)

    
]