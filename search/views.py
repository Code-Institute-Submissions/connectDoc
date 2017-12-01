
from django.shortcuts import render
from django.db.models import Q

from medicalPractice.models import Doctor, MedicalPractice
 
def do_search(request):
    practices = MedicalPractice.objects.filter(name__icontains=request.GET['search_box'])
    doctors = Doctor.objects.filter(name__icontains=request.GET['search_box'])
    return render(request, "results.html", {"practices": practices,"doctors": doctors})
    
def your_view(request):
    if request.method == 'GET': search_query = request.GET('search_box', None)

# def do_search(request):
#     # medicalPractice = Doctor.objects.filter(name__icontains=query_string, address__icontains=query_string==request.GET['q'])
#     return render(request, "results.html", {"medicalPractice": medicalPractice})
    

# def do_search(request):
#     query_string = ''
#     found_entries = None
#     if ('q' in request.GET) and request.GET['q'].strip():
#         query_string = request.GET['q']
#         entry_query = get_query(query_string, ['field1', 'field2', 'field3'])
#         found_entries = Model.objects.filter(entry_query).order_by('-something')

#     return render_to_response('app/template-result.html',
#             { 'query_string': query_string, 'found_entries': found_entries },
#             context_instance=RequestContext(request)
#         )