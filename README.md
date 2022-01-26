# 2022-django-learninglogs
This is my exercise base on the tutorials on Youtube made by Learning Python: https://www.youtube.com/watch?v=J_6R9Bo6AdU&amp;list=PLiEts138s9P1A6rXyg4KZQiNBB_qTkq9V&amp;index=18

Github repository: https://github.com/gurnitha/2022-django-learninglogs

Note:

Some notes in some titles in this README.md files
were quoted from the book of PYTHON CRASH COURSE 2ND EDITION.

A practical book of Python and Django written by ERIC MATTHES.


#### 1. Create django project

        modified:   README.md
        new file:   learning_log/__init__.py
        new file:   learning_log/settings.py
        new file:   learning_log/urls.py
        new file:   learning_log/wsgi.py
        new file:   manage.py


#### 2. Creating an app 'learning_logs'

        modified:   README.md
        modified:   learning_log/settings.py
        new file:   learning_logs/__init__.py
        new file:   learning_logs/admin.py
        new file:   learning_logs/apps.py
        new file:   learning_logs/migrations/__init__.py
        new file:   learning_logs/models.py
        new file:   learning_logs/tests.py
        new file:   learning_logs/views.py


#### 3. Create Topic model, run migrations

        modified:   README.md
        modified:   learning_logs/admin.py
        new file:   learning_logs/migrations/0001_initial.py
        modified:   learning_logs/models.py


#### 4. Create Entry model, run migrations, added some topics and entries

        modified:   README.md
        modified:   learning_logs/admin.py
        new file:   learning_logs/migrations/0002_entry.py
        modified:   learning_logs/models.py


Making Pages: 
-------------

#### 5. Create the Learning Log Home Page: Views, Templates, Urls

        modified:   README.md
        modified:   learning_log/urls.py
        new file:   learning_logs/templates/learning_logs/index.html
        new file:   learning_logs/urls.py
        modified:   learning_logs/views.py


#### 6. Create base template 

        modified:   README.md
        new file:   learning_logs/templates/learning_logs/base.html
        modified:   learning_logs/templates/learning_logs/index.html


#### 7. Create topics (list of topics) page 

        modified:   README.md
        modified:   learning_logs/templates/learning_logs/base.html
        new file:   learning_logs/templates/learning_logs/topics.html
        modified:   learning_logs/urls.py
        modified:   learning_logs/views.py


#### 8. Create detail page for a single topic

        modified:   README.md
        new file:   learning_logs/templates/learning_logs/topic.html
        modified:   learning_logs/templates/learning_logs/topics.html
        modified:   learning_logs/urls.py
        modified:   learning_logs/views.py


### User Accounts: Allowing Users to Enter Data
-----------------------------------------------

### 9. Adding New Topics 

        modified:   README.md
        new file:   learning_logs/forms.py
        new file:   learning_logs/templates/learning_logs/new_topic.html
        modified:   learning_logs/templates/learning_logs/topics.html
        modified:   learning_logs/urls.py
        modified:   learning_logs/views.py


#### 10. Adding New Entries

        modified:   README.md
        modified:   learning_logs/forms.py
        new file:   learning_logs/templates/learning_logs/new_entry.html
        modified:   learning_logs/templates/learning_logs/topic.html
        modified:   learning_logs/urls.py
        modified:   learning_logs/views.py


#### 11. Editing Entries

        modified:   README.md
        new file:   learning_logs/templates/learning_logs/edit_entry.html
        modified:   learning_logs/templates/learning_logs/topic.html
        modified:   learning_logs/urls.py
        modified:   learning_logs/views.py


### User Accounts: Setting Up User Accounts
-------------------------------------------

#### 12. Create users app

        modified:   README.md
        modified:   learning_log/settings.py
        new file:   users/__init__.py
        new file:   users/admin.py
        new file:   users/apps.py
        new file:   users/migrations/__init__.py
        new file:   users/models.py
        new file:   users/tests.py
        new file:   users/views.py


#### 13. The Login Page and 'Hello, admin'

        STEPS:

        1. Setup default auth urls by including
           django.contrib.auth.urls
        2. Create login template
        3. Linking to the Login Page
        4. Using the Login Page
           - If you are still logged in as superuser,
             do logout
           - Go go : http://127.0.0.1:8000/users/login
           - Login as admin
           - You will see 'Hello, admin'
           - :)

        modified:   README.md
        modified:   learning_log/urls.py
        modified:   learning_logs/templates/learning_logs/base.html
        new file:   users/templates/registration/login.html
        new file:   users/urls.py


#### 14. Logging Out

        STEPS:

        1. Adding a Logout Link to base.htm
        2. The Logout Confirmation Page

        modified:   README.md
        modified:   learning_logs/templates/learning_logs/base.html
        new file:   users/templates/registration/logged_out.html


#### 15. The Registration Page

        STEPS:

        1. The register URL
        2. The register() View Function
        3. The register Template
        4. Linking to the Registration Page

        modified:   README.md
        modified:   learning_logs/templates/learning_logs/base.html
        modified:   learning_logs/templates/learning_logs/topics.html
        new file:   users/templates/registration/register.html
        modified:   users/urls.py
        modified:   users/views.py


### User Accounts: Allowing Users to Own Their Data
---------------------------------------------------


#### 16. Restricting Access with @login_required

        STEPS:

        1. Restricting Access to the Topics Page 
        2. Restricting Access to the New Topic Page 
        3. Restricting Access to the New Entry Page 
        4. Restricting Access to the Edit Entry Page 

        NOTE:

        1. Once user logged out, user can:
           -see topics
           -register menu and
           -login menu
        2. To View, Add, Edit topics user must login first. 

        modified:   README.md
        modified:   learning_log/settings.py
        modified:   learning_logs/views.py


