from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Content, CommissionMembers


def messageSend(num, text):
    """
    :param num : Notification number (1: 'danger', 2: 'info', 3: 'success')
    :param text: Message text
    :return: Message
    """

    alert = {1: 'danger', 2: 'info', 3: 'success'}
    if num != 1 and num != 2 and num != 3:
        num = 1
        text = "Error. Wrong number of alert!"
    message = '''
                <div class="alert alert-{} alert-dismissible fade show" role="alert" align="center">
                    <b>{}</b>: {}
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
              '''.format(alert[num], alert[num].title(), text)
    return message


# Create your views here.

def index(request):
    content = {
        "title": "HomePage",
    }
    return render(request, "index.html", content)


def photos(request):
    return HttpResponse("<h1>Photos</h1>")


def contacts(request):
    if request.method == "POST":
        content = {
            "title": "Contacts",
            "message": messageSend(3, "OK"),
            "post": {
                'name': request.POST.get("name"),
                'theme': request.POST.get("theme"),
                'email': request.POST.get("email"),
                'text': request.POST.get("message")
            },
        }
        # for field in content["post"]:
        #     if content["post"][field] is None:
        #         content["message"] = messageSend(2, "The field '{}' is None".format(field))

        return render(request, "contacts.html", content)

    content = {
        "title": "Contacts",
    }
    return render(request, "contacts.html", content)


def work(request):
    # if Content.objects.filter(categoryId=1):
    #     query = Content.objects.filter(categoryId=1)
    # else:
    #     query = None
    query = Content.objects.all
    content = {
        "title": "Work of the CKKT",
        "objectList": query,
    }
    return render(request, "work.html", content)


def members(request):
    query = CommissionMembers.objects.all
    content = {
        "title": "Members of the CKKT",
        "objectList": query,
    }
    return render(request, "members.html", content)


def disciplines(request):
    content = {
        "title": "Disciplines",
    }
    return render(request, "disciplines.html", content)


def specialities(request):
    content = {
        "title": "Specialities",
    }
    return render(request, "specialities.html", content)


def clubs(request):
    pass


