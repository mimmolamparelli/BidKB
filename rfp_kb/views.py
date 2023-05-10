# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .models import rfp_bk


def rfp_kb(request, obj_id=-1):
    # print(request.POST.get('id'))
    name = ""
    q = ""
    a = ""
    if obj_id > 0:
        selected_item = rfp_bk.objects.filter(id=obj_id).values()
        name = selected_item[0]["rfp_name"]
        q = selected_item[0]["question"]
        a = selected_item[0]["answer"]
    template = loader.get_template('main.html')
    context = {
        "rfp_name": name,
        "question": q,
        "answer": a,
    }
    return HttpResponse(template.render(context, request))


@csrf_protect
def test(request):
    value = request.POST.get('txtQuestion')
    print(f"Value={value}")
    template = loader.get_template('test.html')
    return HttpResponse(template.render())


@csrf_protect
def rfp_qa_list(request):
    q = request.POST.get('txtQuestion')
    a = request.POST.get('txtAnswer')
    print(f"Question:{q} / Answer:{a}")
    # mydata = Member.objects.all()
    elems = rfp_bk.objects.all().values()
    template = loader.get_template('rfp_qa_list.html')
    context = {
        "elems": elems,
    }
    return HttpResponse(template.render(context, request))
