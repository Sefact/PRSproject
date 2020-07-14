from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.template import loader

## Main page views
def index(request):
    template = loader.get_template('blog/index.html')
    now = datetime.now()
    context = {
        'latest_question_list': "test",
        'current_date': now,
    }
    return HttpResponse(template.render(context, request))

def introduce(request):
    return render(request, 'blog/introduce.html')

def tag(request):
    return render(request, 'blog/tag.html')

def contact(request):
    return render(request, 'blog/contact.html')

def recommendation1(request):
    return render(request, 'blog/recommendation1.html')

def recommendation2(request):
    return render(request, 'blog/recommendation2.html')

def recommendation3(request):
    return render(request, 'blog/recommendation3.html')

def recommendation4(request):
    return render(request, 'blog/recommendation4.html')

## Main Page Editor Recommendation views
def index_editor1(request):
    return render(request, 'blog/index/index_editor1.html')

def index_editor2(request):
    return render(request, 'blog/index/index_editor2.html')

def index_editor3(request):
    return render(request, 'blog/index/index_editor3.html')

## Recommendation One Page Recommendation views
def recommend1_1(request):
    return render(request, 'blog/recommend/recommend1/recommend1_1.html')

def recommend1_2(request):
    return render(request, 'blog/recommend/recommend1/recommend1_2.html')

def recommend1_3(request):
    return render(request, 'blog/recommend/recommend1/recommend1_3.html')

def recommend1_4(request):
    return render(request, 'blog/recommend/recommend1/recommend1_4.html')

def recommend1_5(request):
    return render(request, 'blog/recommend/recommend1/recommend1_5.html')

def recommend1_6(request):
    return render(request, 'blog/recommend/recommend1/recommend1_6.html')

## Recommendation Three Page Recommendation views
def recommend3_1(request):
    return render(request, 'blog/recommend/recommend3/recommend3_1.html')

def recommend3_2(request):
    return render(request, 'blog/recommend/recommend3/recommend3_2.html')

def recommend3_3(request):
    return render(request, 'blog/recommend/recommend3/recommend3_3.html')

def recommend3_4(request):
    return render(request, 'blog/recommend/recommend3/recommend3_4.html')

def recommend3_5(request):
    return render(request, 'blog/recommend/recommend3/recommend3_5.html')

def recommend3_6(request):
    return render(request, 'blog/recommend/recommend3/recommend3_6.html')

## Recommendation Four Page Recommendation views
def recommend4_1(request):
    return render(request, 'blog/recommend/recommend4/recommend4_1.html')

def recommend4_2(request):
    return render(request, 'blog/recommend/recommend4/recommend4_2.html')

def recommend4_3(request):
    return render(request, 'blog/recommend/recommend4/recommend4_3.html')

## Tag-One Page views
def tag1_1(request):
    return render(request, 'blog/tag/tag1/tag1_1.html')

def tag1_2(request):
    return render(request, 'blog/tag/tag1/tag1_2.html')

def tag1_3(request):
    return render(request, 'blog/tag/tag1/tag1_3.html')

def tag1_4(request):
    return render(request, 'blog/tag/tag1/tag1_4.html')

def tag1_5(request):
    return render(request, 'blog/tag/tag1/tag1_5.html')

def tag1_6(request):
    return render(request, 'blog/tag/tag1/tag1_6.html')

## Tag-Two Page views
def tag2_1(request):
    return render(request, 'blog/tag/tag2/tag2_1.html')

def tag2_2(request):
    return render(request, 'blog/tag/tag2/tag2_2.html')

def tag2_3(request):
    return render(request, 'blog/tag/tag2/tag2_3.html')

def tag2_4(request):
    return render(request, 'blog/tag/tag2/tag2_4.html')

def tag2_5(request):
    return render(request, 'blog/tag/tag2/tag2_5.html')

def tag2_6(request):
    return render(request, 'blog/tag/tag2/tag2_6.html')

## Tag-Three Page views
def tag3_1(request):
    return render(request, 'blog/tag/tag3/tag3_1.html')

def tag3_2(request):
    return render(request, 'blog/tag/tag3/tag3_2.html')

def tag3_3(request):
    return render(request, 'blog/tag/tag3/tag3_3.html')

def tag3_4(request):
    return render(request, 'blog/tag/tag3/tag3_4.html')

def tag3_5(request):
    return render(request, 'blog/tag/tag3/tag3_5.html')

def tag3_6(request):
    return render(request, 'blog/tag/tag3/tag3_6.html')

## Tag-Four Page views
def tag4_1(request):
    return render(request, 'blog/tag/tag4/tag4_1.html')

def tag4_2(request):
    return render(request, 'blog/tag/tag4/tag4_2.html')

def tag4_3(request):
    return render(request, 'blog/tag/tag4/tag4_3.html')

def tag4_4(request):
    return render(request, 'blog/tag/tag4/tag4_4.html')

def tag4_5(request):
    return render(request, 'blog/tag/tag4/tag4_5.html')

def tag4_6(request):
    return render(request, 'blog/tag/tag4/tag4_6.html')

## Tag-Five Page views
def tag5_1(request):
    return render(request, 'blog/tag/tag5/tag5_1.html')

def tag5_2(request):
    return render(request, 'blog/tag/tag5/tag5_2.html')

