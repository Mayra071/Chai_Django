from django.urls import path
from . import views
app_name = "chai"

urlpatterns = [
    # localhost:80001/chai
    path('', views.all_chai, name='all_chai'),

    # localhost:80001/chai/chai_detail
    path('chai<int:chai_id>/', views.chai_detail, name='chai_detail'),

    path('chai_stores/', views.chai_store_view, name='chai_stores'),
]
