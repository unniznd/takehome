from django.urls import path

from imager import views as imagerViews

urlpatterns = [
    path('add/',imagerViews.ImagerView.as_view()),
    path('add/<int:id>/',imagerViews.ImagerView.as_view()),
    path('login/',imagerViews.Login.as_view()),
    path('logout/',imagerViews.Logout.as_view())
]
