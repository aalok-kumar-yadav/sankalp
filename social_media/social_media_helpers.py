from contributor_app.models import Contributor


# Function for getting timeline context
def get_timeline_context(request, user_id):
    user_name = request.session['username']
    if user_name == user_id:
        gender_type = "You"
        con_status = "edit"
    else:
        gender_type = "him" if Contributor.objects.get(user__username=user_id) else "her"
        con_status = "connected"

    timeline_context = {
        'username': user_name, 'user_info': {'first_name': request.session['first_name'], 'followers': '204',
                                             'gender_type': gender_type}, 'timeline_section': 'home',
        'con_status': con_status, 'user_activity': 'Aalok Kumar liked monisha wamankar post'}

    return timeline_context


# Function for getting timeline context
def get_timeline_about_context(request, user_id):
    user_name = request.session['username']
    if user_name == user_id:
        gender_type = "You"
        con_status = "edit"
    else:
        gender_type = "him" if Contributor.objects.get(user__username=user_id) else "her"
        con_status = "connected"

    timeline_context = {
        'username': user_name, 'user_info': {'first_name': request.session['first_name'], 'followers': '204',
                                             'gender_type': gender_type}, 'timeline_section': 'about',
        'con_status': con_status, 'user_activity': 'Aalok Kumar liked monisha wamankar post'}

    return timeline_context


# Function for getting Latest News Feed
def get_news_feed(request):
    context_data = {'username': request.session['username'], 'user_info': {'first_name': request.session['first_name']}}
    return context_data


# Helper function for getting Connected people
def get_connected_people(request, user_id):
    context_data = {'username': request.session['username'],
                    'user_info': {'first_name': request.session['first_name'], 'followers': '204',
                                  'gender_type': "him"}, 'timeline_section': 'connected_people', 'con_status': "edit",
                    'user_activity': 'Aalok Kumar liked monisha wamankar post'}

    return context_data
