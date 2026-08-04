from django.shortcuts import render
from datetime import date

def home(request):
    context = {
        'student_name': 'khadja',
        'projects': [
            {'title': 'Ojra', 'desc': 'Smart minibus payment system', 'year': 2025},
            {'title': 'Heart Disease Prediction', 'desc': 'ML pipeline using scikit-learn', 'year': 2025},
            {'title': 'Population Forecasting', 'desc': 'Egypt population growth model', 'year': 2026},
        ],
        'today': date.today(),
    }
    return render(request, 'pages/home.html', context)