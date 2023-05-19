# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .models import rfp_bk
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


def rfp_kb(request, obj_id=0):
    logger.debug("TEST LOGGER")
    # print(request.POST.get('id'))
    i = ""  #object id
    name = ""  #rfp_name
    q = ""  #question
    a = ""  # answer
    p = ""  # product
    v = ""  #product_variant
    wl = False
    c = False

    if obj_id > 0:
        selected_item = rfp_bk.objects.filter(id=obj_id).values()
        i = selected_item[0]["id"]
        name = selected_item[0]["rfp_name"]
        q = selected_item[0]["question"]
        a = selected_item[0]["answer"]
        p = selected_item[0]["product"]
        v = selected_item[0]["product_variant"]
        wl = selected_item[0]["winLoss"]
        c = selected_item[0]["comply"]
    template = loader.get_template('main.html')
    context = {
        "id": i,
        "rfp_name": name,
        "question": q,
        "answer": a,
        "product": p,
        "product_variant": v,
        "winLoss": wl,
        "comply": c,
    }
    return HttpResponse(template.render(context, request))


@csrf_protect
def test(request):
    value = request.POST.get('cbWinLoss')
    print(f"Value={value}")
    template = loader.get_template('test.html')
    return HttpResponse(template.render())


@csrf_protect
def rfp_qa_list(request):
    print(request)
    q = request.POST.get('txtQuestion')
    a = request.POST.get('txtAnswer')
    print(f"Question:{q} / Answer:{a}")
    # mydata = Member.objects.all()
    elems = rfp_bk.objects.filter(question__icontains=q,
                                  answer__icontains=a).values()
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
    v = request.POST.get('txtProductVariant')
    t = ""  #topic
    if request.POST.get("cbWinLoss") == "on":
        wl = True  #winloss
    else:
        wl = False
    if request.POST.get("cbComply") == "on":
        c = True  #comply
    else:
        c = False
    print(f"question:{q} - answer:{a}")
    rfp = rfp_bk(rfp_name=name,
                 question=q,
                 answer=a,
                 product=p,
                 product_variant=v,
                 topic=t,
                 winLoss=wl,
                 comply=c)
    rfp.save()

    elems = rfp_bk.objects.all().values()[:10]
    template = loader.get_template('rfp_qa_list.html')
    context = {
        "elems": elems,
    }
    return HttpResponse(template.render(context, request))

    # template = loader.get_template('main_view.html')
    # return HttpResponse(template.render())
    # return HttpResponseRedirect(main_view)


@csrf_protect
def rfp_updaterecord(request):
    name = request.POST.get('txtRfp')
    q = request.POST.get('txtQuestion')
    a = request.POST.get('txtAnswer')
    p = request.POST.get('txtProduct')
    v = request.POST.get('txtProductVariant')
    t = ""  #topic
    if request.POST.get("cbWinLoss") == "on":
        wl = True  #win
    else:
        wl = False  #loss
    if request.POST.get("cbComply") == "on":
        c = True  #comply
    else:
        c = False  #do not comply
    rfp = rfp_bk.objects.filter(id=request.POST.get("id")).values()
    rfp.update(rfp_name=name,
               question=q,
               answer=a,
               product=p,
               product_variant=v,
               topic=t,
               winLoss=wl,
               comply=c)

    elems = rfp_bk.objects.all().values()[:10]
    template = loader.get_template('rfp_qa_list.html')
    context = {
        "elems": elems,
    }
    return HttpResponse(template.render(context, request))


@csrf_protect
def rfp_deleterecord(request):
    rfp = rfp_bk.objects.filter(id=request.POST.get("id"))
    rfp.delete()
    template = loader.get_template('main_view.html')
    return HttpResponse(template.render())


def main_view(request):
    elems = rfp_bk.objects.all().values()[:10]
    context = {
        "elems": elems,
    }
    template = loader.get_template('main_view.html')
    return HttpResponse(template.render(context))
