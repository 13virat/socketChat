"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Now, replace the code you have in project/urls.py with the following code. This will handle the chatbox name stated in the browser (http://127.0.0.1:8002/chat/**chatboxname**/).

from django.contrib import admin
from django.urls import path
from chat.views import chat_box

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/<str:chat_box_name>/", chat_box, name="chat"),
]