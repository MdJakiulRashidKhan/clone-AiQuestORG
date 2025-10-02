from django.shortcuts import render

# Create your views here.

def DataEngineer(request):
    return render(request, 'LiveCourses/DataEngineer.html')

def dataAnalysis(request):
    return render(request, 'LiveCourses/dataAnalysis.html') 
def dataScience(request):
    return render(request, 'LiveCourses/dataScience.html')
def machineLearning(request):
    return render(request, 'LiveCourses/machineLearning.html')
def deepLearning(request):
    return render(request, 'LiveCourses/deepLearning.html')
def pythonDeveloper(request):
    return render(request, 'LiveCourses/pythonDeveloper.html')
def pythonBackend(request):
    return render(request, 'LiveCourses/pythonBackend.html')
def statistics(request):
    return render(request, 'LiveCourses/statistics.html')
