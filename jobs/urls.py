from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),

    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),

    path('applicants/', views.applicant_list, name='applicant_list'),
    path('applicants/<int:applicant_id>/', views.applicant_detail, name='applicant_detail'),

    path('jobs/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
]
