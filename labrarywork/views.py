from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView , View ,ListView
from django.views.generic.edit import UpdateView
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(TemplateView):
    template_name = 'owner/home.html'


class Login(View):
    def post(self,request):
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username = loginusername ,password = loginpassword)

        if user is not None:
            login(request,user)
            return redirect('allbook')
        else:
            return redirect('home')


class Logout(View):
    def get(self,request):
        logout(request)
        return render(request,'owner/home.html')


class AllBooks(LoginRequiredMixin,View):
    def get(self,request):
        data = {"allbook":Book.objects.all()}
        return render(request,'owner/all_books.html',data)


class Orders(LoginRequiredMixin,View):
    def get(self,request,pk,*args,**kwargs):
        form = OrderForm()
        data = {"form":form,"pk":pk}

        return render(request,'owner/checkout.html',data)

    def post(self,request,pk,*args,**kwargs):
        form = OrderForm(request.POST or None)

        if form.is_valid():
            a = form.save(commit=False)
            a.book_id = Book(pk)
            a.save()

            book = Book.objects.get(book_id = pk)
            book.qty -= 1
            book.save()
            return redirect('orderbook')


class AllCategory(LoginRequiredMixin,ListView):
    model = Category
    template_name = 'owner/allcategory.html'



class AllOrder(LoginRequiredMixin,View):
    def get(self,request):

        data = {"orderbook":Order.objects.all()}

        return render(request,'owner/order_books.html',data)

class AddBookCategory(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        form = BookCategoryForm
        context = {"forms":form}
        return render(request,'owner/add_category.html',context)

    def post(self,request,*args,**kwargs):
        form = BookCategoryForm(request.POST or None )
        if form.is_valid():
            form.save()
            return redirect('allbook')


class AddBook(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form = BookForm()
        context = {"forms": form}
        return render(request, 'owner/addbook.html', context)

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('allbook')


class RemoveOrder(LoginRequiredMixin,View):
    def get(self,request,pk,*args,**kwargs):
        order_id = Order.objects.get(order_id = pk)
        books = Book.objects.get(book_id = order_id.book_id.book_id)
        books.qty += 1
        books.save()
        Order.objects.filter(order_id = pk ).delete()
        return render(request,'owner/order_books.html')


class UpdateBook(LoginRequiredMixin,UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'owner/update_book.html'

    def form_valid(self,form):
        form.save()
        return redirect('allbook')


class Search(LoginRequiredMixin,View):
    def get(self,request):
        search = request.GET.get("search")

        cond = Q(name__icontains = search) | Q(category__title__icontains = search)

        book = Book.objects.filter(cond)
        data = {"allbook":book}
        return render(request,'owner/all_books.html',data)





