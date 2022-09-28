from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from company.models import Company
from django.db.models import Q


def index(request):
    try:
        key = request.GET['key']
        key = key.strip()
        companies = Company.objects.filter(
            Q(company_name__icontains=key) |
            Q(source__icontains=key) |
            Q(link__icontains=key) |
            Q(date__icontains=key) |
            Q(filepath__icontains=key) |
            Q(filename__icontains=key) |
            Q(search_term__icontains=key)).order_by('-date')

    except Exception as e:
        companies = Company.objects.all().order_by('-date')
        key = ''

    p = Paginator(companies, 25)
    page_number = request.GET.get('page')

    try:
        page_data = p.get_page(page_number)

    except PageNotAnInteger:
        page_data = p.page(1)

    except EmptyPage:
        page_data = p.page(p.num_pages)

    context = {
        'companies': page_data,
        'key': key,
    }
    return render(request, 'index.html', context)


def company_info(request, company_id):
    company_info = Company.objects.get(pk=company_id)

    company_info.reading_count = company_info.reading_count + 1
    company_info.save()

    diction = {'company_info': company_info}
    return render(request, 'company_info.html', context=diction)
