from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
import modules.anime.utils as utils

from .forms import AnimeSearch

import re

from pynimeapi import PyNime
pynime = PyNime()

class AnimeData:
    def __init__(self, title, category_url="", latest_episode_int="", latest_episode_url="", picture_url=""):
        self.title = title
        self.category_url = category_url
        self.latest_episode_int = latest_episode_int
        self.latest_episode_url = latest_episode_url
        self.picture_url = picture_url

# Create your views here.
def index(request):
    anime_data_list = list()
    # Get the requested page number from the URL parameter 'page'
    page = request.GET.get('page', 1) 
    # Fetch multiple pages of recent anime releases
    page_limit = 10  # Fetch a total of 10 pages
    anime_data = list()
    # for current_page in range(int(page), int(page) + page_limit):
    #     recent_anime = pynime.get_recent_release(page=current_page)
    #     anime_data.extend(recent_anime) 
    current_page = int(page)
    for _ in range(current_page + page_limit):
        recent_anime = pynime.get_recent_release(page=current_page)
        if not recent_anime:
            break  # No more pages available, exit loop
        anime_data.extend(recent_anime)  # Extend the list with results from the current page
        current_page += 1
    schedule = utils.anime_schedule()
    for i in anime_data:
        category_url = re.findall(r"/(\S*)-episode", i.latest_episode_url.replace(pynime.baseURL,""))[0]
        #save the anime to the database to enable search
        anime_data_list.append(
            AnimeData(
                title=i.title,
                latest_episode_int=i.latest_episode,
                latest_episode_url=i.latest_episode_url.replace(pynime.baseURL,""),
                picture_url=i.picture_url,
                category_url=category_url
            )
        )
    paginator = Paginator(anime_data_list, 20)  # Display 20 items per page

    try:
        anime_data_page = paginator.page(page)
    except PageNotAnInteger:
        anime_data_page = paginator.page(1)
    except EmptyPage:
        anime_data_page = paginator.page(paginator.num_pages)
    context = {
        'anime_data_list': anime_data_list,
        'anime_data_page': anime_data_page,
        'schedule': schedule,
    }
    return render(request, 'anime/index.html', context)

def watch(request, anime_episode_url: str, video_res: int):
    # url = pynime.get_stream_urls(f"{pynime.baseURL}/{anime_episode_url}")
    # print(url)
    # stream_url = pynime.get_stream_urls(f"{pynime.baseURL}/{anime_episode_url}")[str(video_res)]
    base_url = pynime.baseURL
    url = pynime.get_stream_urls(f"{base_url}/{anime_episode_url}")
    available_resolutions = url.keys()

    # Find the closest available resolution to the requested one
    closest_resolution = min(available_resolutions, key=lambda x: abs(int(x) - video_res))
    
    stream_url = url[closest_resolution]
    episode = re.findall(r"episode-(\d+)", anime_episode_url)[0]
    anime_title = pynime.search_anime(
        re.findall(r"(\S*)-episode", anime_episode_url)[0]
    )[0].title
    category_url = re.findall(r"(\S*)-episode", anime_episode_url)[0] 
    get_episodes = pynime.get_episode_urls(f"{pynime.baseURL}/category/{category_url}")
    context = {
        'anime_title': anime_title,
        'episode': int(episode),
        'total_episode': len(get_episodes),
        'video_source': stream_url,
        'anime_category_url': category_url
    }
    return render(request, 'anime/watch.html', context)

def search_anime(request):
    if request.method == 'POST':
        form = AnimeSearch(request.POST)
        if form.is_valid():
            anime_result_list = list()
            anime_search_query = form.cleaned_data['search_query']
            search_result = pynime.search_anime(anime_search_query)

            for i in search_result:
                anime_result_list.append(
                    AnimeData(
                        title=i.title,
                        category_url=re.findall(r"\S*category/(\S*)", i.category_url)[0],
                        picture_url=i.picture_url,
                    )
                )

            context = {
                'search_query': anime_search_query,
                'search_result': anime_result_list,
            }
            return render(request, 'anime/search.html', context)

    return render(request, 'anime/search.html', {'search_result': []})

def details(request, anime_category_url: str):
    anime_details = pynime.get_anime_details(f"{pynime.baseURL}/category/{anime_category_url}")
    get_episodes = pynime.get_episode_urls(f"{pynime.baseURL}/category/{anime_category_url}")

    context = {
        'anime_watch_url': anime_category_url,
        'anime_title': anime_details.title,
        'anime_synopsis': anime_details.synopsis,
        'anime_picture_url': anime_details.image_url,
        'anime_genres': ", ".join(str(genre) for genre in anime_details.genres),
        'anime_status': anime_details.status,
        'anime_season': anime_details.season,
        'anime_released': anime_details.released,
        'total_episode': len(get_episodes),
        'list_episodes': get_episodes,
    }
    return render(request, 'anime/details.html', context)