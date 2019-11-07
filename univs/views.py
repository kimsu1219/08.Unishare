from django.shortcuts import render
from univs.models import UsRoominfo, UsUser
from django.http import HttpResponse
# Create your views here.

# index page is main Page
# It shows the room that someone can use.
# It is possible to select room.
def index(request):
    roominfo_101 = UsRoominfo.objects.filter(us_roomname = '101')
    roominfo_102 = UsRoominfo.objects.filter(us_roomname = '102')
    roominfo_103 = UsRoominfo.objects.filter(us_roomname = '103')
    context = {'roominfo_101' : roominfo_101, 'roominfo_102' : roominfo_102, 'roominfo_103' : roominfo_103}
    return render(request, 'univs/index.html', context)

# def userInfo(request, roominfo, roomtime):
#     context = {'roomname':roominfo, 'roomtime': roomtime}
#     return render(request, 'univs/userinfo.html', context)

def userInfo(request, roominfo, roomtime):
    context = {'roomname' : roominfo, 'roomtime' : roomtime}
    return render(request, 'univs/userinfo.html', context)

def getPassword(request):
    roomname= request.POST['roomname']
    roomtime = request.POST['roomtime']
    useremail = request.POST['useremail']
    username = request.POST['username']
    userdepartment = request.POST['userdepartment']
    use = request.POST['use']

    appuser = UsUser(us_name = username, us_email = useremail, us_department = userdepartment,
                    us_roomname =roomname, us_roomtime=roomtime)
    appuser.save()
    q = UsRoominfo.objects.filter(us_roomtime=roomtime).get(us_roomname=roomname)
    q.us_use = 0
    q.save()


    password = q


    context = {'password' : password}
    return render(request, 'univs/getpassword.html', context)
	# appuser.save()
