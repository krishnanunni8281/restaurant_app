from django.urls import path
from employee import views

urlpatterns = [



    path("home", views.EmpBase.as_view(), name="emp_base"),
    path("empstaff/list", views.EmpStaffList.as_view(), name="empstaff_list"),
    path("empjob/add", views.EmpAddStaff.as_view(), name="empstaff_add"),
    path("emp/detail/<int:id>", views.EmpDetailStaff.as_view(), name="empstaff_detail"),
    path("emp/edit/<int:id>", views.EmpUpdateStaff.as_view(), name="empstaff_edit"),
    path("emp/delete/<int:id>", views.EmpDeleteStaff.as_view(), name="empdelete"),

    path("emofood/list",views.EmpFoodList.as_view(),name="empfood_list"),
    path("empfood/add",views.EmpAddFood.as_view(),name="empfood_add"),
    path("empfood/detail/<int:id>",views.EmpDetailFood.as_view(),name="empfood_detail"),
    path("empfood/edit/<int:id>", views.EmpUpdateFood.as_view(), name="empfood_edit"),
    path("empfood/delete/<int:id>", views.EmpDeleteFood.as_view(), name="empdeletefood"),

    path("dashboard",views.EmpDashboard.as_view(),name="dashboard"),
    path("order,<int:o_id>",views.OrderDetail.as_view(),name="orderdetil")


]
