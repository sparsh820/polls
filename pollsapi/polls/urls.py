from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from .views import PollViewSet

router = DefaultRouter()
router.register('polls-router', PollViewSet, basename='polls')
urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail"),
    path("Polls-class/", PollList.as_view(), name="polls_list"),
    path("Polls-class/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("Polls-generic/", PollListGen.as_view(), name="polls_list"),
    path("Polls-generic/<int:pk>/", PollDetailGen.as_view(), name="polls_detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    path("choices-del/<int:pk>/", ChoiceListDel.as_view(), name="choice_list_del"),  # Corrected line
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]
urlpatterns += router.urls