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
                                             'gender_type': gender_type}, 'timeline_section': 'home',
        'con_status': con_status, 'user_activity': 'Aalok Kumar liked monisha wamankar post'}

    return timeline_context