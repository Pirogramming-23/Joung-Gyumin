from django.shortcuts import render, redirect
from .models import Post, Like, Comment, PostImage
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Count

# Create your views here.
def post_list(request):
    sort = request.GET.get('sort', 'latest')

    if sort == 'likes':
        posts = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')
    elif sort == 'comments':
        posts = Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')
    else:
        posts = Post.objects.all().order_by('-created_at')
    
    
    comments = Comment.objects.all().order_by('created_at')

    liked_post_ids = []
    if request.user.is_authenticated:
        liked_post_ids = Like.objects.filter(user=request.user).values_list('post_id', flat=True)

    return render(request, 'post/post_list.html', {
        'posts': posts,
        'liked_post_ids': liked_post_ids,
        'comments': comments,
        'current_sort': sort,
    })



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        images = request.FILES.getlist('images')  # 여러 파일 받기

        if form.is_valid():
            post = form.save(commit=False)   # 아직 저장하지 않음
            post.author = request.user       # 작성자 지정
            post.save()                      # 이제 저장

            for img in images:
                PostImage.objects.create(post=post, image=img)

            return redirect('post_list')

    else:
        form = PostForm()

    return render(request, 'post/create_post.html', {'form': form})


@login_required
@require_POST
def delete_comment_ajax(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author == request.user:
        comment.delete()
        return JsonResponse({'success': True})
    else :
        return JsonResponse({'success': False, 'error': '권한 없음'}, status=403)


@login_required
@require_POST
def toggle_like_ajax(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    liked = False

    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': post.likes.count()
    })

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author:
        return HttpResponseForbidden("삭제 권한이 없습니다.")

    post.delete()
    return redirect('post_list')


from django.contrib.auth.views import LogoutView

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt  
def add_comment_ajax(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content') or request.body.decode().split('content":"')[1].split('"')[0]
        post = get_object_or_404(Post, id=post_id)
        comment = Comment.objects.create(post=post, author=request.user, content=content)

        return JsonResponse({
            'success': True,
            'id': comment.id,
            'author': comment.author.username,
            'content': comment.content,
        })

    return JsonResponse({'success': False}, status=400)

class LogoutViewAllowGet(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)