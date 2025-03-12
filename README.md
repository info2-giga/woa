# World of Adventures (not World of Warcraft)

## Table of contents
1. [Introduction](#introduction)
2. [Test users](#some-users-for-testing)
    - [Personas](#our-personas)
    - [Gigachad](#gigachad)
3. [Workflow](#for-workflow)
4. [Python commands](#some-python-commands)

## Introduction
![Wendy Ameilya](./coding.gif)

Work in progress

## Some users for testing
### Our personas
**Wendy Ameilya (CS Team Lead)**

![Wendy Ameilya](media/uploads/profiles/wendy.jpg)

Wendy is **26 years old** and works for a large IT service provider. She is a huge **K-Pop fan** and feel﻿s strongly attracted to **Asian cultures**. When she is not working, Wendy uses her free time to explore new travel destinations in Asia and deepen her enthusiasm for the region.
````
username: wendy_reveluv_mei
password: wendyfromredvelvet
````

**Niklas Regen (Heritage Consultant)**

![Niklas Regen](media/uploads/profiles/niklas.jpg)

Niklas, 34, is a **Heritage Consultant** based in Heidelberg. Passionate about preserving **cultural landmarks**, he spends his free time **visiting museums**, writing about **heritage topics**, and exploring nature through hiking and photography.

```
username: niklas_regen
password: niklasregen
```

**Mike Ehrmantraut (CS Student)**

![Mike Ehrmantraut](media/uploads/profiles/mike.jpg)

Mike Ehrmantraut is a busy 23 year old Bachelors **Student**. He wants to travel but doesn't know where to start or how much money it takes which is why he never starts doing research and the thought seems like a scary wall of fog.

```
username: mike_ehrmantraut
password: mikeehrmantraut
```
### Gigachad
![Ernest Khalimov](media/uploads/profiles/gigachad.jpg)

From giga- +‎ Chad (“a very attractive man”). Although isolated uses exist earlier, the term was popularized by an anonymous poster on the 4chan /pol/ board on October 17th, 2017, who referred to Russian model Ernest Khalimov as "Gigachad".[1] See Gigachad for more.

```
username: gigachad
password: gigachad
```
## For workflow

### CSS

If you code with the project, make sure you have the "**watcher**" on for TailwindCSS.

First you need to install the necessary npm packages for the project. 
```
cd static/css/
npm install
tailwindcss -i ./input.css -o ./output.css --watch
```
Or move to the file and run the script.

It is necessary to code with the watcher, because everytime you write a new code piece, a new css file will be generated for the project.

### Helpful variables for templating
```
{% if request.user.is_authenticated %}
   <p>If the user is authenticated.</p>
{% endif %}

{% static 'images/placeholder.jpg %} -- load a static file from the static folder

request.user.username -- username from the requested user
... other attributes .... simple

```

---

### Folders/Files/Vice Versa

```
/authentication
   /context_processors.py -- useful for render specific templates globally
   /forms.py -- create a seperate custom form class for the HTML forms
   /models.py -- Alter the fields for the CustomUser
   /views.py -- Create a view or controller for the user
   
/<service-xyz>
   ...
   
/static -- holds the statics assets like images, fonts, css-files and js-files

/media -- required for the backend
   /uploads -- folder for uploading files
      /posts
         /images
         /videos
      /profiles
      
/woa -- important folder
   /settings.py -- the global file to configure specific variables and so on
   /urls.py -- for the routing
   
/templates -- the template folder for out HTML files
   /assets
      /base.html -- the global file for the app (Navigation, everything)
   /<service-xyz> -- the service/feature template for the app
```

---

### GitLab

To work on our features for example:
```
1. First clone 
git clone https://gitlab.rz.htw-berlin.de/imi-informatik/info3/24-wise/projects/g2team5/woa
git checkout -b feature/my-feature-abc

2. Pull regulary from main
git checkout main
git pull origin main
git checkout feature/my-feature-abc
git merge main

3. Develope the features
git add.
git commit -m "Add a special feature for xyz"

4. Test the application with data

5. Create pull request
git push origin feature/my-feature-abc

6. Merge in main
git checkout main
git pull origin main
git checkout feature/my-feature-abc
git merge main

Got the snippet from ChatGPT
```

## Some python commands
```
- Migrate database
python manage.py makemigration <your-service> 
python manage.py migrate <your-service>

- Using the sheel in venv
python manage.py shell
```

