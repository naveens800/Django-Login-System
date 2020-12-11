from django.shortcuts import render
from .forms import QuestionForm
from django.core.paginator import Paginator
# my_helper functions for views
from .helperFunctions import  handleQuesTypes, checkAvailability


#created at global scope, so that can access this variable
questionsList = []

"""Create your views here."""

# provides home page
def home(request):
    return render(request, 'searchQuestions/home.html')


# handles query form 
def handleQueryForm(request):
    #if query form is submitted
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # retrieve fields from request
            question_type = request.POST.get('question')
            ids = request.POST.get('ids')
            form.save(commit=True)
            # list of objects
            global questionsList
            # returns list/None after handling a requested query
            questionsList = handleQuesTypes(question_type, ids)
            # returns True/False for data availability
            print(checkAvailability(questionsList))
            # if data is available
            if(checkAvailability(questionsList)):
                context = {"msg": "Query is Saved successfully"}
            #if there is no data
            else:
                context = {'msg2':"Query cannot be processed cause, there is no such content available"}
            return render(request, 'searchQuestions/success.html', context)
    else:
        # if query form is requested
        form = QuestionForm()
        context = {'form': form, 'default':"'default' means simply Get all questions on the site."}
        return render(request, 'searchQuestions/index.html', context)



# handles the pagination of results
def paginateResults(request):
    if request.method == "GET":
        paginator = Paginator(questionsList, 25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}
        return render(request, 'searchQuestions/searchResults.html', context)
