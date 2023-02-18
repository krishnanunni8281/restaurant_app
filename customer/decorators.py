# from django.shortcuts import redirect
#
# def sign_in_required(fun):
#     def wrapper(req,*args,**kwargs):
#         if req.user.is_authenticated:
#             fun(req,*args,**kwargs)
#         else:
#             return redirect('signin')
#     return wrapper