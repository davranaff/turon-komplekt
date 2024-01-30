from django.shortcuts import render, redirect
from django.core.mail import send_mail

from app.models import *
from app.utils.get_datas import get_home_datas, get_detail_data, get_all_products

# Create your views here.
def index(request):
    path = request.path

    if 'ru' in path:
        datas = get_home_datas({
            'info': Info,
            'project': Project,
            'certificate': Certificate,
            'object': Objects,
            'branch': Branch,
            'trust': Trust,
        }, lc_type='ru')
        return render(request, 'index.html', datas)

    if 'en' in path:
        datas = get_home_datas({
            'info': Info,
            'project': Project,
            'certificate': Certificate,
            'object': Objects,
            'branch': Branch,
            'trust': Trust,
        }, lc_type='en')
        return render(request, 'index.html', datas)

    if 'uz' in path:
        datas = get_home_datas({
            'info': Info,
            'project': Project,
            'certificate': Certificate,
            'object': Objects,
            'branch': Branch,
            'trust': Trust,
        }, lc_type='uz')
        return render(request, 'index.html', datas)


def detail(request, slug):
    path = request.path

    if 'ru' in path:
        datas = get_detail_data({'project': Project}, 'ru', slug)
        info = get_home_datas({
            'info': Info,
            'project': Project,
            'certificate': Certificate,
            'object': Objects,
            'branch': Branch,
            'trust': Trust
        }, lc_type='ru')
        return render(request, 'detail_page.html', {**info, **datas})

    if 'en' in path:
        datas = get_detail_data({'project': Project}, 'en', slug)
        info = get_home_datas({
            'info': Info,
            'project': Project,
            'certificate': Certificate,
            'object': Objects,
            'branch': Branch,
            'trust': Trust
        }, lc_type='en')
        return render(request, 'detail_page.html', {**info, **datas})

    if 'uz' in path:
        datas = get_detail_data({'project': Project}, 'uz', slug)
        info = get_home_datas({
            'info': Info,
            'project': Project,
            'certificate': Certificate,
            'object': Objects,
            'branch': Branch,
            'trust': Trust
        }, lc_type='uz')
        return render(request, 'detail_page.html', {**info, **datas})


def all_products(request):
    path = request.path

    if 'ru' in path:
        datas = get_all_products(model={'project': Project}, lc_type='ru')
        return render(request, 'all_products.html', datas)

    if 'en' in path:
        datas = get_all_products(model={'project': Project}, lc_type='en')
        return render(request, 'all_products.html', datas)

    if 'uz' in path:
        datas = get_all_products(model={'project': Project}, lc_type='uz')
        return render(request, 'all_products.html', datas)


def all_objects(request):

    objects = Objects.objects.all()
    return render(request, 'objects.html', {'objects': objects})


def feedback(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        text = request.POST.get('text')

        feedback_result = FeedBack.objects.create(name=name, telephone=phone, text=text)

        send_mail(
            "Yangi xabar pro-filter.uz dan",
            f"Qayta aloqa bo'limidan yangi zayavka\n\n"
            f"Ism: {feedback_result.name}\n"
            f"Telefon nomer: {feedback_result.telephone}\n"
            f"Xabar: {feedback_result.text}",
            from_email=None,
            recipient_list=['awalgroup0105@gmail.com',]
        )

        return redirect('/')

    return redirect('/')
