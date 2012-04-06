from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import LunchForm
import datetime
from models import Lunch

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def lunch(request):
    html  = "<html><header><title>Lunch Organizer</title></header>"
    html += "<body>"
    weekday_num = datetime.date.today().isoweekday()
    begin_curr_week_date = datetime.date.today()-datetime.timedelta(days=weekday_num-1)
    for i in range(5):
        html += "On "
        curr_date = begin_curr_week_date + datetime.timedelta(days=i)
        html += curr_date.strftime("%A ")
        lunch_suggestions = Lunch.objects.filter(date__exact=curr_date)
        if not lunch_suggestions:
            html += "nobody cooks."
        else:
            for lunch in lunch_suggestions:
                html += lunch.cook + " cooks at " + lunch.time.__str__() + "."
        html += "<br>"
    html += "</body>"
    html += "</html>"
    return HttpResponse(html)

def curr_week_lunch_list():
    weekday_num = datetime.date.today().isoweekday()
    begin_curr_week_date = datetime.date.today()-datetime.timedelta(days=weekday_num-1)
    
    lunch_list = []
    for i in range(12):
        curr_date = begin_curr_week_date + datetime.timedelta(days=i)
        if curr_date.isoweekday()>5:
            continue
        lunch_suggestions = Lunch.objects.filter(date__exact=curr_date)
        if not lunch_suggestions:
            new_lunch = Lunch()
            new_lunch.date = curr_date
            new_lunch.time = datetime.time(13,00) # lunch at 13:00
            #new_lunch.cook = "nobody"
            lunch_list.append(new_lunch)
        else:
            lunch_list.append(lunch_suggestions[0])
    return lunch_list
 
def lunch_template(request):    
    t = get_template('week_overview.html')
    html = t.render(Context({'lunch_list': curr_week_lunch_list()}))
    return HttpResponse(html)           

def edit_lunch_template(request,edit_pk):
    if  edit_pk == None:
        curr_lunch = Lunch()
    else:
        curr_lunch = Lunch.objects.get(pk=edit_pk)
        
    if request.method == 'POST':
        form = LunchForm(request.POST, instance=curr_lunch)
        if form.is_valid():
            edited_lunch = form.save(commit=False)            
            edited_lunch.save(force_update=True,force_insert=False)
            return HttpResponseRedirect('/lunch/')
    else:
        form = LunchForm(instance=curr_lunch)
    return render_to_response('new_lunch.html', {'form': form})    

def new_lunch_template(request,curr_date):
    if request.method == 'POST':
        form = LunchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/lunch/')
    else:
        new_lunch = Lunch()
        new_lunch.date = curr_date
        new_lunch.time = "13:00"
        form = LunchForm(instance=new_lunch)
    return render_to_response('new_lunch.html', {'form': form})