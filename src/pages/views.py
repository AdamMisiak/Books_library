from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Avg, Value
from .models import UserImage
from .functions import find_fav
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import (
    RegisterForm,
    UpdateForm,
    BookOptionsForm,
    BookUpdateForm,
    NavbarSearchingForm,
    ImageUpdateForm,
    ReviewBookForm,
)
from django.apps import apps

# MODELS IMPORTED
Book = apps.get_model("books", "Book")
BookPosition = apps.get_model("books", "BookPosition")


def home_view(request, *args, **kwargs):
    book_with_reviews = BookPosition.objects.filter(review__isnull=False)

    paginator = Paginator(book_with_reviews, 4)
    page = request.GET.get("page")
    paged_book_with_reviews = paginator.get_page(page)

    # NAVBAR SEARCHING FORM HANDLING
    if request.POST:
        form = NavbarSearchingForm(request.POST)
        if form.is_valid():
            request.session["form"] = form.cleaned_data
            return HttpResponseRedirect(reverse("books:results"))
    else:
        form = NavbarSearchingForm()

    context = {
        "form": form,
        "book_with_reviews": paged_book_with_reviews,
    }
    return render(request, "home.html", context)


def about_view(request, *args, **kwargs):
    return render(request, "about.html")


def register_user_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            authenticate(username=username, password=raw_password)
            user = User.objects.get(username=username)
            image = UserImage(user=user)
            image.save()
            return redirect("/users/login")
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "users/register.html", context)


def login_user_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "users/login.html", context)


# DETAILS OF ACCOUNT VIEW
def account_view(request):
    user = User.objects.get(pk=request.user.id)
    books = user.books_added.all()

    context = {
        "user": user,
        "books": books,
    }
    return render(request, "users/account.html", context)