#### 17. Connecting Data to Certain Users

        STEPS:

        In learning_logs/model.py
        
        1. Import from django.contrib.auth.models import User  
        2. Modifying the Topic Model
        3. Identifying Existing Users

                (learninglogs) λ python manage.py shell
                Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC         v.1928 64 bit (AMD64)] on win32
                Type "help", "copyright", "credits" or "license" for more information.
                (InteractiveConsole)
                >>>
                >>> from django.contrib.auth.models import User
                >>> User.objects.all()
                <QuerySet [<User: admin>, <User: testuser1>]>
                >>>
                >>> for user in User.objects.all():
                ...     print(user.username, user.id)
                ...
                admin 1
                testuser1 2
                >>>

        4. Migrating the Database

                (learninglogs) λ python manage.py makemigrations learning_logs
                You are trying to add a non-nullable field 'owner' to topic without a default; we can't do that (the database needs something to populate existing rows).
                Please select a fix:
                 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
                 2) Quit, and let me add a default in models.py
                Select an option: 1
                Please enter the default value now, as valid Python
                The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
                Type 'exit' to exit this prompt
                >>> 1
                Migrations for 'learning_logs':
                  learning_logs\migrations\0003_topic_owner.py
                    - Add field owner to topic
                
                ...
                (learninglogs) λ python manage.py migrate

        5. We can verify that the migration worked

                (learninglogs) λ python manage.py shell
                Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
                Type "help", "copyright", "credits" or "license" for more information.
                (InteractiveConsole)
                >>>
                >>> from learning_logs.models import Topic
                >>> for topic in Topic.objects.all():
                ...     print(topic, topic.owner)
                ...
                Topic 1 admin
                Topic 2 admin
                Topic 3 admin
                Topic 4 admin
                Topic 5 admin
                Test1 topic admin
                Test1 topic admin
                Topic 1 of testuser1 admin
                >>>

                NOTE:

                Now all topics is belongs to the admin because we added admin id of 1
                in the python shell

        modified:   README.md
        modified:   learning_logs/migrations/0003_topic_owner.py
        modified:   learning_logs/models.py


#### 18. Restricting Topics Access to Appropriate Users

        NOTE:

        Currently, if you’re logged in, you’ll be 
        able to see all the topics, no matter 
        which user you’re logged in as. 
        We’ll change that by showing users only the 
        topics that belong to them. 

        STEPS:

        1. Make the following change to the topics() function in views.py
        topics = Topic.objects.filter(
                owner=request.user).order_by('date_added')


        NOTE:

        1. There are two users for now:
           - admin as superuser
           - testuser1 as normal user
        2. Now admin can view on its own topics
        3. Now testuser1 also can view only its own topics

        modified:   README.md
        modified:   learning_logs/views.py       


#### 19. Protecting a User’s Topics

        NOTE:

        We haven’t restricted access to the topic 
        pages yet, so any registered user 
        could try a bunch of URLs, 
        like http://localhost:8000/topics/1/, and retrieve 
        topic pages that happen to match.

        So, if admin login, he can:

        1. View testuser1 topics
        2. Edit testuser1 topic

        We will protect user's topics now

        STEPS:

        In learning_logs/views.py

        1. Import: from django.http import Http404
        2. Modify topic view method
        3. Test it out :)

        NOTE:

        1. If admin logged in, it can view only
           its own topics
        2. But it can edit testuser1 topic, if he
           goes to: http://127.0.0.1:8000/edit_entry/8/

           Note: entry 8 is belong to testuser1

        modified:   README.md
        modified:   learning_logs/views.py  


#### 20. Protecting the edit_entry Page

        The edit_entry pages have URLs in the form 
        http://localhost:8000/edit_entry/entry_id/, 
        where the entry_id is a number. 

        Let’s protect this page so no one can use the 
        URL to gain access to someone else’s entries:

        STEPS:

        1. Add this to edit_topic view method

                if topic.owner != request.user:
                raise Http404

        2. Test it out :)

        NOTE:

        1. If admin logged in, and try to go here
           http://127.0.0.1:8000/edit_entry/8/

           It will response with:

           Page not found (404)

        modified:   README.md
        modified:   learning_logs/views.py


#### 21. Associating New Topics with the Current User

        Currently, our page for adding new topics is broken, 
        because it doesn’t 
        associate new topics with any particular user. 
        If you try adding a new topic, 
        you’ll see the error message IntegrityError 
        along with NOT NULL constraint 
        failed: learning_logs_topic.owner_id. 

        Django’s saying you can’t create a new 
        topic without specifying a value for the topic’s 
        owner field.

        STEPS:

        1. Modify new_topic view method with this:

                        if form.is_valid():
                        new_topic = form.save(commit=False)
                        new_topic.owner = request.user
                        new_topic.save()

        2. Test it out :)

        NOTE:

        1. The broken thigs are gone now

        modified:   README.md
        modified:   learning_logs/views.py


### STYLING: Styling Learning Log
---------------------------------


#### 22. Install the django-bootstrap4 App

        STEPS:

        1. Install django-bootstrap4: 
           λ  pip install django-bootstrap4
        2. Register bootstrap4 in settings.py
        3. Modifying base.html

        modified:   README.md
        modified:   learning_log/settings.py
        modified:   learning_logs/templates/learning_logs/base.html





