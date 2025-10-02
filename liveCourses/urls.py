from django.urls import path
from . import views

urlpatterns = [
    path("data-engineer/", views.DataEngineer, name="data_engineer"),
    path("python-developer/", views.pythonDeveloper, name="python_developer"),
    path("data-analysis/", views.dataAnalysis, name="data_analysis"),
    path("data-science/", views.dataScience, name="data_science"),
    path("machine-learning/", views.machineLearning, name="machine_learning"),
    path("deep-learning/", views.deepLearning, name="deep_learning"),
    path("python-backend/", views.pythonBackend, name="python_backend"),
    path("statistics/", views.statistics, name="statistics"),
]
