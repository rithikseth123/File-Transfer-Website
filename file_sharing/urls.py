from django.urls import path
from . import views

# app_name = 'file_sharing'

urlpatterns = [
    path("", views.IndexView.as_view(), name="main-page"),
    path("upload/", views.upload_file, name="upload-file"),
    path("share/<str:unique_identifier>/", views.share_link, name="share-link"),
    # path("share/<int:id>/", views.share_link, name="share-link"),
]