def tag5_3(request):
    return render(request, 'blog/tag/tag5/tag5_3.html')

def tag5_4(request):
    return render(request, 'blog/tag/tag5/tag5_4.html')

def tag5_5(request):
    return render(request, 'blog/tag/tag5/tag5_5.html')

def tag5_6(request):
    return render(request, 'blog/tag/tag5/tag5_6.html')

## Tag-Six Page views
def tag6_1(request):
    return render(request, 'blog/tag/tag6/tag6_1.html')

def tag6_2(request):
    return render(request, 'blog/tag/tag6/tag6_2.html')

def tag6_3(request):
    return render(request, 'blog/tag/tag6/tag6_3.html')

def tag6_4(request):
    return render(request, 'blog/tag/tag6/tag6_4.html')

def tag6_5(request):
    return render(request, 'blog/tag/tag6/tag6_5.html')

def tag6_6(request):
    return render(request, 'blog/tag/tag6/tag6_6.html')

## Tag-list Page views
def tag_list1(request):
    return render(request, 'blog/tag/taglist/tag_list1.html')

def tag_list2(request):
    return render(request, 'blog/tag/taglist/tag_list2.html')

def tag_list3(request):
    return render(request, 'blog/tag/taglist/tag_list3.html')

def tag_list4(request):
    return render(request, 'blog/tag/taglist/tag_list4.html')

def tag_list5(request):
    return render(request, 'blog/tag/taglist/tag_list5.html')

def tag_list6(request):
    return render(request, 'blog/tag/taglist/tag_list6.html')

## Area-One Page views
def area1_1(request):
    return render(request, 'blog/area/area1/area1_1.html')

def area1_2(request):
    return render(request, 'blog/area/area1/area1_2.html')

def area1_3(request):
    return render(request, 'blog/area/area1/area1_3.html')

def area1_4(request):
    return render(request, 'blog/area/area1/area1_4.html')

def area1_5(request):
    return render(request, 'blog/area/area1/area1_5.html')

def area1_6(request):
    return render(request, 'blog/area/area1/area1_6.html')

## Area-Two Page views
def area2_1(request):
    return render(request, 'blog/area/area2/area2_1.html')

def area2_2(request):
    return render(request, 'blog/area/area2/area2_2.html')

def area2_3(request):
    return render(request, 'blog/area/area2/area2_3.html')

def area2_4(request):
    return render(request, 'blog/area/area2/area2_4.html')

def area2_5(request):
    return render(request, 'blog/area/area2/area2_5.html')

def area2_6(request):
    return render(request, 'blog/area/area2/area2_6.html')

## Area-Three Page views
def area3_1(request):
    return render(request, 'blog/area/area3/area3_1.html')

def area3_2(request):
    return render(request, 'blog/area/area3/area3_2.html')

def area3_3(request):
    return render(request, 'blog/area/area3/area3_3.html')

def area3_4(request):
    return render(request, 'blog/area/area3/area3_4.html')

def area3_5(request):
    return render(request, 'blog/area/area3/area3_5.html')

def area3_6(request):
    return render(request, 'blog/area/area3/area3_6.html')

## Area-Four Page views
def area4_1(request):
    return render(request, 'blog/area/area4/area4_1.html')

def area4_2(request):
    return render(request, 'blog/area/area4/area4_2.html')

def area4_3(request):
    return render(request, 'blog/area/area4/area4_3.html')

def area4_4(request):
    return render(request, 'blog/area/area4/area4_4.html')

def area4_5(request):
    return render(request, 'blog/area/area4/area4_5.html')

def area4_6(request):
    return render(request, 'blog/area/area4/area4_6.html')

## Area-Five Page views
def area5_1(request):
    return render(request, 'blog/area/area5/area5_1.html')

def area5_2(request):
    return render(request, 'blog/area/area5/area5_2.html')

def area5_3(request):
    return render(request, 'blog/area/area5/area5_3.html')

def area5_4(request):
    return render(request, 'blog/area/area5/area5_4.html')

def area5_5(request):
    return render(request, 'blog/area/area5/area5_5.html')

def area5_6(request):
    return render(request, 'blog/area/area5/area5_6.html')

## Area-Six Page views
def area6_1(request):
    return render(request, 'blog/area/area6/area6_1.html')

def area6_2(request):
    return render(request, 'blog/area/area6/area6_2.html')

def area6_3(request):
    return render(request, 'blog/area/area6/area6_3.html')

def area6_4(request):
    return render(request, 'blog/area/area6/area6_4.html')

def area6_5(request):
    return render(request, 'blog/area/area6/area6_5.html')

def area6_6(request):
    return render(request, 'blog/area/area6/area6_6.html')

## Area-list Page views
def area_list1(request):
    return render(request, 'blog/area/arealist/area_list1.html')

def area_list2(request):
    return render(request, 'blog/area/arealist/area_list2.html')

def area_list3(request):
    return render(request, 'blog/area/arealist/area_list3.html')

def area_list4(request):
    return render(request, 'blog/area/arealist/area_list4.html')

def area_list5(request):
    return render(request, 'blog/area/arealist/area_list5.html')

def area_list6(request):
    return render(request, 'blog/area/arealist/area_list6.html')