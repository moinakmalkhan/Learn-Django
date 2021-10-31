from django.shortcuts import render

# Create your views here.
def setcookies(request):
    request.session['fname'] = 'Moin'
    request.session['lname'] = 'Khan'
    res = render(request,"cookiesoperations/setcookies.html")
    # res.set_cookie("name","moinkhan")
    # res.set_cookie("name","moinkhan")
    return res
def getcookies(request):
    # name = request.COOKIES.get("name","Unknown")
    fname = request.session['fname']
    lname = request.session['lname']
    return render(request, "cookiesoperations/getcookies.html", {"fname" : fname, 'lname' : lname})


def delcookies(request):
    request.session.flush()
    return render(request, "cookiesoperations/delcookies.html")