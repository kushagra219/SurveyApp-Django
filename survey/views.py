from .models import Improvement, Survey
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST": # POST reuqest - Submit the form
        return form_submission(request)
    else: # GET Request - Access the webpage
        return render(request, 'survey/index.html')
    
def thank_you(request):
    return render(request, 'survey/thankyou.html')

# function to save form data in the database
def form_submission(request):
    name = request.POST["name"]
    email= request.POST["email"]
    age = request.POST["age"]
    role = request.POST["role"]
    recommendation = request.POST["recommendation"]
    language = request.POST["language"]

    improvements = []
    for key in request.POST.keys():
        if key.split("-")[0] == "improvement": 
            improvements.append(request.POST[key])

    # making the survey object
    suvery_obj = Survey.objects.create(name=name, email=email, age=age, current_role=role, 
                                                    recommendation=recommendation, fav_language=language)

    # as improvements is a different model, we have to add improvement_obj to improvements field of Survey model
    for i in improvements:
        improvement_obj = Improvement.objects.get(description=i)
        suvery_obj.improvements.add(improvement_obj)

    # save the survey_obj to the database
    suvery_obj.save()

    return redirect('survey:thank-you')

def survey_list(request):
    survey_responses = Survey.objects.all()
    context = {"survey_responses": survey_responses}
    return render(request, 'survey/survey_list.html', context=context)


