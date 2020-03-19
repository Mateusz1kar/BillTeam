from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Person,Project,Notification

# Create your views here.

class PersonList(generic.ListView):
    template_name = 'polls/person.html'
    context_object_name = 'person'

    def get_queryset(self):
        return Person.objects.order_by('idPerson')



def index (request):
    return HttpResponse("Hello, world. You're at the polls index.")



class  DetailPerson(generic.DetailView):
    template_name = 'polls/detailPerson.html'
    context_object_name = 'person'

    def get_queryset(self):
        return Person.objects.order_by('idPerson')
    #person = Person.objects.filter(idPerson=pk).first()



    #person2 = get_object_or_404(Person, idPerson=idPerson)


def  addPerson(request):
    return render(request, 'polls/addPerson.html')


def personFormExecute(request):
    try:
        person2 = get_object_or_404(Person, idPerson=request.POST['id'])
        person2.firstName = request.POST['fname']
        person2.lastName = request.POST['lname']
        person2.login = request.POST['login']
        person2.password = request.POST['password']
        person2.position = request.POST['position']
        #pom = False
        try:
            if (request.POST['czyA']):
                pom = True
        except:
            pom = False
        person2.admin = pom

    except (KeyError, Person):
        # Redisplay the question voting form.
        return render(request, 'polls/detailPerson.html', {
            'person': person2,
            'error_message': "You didn't select a choice.",
        })
    else:

        person2.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:detailPerson', args=(person2.idPerson,)))


def personFormDeleteExecute(request):
    try:
        person2 = get_object_or_404(Person, idPerson=request.POST['id'])

    except (KeyError, Person):
        # Redisplay the question voting form.
        return render(request, 'polls/detailPerson.html', {
            'person': person2,
            'error_message': "You didn't select a choice.",
        })
    else:

        person2.delete()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:personList'))

def addPersonFormExecute(request):
    #pom = False
    try:
        if (request.POST['czyA']):
             pom = True
    except:
        pom = False

    person2 = Person()
    #person = Person(firstName=request.POST['fname'], lastName=request.POST['lname'], login = request.POST['login'], password=request.POST['password'], position=request.POST['position'], admin= pom)

    person2.firstName = request.POST['fname']
    person2.lastName = request.POST['lname']
    person2.login = request.POST['login']
    person2.password = request.POST['password']
    person2.position = request.POST['position']
    person2.admin = pom

    person2.save()
    return HttpResponseRedirect(reverse('polls:personList'))


def detailProject(request, idProject):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % idProject)

def detailNotification(request, idNotification):
    return HttpResponse("You're voting on question %s." % idNotification)




class ProjectList(generic.ListView):
    template_name = 'polls/ProjectList.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.order_by('idProject')

