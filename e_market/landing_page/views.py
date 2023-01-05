from django.shortcuts import render

# Create your views here.

def index (request):
    business_categories = ["Banks","Insurance companies","Mobile loan apps","Mobile money apps","Online payment platforms","Car Dealers","Real Estate Dealers","Travel companies","Private Universities","Taxi","Supermarkets", "Hotels"]
    business_categories = ["item-x" for i in range(12)]
    context = {
        "user" : "Jacob Watua",
        "comparisons" : "It’s often difficult to choose the best option when you have different ones that are far apart.\
        Paired Comparison Method can be used in different situations. For example, when it’s unclear which priorities are important or when evaluation criteria are subjective in nature.The Paired Comparison Analysis also helps when potential options are competing with each other, because the most effective solution will be chosen in the end. It’s easier to set priorities when there are no conflicting requirements.",
        "business_categories" : business_categories
    }
    return render(request, "disposable.html", context= context)

