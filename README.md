# 2022-django-learninglogs
This is my exercise base on the tutorials on Youtube made by Learning Python: https://www.youtube.com/watch?v=J_6R9Bo6AdU&amp;list=PLiEts138s9P1A6rXyg4KZQiNBB_qTkq9V&amp;index=18

Github repository: https://github.com/gurnitha/2022-django-learninglogs


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

