from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Yousuf",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened...",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus feugiat, molestie ipsum et, ultricies diam. Nullam nec purus feugiat, molestie ipsum et, ultricies diam. Nullam nec purus feugiat, molestie ipsum et, ultricies diam."
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Yousuf",
        "date": date(2021, 7, 28),
        "title": "Programming Is Great!",
        "excerpt": "I've found programming to be really fun. I'm definitely going to continue learning more!",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus feugiat, molestie ipsum et, ultricies diam. Nullam nec purus feugiat, molestie ipsum et, ultricies diam. Nullam nec purus feugiat, molestie ipsum et, ultricies diam."
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Yousuf",
        "date": date(2021, 8, 5),
        "title": "Nature Walk",
        "excerpt": "Nature walks are really refreshing. I recommend getting out early in the morning!",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec purus feugiat, molestie ipsum et, ultricies diam. Nullam nec purus feugiat, molestie ipsum et, ultricies diam. Nullam nec purus feugiat, molestie ipsum et, ultricies diam."
    }
]

# Create your views here.


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
