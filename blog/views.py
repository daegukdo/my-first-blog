from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def COVID19_map_data(request):
    return render(request, 'blog/COVID19/COVID_19_in_South_Korea_200317.html', {})