
from django.shortcuts import render
from django.db.models import Q

from medicalPractice.models import Doctor
 
def do_search(self, request, search_text, format=None, **kwargs):
        medicalPractice = Doctor.objects.filter(search_tags__contains=search_text==request.GET['search_box']) | Q(auto_tags__contains=search_text)
        return render(request, "results.html", {"medicalPractice": medicalPractice})
    
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