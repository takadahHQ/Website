from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class AdvertisementMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

            # Get the current module/app name being accessed
        current_app = resolve(request.path_info).app_name

        # List of module/app names where the advertisement conditions should apply
        selected_apps = ['app1', 'app2', 'app3']  # Replace with the desired app names

        if current_app in selected_apps:  # Implement your own condition function
            user = request.user

            num_visited_pages = request.session.get('num_visited_pages', 0)
            
            if user.is_anonymous:
                num_visited_pages += 1
                max_page_visits = 3
            else:
                num_visited_pages += 1
                max_page_visits = 10

            if num_visited_pages >= max_page_visits:
                original_page_url = request.get_full_path()
                advertisement_url = reverse('advertisement', args=[original_page_url])
                request.session['num_visited_pages'] = 0  # Reset the counter
                return redirect(advertisement_url)
            else:
                request.session['num_visited_pages'] = num_visited_pages

        return response
