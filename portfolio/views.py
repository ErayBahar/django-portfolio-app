from django.shortcuts import get_object_or_404,render,redirect
from .models import portfolioItem
from .forms import PortfolioItemForm

# Create your views here.

def portfolio_list(request):
    items = portfolioItem.objects.all()
    return render(request,'portfolio/portfolio_list.html',{'items':items})
def add_investment(request):
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioItemForm
    return render(request,'portfolio/add_investment.html',{'form':form})
def delete_investment(request,item_id):
    item = get_object_or_404(portfolioItem, id=item_id)

    if request.method == "POST":
        item.delete()
        return redirect('portfolio_list')

    return render(request,'portfolio/delete_confirm.html',{'item':item})
