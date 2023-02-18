from django.urls import path
from customer import views

urlpatterns = [

    #     customer home

    path("home", views.CustomerBase.as_view(), name="customerbase"),

    # front
    path("foodlist", views.ProfileHome.as_view(), name="custpro"),

    # add to cart
    path("carts/add/<int:id>", views.AddToCart.as_view(), name="addtocart"),

    # cart item
    path("cart/items", views.CartItem.as_view(), name="cartitem"),

    # remove cart
    path("cart/item/remove/<int:id>", views.RemoveCart.as_view(), name="removeitem"),

    # customer detils
    path("order/add/<int:p_id>/<int:c_id>", views.OrderCreate.as_view(), name="ordercreate"),

    # customer purchased
    path("orders", views.MyOrders.as_view(), name="myorders"),

    # canel order
    path("remove/<int:id>", views.cancel_order, name="cancelorder"),

    path("ac/signup", views.SignUpView.as_view(), name="register"),
    path("ac/signin", views.SignInView.as_view(), name="signin"),

    path("signout", views.signout, name="signout"),

]
