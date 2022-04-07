from django.urls import path

from imager import views as imagerViews

urlpatterns = [
    path('add/',imagerViews.ImagerView.as_view()),
    path('image/',imagerViews.GetImagerView.as_view()),
    path('image/<int:id>/',imagerViews.GetImagerView.as_view()),
    path('login/',imagerViews.Login.as_view()),
    path('logout/',imagerViews.Logout.as_view()),
]
