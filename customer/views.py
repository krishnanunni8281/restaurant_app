from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,ListView
from employee.models import Food
from employee import forms
from django.contrib.auth import authenticate, login
from customer.models import User
from django.urls import reverse_lazy
from customer import forms
from customer.models import Carts,Orders
from django.db.models import Sum
from customer.forms import OrderForm
from django.contrib.auth import logout




# Create your views here.
class ProfileHome(TemplateView):
    template_name = "customer_index.html"

class CustomerBase(View):
    def get(self, request):
        if request.user.is_authenticated:
            qs = Food.objects.all()
            context = {"foods": qs}
            return render(request, "customer_index.html", context)
        else:
            return redirect("signin")

# class CustomerBase(View):
#     def get(self, request,*args,**kwargs):
#             qs = Food.objects.all()
#             context = {"foods": qs}
#             return render(request, "customer_index.html", context)


class SignUpView(CreateView):
    template_name = "register.html"
    form_class = forms.UserRegistration
    model = User
    success_url = reverse_lazy("signin")


class SignInView(TemplateView):
    template_name = "login.html"

    def get(self, request):
        form = forms.LoginForm
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                print(request.user.role)
                if request.user.role == "customer":
                    return redirect("customerbase")
                else:
                    return redirect("emp_base")
        return redirect("signin")



class AddToCart(View):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        food = Food.objects.get(id=id)
        user = request.user
        cart=Carts(user=user, item=food)
        cart.save()
        print("Your job has been added")
        return redirect("customerbase")


class CartItem(ListView):
    model = Carts
    template_name = "cart_item.html"
    context_object_name = "items"
    def get(self, request, *args, **kwargs):
        qs = self.model.objects.filter(user=self.request.user).exclude(status="cancelled")
        total_Sum=qs.aggregate(Sum("item__price"))
        total=total_Sum["item__price__sum"]
        context = {"items": qs,"total":total}
        return render(request, self.template_name, context)

class RemoveCart(View):
    model=Carts
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        cart=Carts.objects.get(id=id)
        cart.status="cancelled"
        cart.save()
        return redirect("customerbase")

class OrderCreate(CreateView):
    model=Orders
    template_name = "customer_order.html"
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        p_id=kwargs.get("p_id")
        cd_id=kwargs.get("c_id")
        form=OrderForm(request.POST)
        if form.is_valid():
            cart=Carts.objects.get(id=cd_id)
            address=form.cleaned_data.get("address")
            food=Food.objects.get(id=p_id)
            user=request.user
            order=Orders(item=food,user=user,address=address)
            order.save()
            cart.status="orderplaced"
            cart.save()
            # messages.success(request,"Successfully")
            return redirect("customerbase")

class MyOrders(ListView):
    model = Orders
    context_object_name = "orders"
    template_name = "myorder.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).exclude(status="cancel")

def cancel_order(request,*args,**kwargs):
    o_id=kwargs.get("id")
    order=Orders.objects.get(id=o_id)
    order.status="cancel"
    order.save()
    return redirect("customerbase")

def signout(request):
    logout(request)
    return redirect("signin")