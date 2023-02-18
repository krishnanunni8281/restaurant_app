from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView
from employee.models import Staff,Food
from employee.forms import EmpStaffForm,EmpFoodForm
from django.urls import reverse_lazy
from customer.models import Orders






# Create your views here.






class EmpBase(TemplateView):
    template_name = "baseemp.html"


class EmpStaffList(ListView):
    model = Staff
    context_object_name = "staff"
    template_name = "empstaff.html"


#     food models
class EmpFoodList(ListView):
    model = Food
    context_object_name = "food"
    template_name = "empfood.html"

class EmpAddFood(CreateView):
    model=Staff
    form_class=EmpFoodForm
    template_name="empaddfood.html"
    success_url=reverse_lazy("empfood_list")



class EmpDetailFood(DetailView):
    model=Food
    context_object_name = "food"
    template_name = "emp_food_detail.html"
    pk_url_kwarg = "id"



class EmpAddStaff(CreateView):
    model = Staff
    form_class = EmpStaffForm
    template_name = "empaddstaff.html"
    success_url = reverse_lazy("empstaff_list")

class EmpDetailStaff(DetailView):
    model = Staff
    context_object_name = "staff"
    template_name = "emp_staff_detail.html"
    pk_url_kwarg = "id"

class EmpUpdateStaff(UpdateView):
    model = Staff
    template_name = "emp_update_staff.html"
    pk_url_kwarg = "id"
    form_class = EmpStaffForm
    success_url = reverse_lazy("empstaff_list")

class EmpUpdateFood(UpdateView):
    model = Food
    template_name = "emp_update_food.html"
    pk_url_kwarg = "id"
    form_class = EmpFoodForm
    success_url = reverse_lazy("empfood_list")


class EmpDeleteStaff(DeleteView):
    model = Staff
    template_name = "emp_delete_staff.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("empstaff_list")

class EmpDeleteFood(DeleteView):
    model = Food
    template_name = "emp_delete_food.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("empfood_list")


#     manager

class EmpDashboard(ListView):
    model = Orders
    template_name = "emp_dashboard.html"

    def get(self,request,*args,**kwargs):
        new_order=self.model.objects.filter(status="buyitem")
        context={"n_order":new_order}
        return render(request,self.template_name,context)


class OrderDetail(DetailView):
    model = Orders
    template_name = "order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "o_id"

