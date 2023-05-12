# from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .models import rfp_bk
from django.urls import reverse


# github #2
def rfp_kb(request, obj_id=0):
    # print(request.POST.get('id'))
    name = "" #rfp_name
    q = "" #question
    a = "" # answer
    p = ""  # product 
    v="" #product_variant
    if obj_id > 0:
        selected_item = rfp_bk.objects.filter(id=obj_id).values()
        name = selected_item[0]["rfp_name"]
        q = selected_item[0]["question"]
        a = selected_item[0]["answer"]
        p = selected_item[0]["product"]
        v = selected_item[0]["product_variant"]
    template = loader.get_template('main.html')
    context = {
        "rfp_name": name,
        "question": q,
        "answer": a,
        "product":p,
        "product_variant":v,
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
    print (request)
    q = request.POST.get('txtQuestion')
    a = request.POST.get('txtAnswer')
    print(f"Question:{q} / Answer:{a}")
    # mydata = Member.objects.all()
    elems = rfp_bk.objects.filter(question__icontains=q, answer__icontains=a).values()
    template = loader.get_template('rfp_qa_list.html')
    context = {
        "elems": elems,
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def rfp_addrecord(request):
    name = request.POST.get('txtRfp')
    q = request.POST.get('txtQuestion')
    a = request.POST.get('txtAnswer')
    p = request.POST.get('txtProduct')
    v= request.POST.get('txtProductVariant')
    t = "" #topic
    wl = True #winloss
    c = True #comply
    print(f"question:{q} - answer:{a}")
    rfp = rfp_bk(rfp_name=name,question=q,answer = a, product = p, product_variant =v, topic=t, winLoss=wl, comply=c)
    rfp.save()
    return HttpResponseRedirect(reverse('rfp_qa_list'))

    
