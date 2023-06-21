from django.urls import include, path


urlpatterns = [
    path("todo/", include("todo.urls")),
]

app_name = "api"
