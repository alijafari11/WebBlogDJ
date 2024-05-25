from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def test(request):
    return render(request, 'blog/test.html')


def post_list(request, tag_slug=None):
    posts = Post.published.all()
    tag = None
    if tag_slug:
        tag = Tag.objects.get(slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    # PAGINATOR
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page,
        'tag': tag
    }
    return render(request, 'blog/post/list.html', context)

# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'


def post_detail(request, slug, pk):
    post = get_object_or_404(Post, status='published', slug=slug, id=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(similar_count=Count('tags')).order_by('-similar_count', '-publish')
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'similar_posts': similar_posts,
    }
    return render(request, 'blog/post/detail.html', context)


def user_account(request):
    user = request.user
    try:
        account = Account.objects.get(user=user)
    except:
        account = Account.objects.create(user=user)
    if request.method == "POST":

        form = AccountForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['f_name']
            user.last_name = form.cleaned_data['l_name']
            account.sex = form.cleaned_data['sex']
            account.address = form.cleaned_data['address']
            account.age = form.cleaned_data['age']
            account.phone = form.cleaned_data['phone']
            user.save()
            account.save()
            return redirect('blog:home')
        else:
            return render(request, 'blog/forms/account_form.html', {'form': form, 'account': account})
    form = AccountForm()
    return render(request, 'blog/forms/account_form.html', {'form': form, 'account': account})


def contactus(request):
    sent = False
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            name = cd['name']
            email = cd['email']
            phone = cd['phone']
            message = cd['message']
            msg = f"name: {name} \nphone: {phone} \nemil: {email}\n message: \n{message}"
            send_mail(subject, msg, 'pvali.jafari@outlook.com', ['pvali.jafari@gmail.com'], fail_silently=False)
            sent = True
    else:
        form = ContactUsForm()

    return render(request, 'blog/forms/contact-us.html', {'form': form, 'sent': sent})


def share_post(request, post_id):
    post = get_object_or_404(Post, status='published',id=post_id)
    sent = False
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'''{cd['name']} شما را به خواندن {post.titles}  دعوت کرده است. '''
            message = cd['message']
            msg = f'''{cd['name']} شما را به خواندن {post.titles} در ادرس زیر دعوت کرده است: 
            {message}
            {post_url}
            '''
            send_mail(subject, msg, 'pvali.jafari@outlook.com', [cd['to']], fail_silently=False)
            sent = True
    else:
        form = ShareForm()

    return render(request, 'blog/forms/share-post.html', {'form': form, 'sent': sent, 'post': post})
