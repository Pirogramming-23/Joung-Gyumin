from django.shortcuts import render, redirect
from .models import Idea, IdeaStar
from .forms import IdeaForm, DevToolForm
from django.shortcuts import get_object_or_404
from .models import DevTool
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

# Create your views here.
def idea_list(request):
    order = request.GET.get('order', 'created_at')  # 기본은 최신순
    if order == 'interest':
        ideas = Idea.objects.all().order_by('-interest')
    elif order == 'title':
        ideas = Idea.objects.all().order_by('title')
    elif order == 'created_at':
        ideas = Idea.objects.all().order_by('-created_at')
    else:
        ideas = Idea.objects.all()
    
    if request.user.is_authenticated:
        user_starred_ids = IdeaStar.objects.filter(user=request.user).values_list('idea_id', flat=True)
    else:
        user_starred_ids = request.session.get('starred_ideas', [])
    
    for idea in ideas:
        idea.is_starred = idea.id in user_starred_ids

    paginator = Paginator(ideas, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'ideas': ideas,
        'order' : order,
    }
    return render(request, 'ideas/idea_list.html', context)


def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', idea_id=idea.id)
    else:
        form = IdeaForm()

    return render(request, 'ideas/idea_form.html', {'form': form})

def idea_detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)

    if request.user.is_authenticated:
        is_starred = IdeaStar.objects.filter(user=request.user, idea=idea).exists()
    else:
        starred_ids = request.session.get('starred_ideas', [])
        is_starred = idea.id in starred_ids

    idea.is_starred = is_starred 

    return render(request, 'ideas/idea_detail.html', {'idea': idea})

def idea_update(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', idea_id=idea.id)
    else:
        form = IdeaForm(instance=idea)

    return render(request, 'ideas/idea_form.html', {'form': form})

def idea_delete(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')
    return render(request, 'ideas/idea_confirm_delete.html', {'idea': idea})

def devtool_list(request):
    tools = DevTool.objects.all()
    return render(request, 'ideas/devtool_list.html', {'tools': tools})


def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            tool = form.save()
            return redirect('devtool_detail', tool_id=tool.id)
    else:
        form = DevToolForm()

    return render(request, 'ideas/devtool_form.html', {'form': form})

def devtool_detail(request, tool_id):
    tool = get_object_or_404(DevTool, id=tool_id)
    ideas = tool.ideas.all()  

    context = {
        'tool': tool,
        'ideas': ideas,
    }
    return render(request, 'ideas/devtool_detail.html', context)

def devtool_update(request, tool_id):
    tool = get_object_or_404(DevTool, id=tool_id)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('devtool_detail', tool_id=tool.id)
    else:
        form = DevToolForm(instance=tool)

    return render(request, 'ideas/devtool_form.html', {'form': form})

def devtool_delete(request, tool_id):
    tool = get_object_or_404(DevTool, id=tool_id)
    if request.method == 'POST':
        tool.delete()
        return redirect('devtool_list')
    return render(request, 'ideas/devtool_confirm_delete.html', {'tool': tool})


@csrf_exempt
def toggle_star(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)

    if request.user.is_authenticated:
        starred, created = IdeaStar.objects.get_or_create(user=request.user, idea=idea)
        if not created:
            starred.delete()
            is_starred = False
        else:
            is_starred = True
    else:
        starred_ideas = request.session.get('starred_ideas', [])
        if idea_id in starred_ideas:
            starred_ideas.remove(idea_id)
            is_starred = False
        else:
            starred_ideas.append(idea_id)
            is_starred = True
        request.session['starred_ideas'] = starred_ideas

    return JsonResponse({'is_starred': is_starred})

@require_POST
@csrf_exempt 
def adjust_interest(request, idea_id):
    try:
        idea = Idea.objects.get(id=idea_id)
        action = request.POST.get('action')

        if action == 'increment':
            idea.interest += 1
        elif action == 'decrement' and idea.interest > 0:
            idea.interest -= 1

        idea.save()
        return JsonResponse({'success': True, 'interest': idea.interest})
    except Idea.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Idea not found'})
