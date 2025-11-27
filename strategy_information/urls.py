from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_strategy, name="add_strategy"),
    path("strategy/<int:pk>/", views.strategy_detail, name="strategy_detail"),
    path("contact/", views.contact, name="contact"),
]