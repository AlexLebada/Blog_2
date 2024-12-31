## Project description
 This is a blog application with AI tools like:
- Chatbot: for general q's
- Answer based context: where creators can enhance their work by getting specific answers from chatbot with provided external data
- Summarization: Extract main ideas of a content ( in progress )


![Screenshot 2024-12-31 142218](https://github.com/user-attachments/assets/b24f68bf-b985-4f21-919f-68f9f475bd52)


## Backend description

* ### Project urls
  
    */Blog_2/url.py:*

       urlpatterns = [
        #re_path(r'^post/(.*)$', blog_views.post), #using regex pattern
        path('post/<slug:slug>/', blog_views.post), #without regex
        path('all_posts/', blog_views.all_posts),
        path('', blog_views.home, name='home'),
        #path('', blog_views.index),
        path('writer_panel/', blog_views.writer_panel, name='writer_panel'),
        path('editor_panel/', blog_views.editor_panel, name='editor_panel'),
        path('profile/', blog_views.profile, name='profile'),
        path('voting/', blog_views.voting, name='voting'),
        path('admin/', admin.site.urls),
        path('settings/', blog_views.settings, name='settings'),
        path('admin_tools_stats/', include('admin_tools_stats.urls')),
        path('register/', include('register.urls')),
        path('photo/upload/', room_views.photo_upload, name='photo_upload'),
        path('', include("django.contrib.auth.urls")),
        path('login/', LoginView.as_view(template_name='./registration/login.html'), name='login'),
        path('upload-file/', blog_views.upload_file, name='upload_file'),
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


## Frontend description

* ### User panel
 Because I want to make custom POST requests without *user_panel.html* page refresh, im using Fetch API when DOM loaded. For example, here Im making the request for post submission

   */Blog_2/blog/static/css/chatbot.js:*

           document.addEventListener('DOMContentLoaded', function() {
           ...
              postForm.addEventListener('submit', function (event) {
              event.preventDefault(); // Prevent page reload
      
              const formData = new FormData(postForm); // Collect form data including the file
              formData.append('submit_post', 'true')
              const csrfToken = getCSRFToken();
      
              fetch('/writer_panel/', {
                  method: 'POST',
                  headers: {
                      'X-CSRFToken': csrfToken, // Include CSRF token
                  },
                  body: formData,
              })
                  .then(response => response.json())
                  ...
              })
           })
