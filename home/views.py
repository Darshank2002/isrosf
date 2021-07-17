from django.shortcuts import render
from .models import MissionPost, Timeline, Rocket, Mission, MissionImage
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='3e05ac0218b34da39f0936f5c9542303')

articles = newsapi.get_everything(q='(ISRO) NOT (China OR NASA OR ESA OR spy case OR Recruitment) ',

                                  language='en',
                                  sort_by='relevancy',
                                  page=2)


def index(request):
    return render(request, 'index.html')


def rockets(request):
    return render(request, 'rockets.html')


def lv(request, code):
    rocket = Rocket.objects.filter(rocket_code=code).first()
    return render(request, 'Rockets/pslvT.html', {"rocket": rocket})


def missions(request):
    return render(request, 'missions.html')


def missionPage(request, Type, code):
    mission = Mission.objects.filter(mission_code=code).first()
    images = MissionImage.objects.filter(post=mission)
    return render(request, 'singleMission.html', {'mission': mission, 'images': images})


def spacecraft(request):
    return render(request, 'spacecraft.html')


def missionsTemp(request, Type):

    missions = Mission.objects.filter(mission_type=Type)
    missionType = missions[0].get_mission_type_display()

    return render(request, 'missionsHomeList.html', {"missions": missions, 'type': missionType})


def timeline(request):
    timeStamps = Timeline.objects.all()
    return render(request, 'timeline.html', {'timeStamps': timeStamps})


def news(request):

    return render(request, 'news.html', {"article": articles['articles']})
