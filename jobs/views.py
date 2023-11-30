from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Company, Job, Applicant
from .forms import ApplicantForm


def company_list(request):
    companies = Company.objects.all()
    return render(request, 'main/company_list.html', {'companies': companies})


def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'main/company_detail.html', {'company': company})


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'main/job_list.html', {'jobs': jobs})


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'main/job_detail.html', {'job': job})


def applicant_list(request):
    applicants = Applicant.objects.all()
    return render(request, 'main/applicant_list.html', {'applicants': applicants})


def applicant_detail(request, applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    return render(request, 'main/applicant_detail.html', {'applicant': applicant})


def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.save()
            job.applicants.add(applicant)
            return HttpResponseRedirect('/jobs/')  # Redirect to job list after applying
    else:
        form = ApplicantForm()

    return render(request, 'main/apply_for_job.html', {'form': form, 'job': job})
