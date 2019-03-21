"""
    Social media file helper contains helper function for providing
    all types of binary file uploading in media directory.

"""

import os


# Function for uploading profile image
def upload_profile_image(request, file_name='profile_pic'):
    upload_flag = False
    upload_dir = 'media/profile/'
    file_path = None
    if request.method == "POST":
        target_file_name = str(request.session['username'])+str("_profile_")+str(request.FILES.get(file_name))
        file_path = os.path.join(upload_dir, target_file_name)
        if not os.path.isdir(upload_dir):
            os.makedirs(upload_dir)
        source_file = request.FILES[file_name]
        with open(file_path, 'wb+') as destination_file:
            for chunk in source_file.chunks():
                destination_file.write(chunk)
            destination_file.close()
            upload_flag = True

    if not upload_flag:
        file_path = None
    return file_path