# UPDATE USER'S INFORMATION VIEW
def update_user_view(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        form = UpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:account"))
    else:
        form = UpdateForm(instance=request.user)
    context = {"form": form}
    return render(request, "users/update.html", context)


# LIBRARY OF USER'S BOOKS VIEW
def library_view(request):
    user = User.objects.get(pk=request.user.id)

    # FILTERING ONLY USER'S ADDED BOOKS
    users_book_positions = BookPosition.objects.filter(user=user, value="Add")
    books = user.books_added.all()

    context = {"books": books, "users_book_positions": users_book_positions}
    return render(request, "users/library.html", context)


# LIBRARY OF USER'S BOOKS VIEW
def user_library_view(request, id):

    # REVIEW'S USERNAME CLICKED
    user = User.objects.get(id=id)
    users_book_positions = BookPosition.objects.filter(user=user, value="Add")
    books = user.books_added.all()

    context = {
        "books": books,
        "users_book_positions": users_book_positions,
        "user": user,
    }
    return render(request, "users/user_library.html", context)


# USER'S CHALLENGE VIEW
def challenge_view(request):
    today = datetime.now()
    current_month = today.strftime("%B")

    user = User.objects.get(pk=request.user.id)
    books = user.books_added.all()

    users_book_positions = BookPosition.objects.filter(user=user, value="Add")

    context = {
        "current_month": current_month,
        "user": user,
        "books": books,
        "users_book_positions": users_book_positions,
    }

    return render(request, "users/challenge.html", context)


# ADD/DELETE BOOK TO USER'S LIBRARY VIEW
def add_book_view(request):
    if request.method == "GET":

        # READING BOOK ID FROM JQUERY SCRIPT
        book_id = request.GET["book_id"]
        book = Book.objects.get(id=book_id)

        # ADDING OR DELETING BOOK FROM USER'S LIBRARY
        if request.user in book.user.all():
            book.user.remove(request.user)
            book_position, created = BookPosition.objects.get_or_create(
                user=request.user, book=book
            )
            book_position.value = "Delete"
        else:
            book.user.add(request.user)
            book_position, created = BookPosition.objects.get_or_create(
                user=request.user, book=book
            )
            book_position.value = "Add"
        book_position.save()

        return HttpResponse("success")
    else:
        return HttpResponse("unsuccesful")


# DETAILS OF BOOK VIEW
def info_book_view(request):
    if request.method == "POST":
        form = BookOptionsForm(request.POST)
        if form.is_valid():

            # READING ID OF BOOK FROM FORM
            book_id = form.cleaned_data.get("id")
            request.session["book_id"] = book_id

            book = Book.objects.get(id=book_id)
            book_position = BookPosition.objects.get(user=request.user, book=book)

            book_title = book.title
            request.session["book_title"] = book_title

            context = {"book": book, "book_position": book_position}

            return render(request, "users/info_book.html", context)


# UPDATE BOOK'S INFORMATION VIEW
def update_book_view(request):
    if request.method == "POST":
        form = BookUpdateForm(request.POST)
        if form.is_valid():
            book_id = request.session["book_id"]
            book = Book.objects.get(id=book_id)
            book_position = BookPosition.objects.get(user=request.user, book=book)

            # SETTING GENRE, MONTH AND STATUS OF BOOK
            genre = form.cleaned_data.get("genre")
            month = form.cleaned_data.get("month")
            year = form.cleaned_data.get("year")
            status = form.cleaned_data.get("status")

            book_position.month = month
            book_position.year = year
            book_position.status = status
            book.genre_1 = genre

            book_position.save()
            book.save()
            return HttpResponseRedirect(reverse("users:library"))
    else:
        form = BookUpdateForm()

    context = {
        "form": form,
    }

    return render(request, "users/update_book.html", context)


# UPDATE USER'S IMAGE VIEW
def update_image_view(request):
    if request.method == "POST":
        form = ImageUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            userimage = UserImage.objects.get(user=user)
            userimage.image = request.FILES["image"]
            userimage.save()
            return HttpResponseRedirect(reverse("users:account"))
    else:
        form = ImageUpdateForm()
    return render(request, "users/update_image.html", {"form": form})


# REVIEW BOOK VIEW
def review_book_view(request):
    if request.method == "POST":
        form = ReviewBookForm(request.POST)
        if form.is_valid():
            book_id = request.session["book_id"]
            book = Book.objects.get(id=book_id)
            book_position = BookPosition.objects.get(user=request.user, book=book)

            # SETTING REVIEW
            review = form.cleaned_data.get("review")
            rate = form.cleaned_data.get("rate")
            book_position.review = review
            book_position.rate = rate
            book_position.save()

            return HttpResponseRedirect(reverse("users:library"))
    else:
        form = ReviewBookForm()

    context = {
        "form": form,
    }

    return render(request, "users/review_book.html", context)


# DELETE BOOK'S REVIEW VIEW
def delete_review_view(request):
    if request.method == "GET":

        # READING BOOK ID FROM JQUERY SCRIPT
        book_id = request.GET["book_id"]
        book = Book.objects.get(id=book_id)
        book_position = BookPosition.objects.get(user=request.user, book=book)

        book_position.review = None
        book_position.rate = 0
        book_position.save()

        return HttpResponse("success")
    else:
        return HttpResponse("unsuccesful")


# STATS OF USER VIEW
def stats_view(request):
    stats = {}
    user = User.objects.get(pk=request.user.id)

    # FILTERING ONLY USER'S ADDED BOOKS
    users_book_positions = BookPosition.objects.filter(user=user, value="Add")
    user_books = user.books_added.all()

    stats['Books in library'] = users_book_positions.count()
    stats['Books To Do'] = users_book_positions.filter(status="To do").count()
    stats['Books In Progress'] = users_book_positions.filter(status="In progress").count()
    stats['Books Done'] = users_book_positions.filter(status="Done").count()
    stats['Reviews written'] = users_book_positions.filter(review__isnull=False).count()
    stats['Average rate'] = round(list(users_book_positions.aggregate(Avg('rate')).values())[0], 2)
    stats['Favourite author'] = find_fav(users_book_positions, 'author')
    stats['Favourite genre'] = find_fav(users_book_positions, 'genre')
    stats['Favourite month'] = find_fav(users_book_positions, 'month')
    stats['Favourite year'] = find_fav(users_book_positions, 'year')

    
    context = {
        "stats": stats,
     }
    return render(request, "users/stats.html", context)