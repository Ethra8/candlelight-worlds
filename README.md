# CANDLELIGHT WORLDS
![image](https://github.com/user-attachments/assets/3fbe4063-a3ce-4be9-9f37-912db1aecd1c)

## PROJECT OVERVIEW
- A booking site for a restaurant that offers out-of-the-box romantic dinners. This new concept involves private rooms carefully decorated to transport our guests to different times and places, all under immersive candlelight lighting.
- These romantic experiences not only include tasty dishes from around the globe served by our discreet and professional table service, but each private room also includes a lounge area with a king-size bed and an in-room private jakuzzi, so that couples can relax and chill after dinner, or even have a siesta!
- Guests also have the option to spend the night, if they wish so, by paying a supplement.

## LIVE SITE
Visit the live site **[here](https://candlelight-worlds-f913477cd630.herokuapp.com/)**

## REPOSITORY
Check Repository **[here](https://github.com/Ethra8/candlelight-world)**

### AUTHOR
Edna Torres Munill

# TABLE OF CONTENTS

- [Project Overview](#project-overview)
  * [Live Site](#live-site)
  * [Repository](#repository)
  * [Author](#author)
- [UX](#ux)
  * [Target Audience](#target-audience)
  * [Project Goals](#project-goals)
  * [Stories](#stories)
     - [User Stories](#user-stories)
     - [Site Owner Stories](#site-owner-stories)
  * [User Profiles](#user-profiles)
- [UI](#ui)
  * [Wireframes](#wireframes)
    - [Mobile & Tablet (portrait)](#mobile-&-tablet-(portrait))
    - [Desktop & Tablet (landscape)](#desktop-&-tablet-(landscape))
  * [Pages](#pages)
    - [Home Page](#home-page)
    - [Worlds Page](#worlds-page)
    - [Services Page](#services-page)
    - [Booking Page](#booking-page)
    - [404 Error Page](#404-error-page)
  * [Design Choices](#design-choices)
    - [Colors](#colors)
      * [Colors Rationale of Use](#colors-rationale-of-use)
    - [Typography](#typography)
      * [Typography Rationale of Use](#typography-rationale-of-use)
  * [CRUD Functionality](#crud-functionality)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
  * [Features](#features)
    - [Responsiveness](#responsiveness)
    - [Accessibility](#accessibility)
    - [Navigation Bar](#navigation-bar)
    - [Footer](#footer)
    - [User Authentication](#user-authentication)
    - [Confirmation Messages](#confirmation-messages)
    - [404 Error Page](#404-error-page)
    - [Admin Console](#admin-console)
- [AGILE Methodology](#agile-methodology)
  * [Github Project - Kanban](#github-project---kanban)
- [TESTING](#testing)
  * [Defect Tracking](#defect-tracking)
    - [Github Issues](#github-issues)
    - [Defects of Note](#defects-of-note)
    - [Outstanding Defects](#outstanding-defects)
  * [Core Web Vitals](#core-web-vitals)
     - [Lighthouse Reports](#lighthouse-reports)
  * [Accessibility](#accessibility)
     - [Contrast Validation Reports](#contrast-validation-reports)
     - [General WCAG 2.1 Report](#general-wcag-2.1-report)
  * [Manual Testing](#manual-testing)
     - [Testing Stories](#testing-stories)
- [TECHNOLOGIES and METHODOLOGIES USED](#technologies-and-methodologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)
- [DEPLOYMENT](#deployment)
  * [Version Control](#version-control)
  * [Heroku](#heroku)
  * [Local Copy](#local-copy)
    - [How to Clone](#how-to-clone)
    - [How to Fork](#how-to-fork)
- [CREDITS & ACKNOWEDGEMENTS](#credits-and-acknowledgements)


# UX
You will find in the points stated below a brief study aiming at providing the user with the best possible experience when visiting this site.
-

## TARGET AUDIENCE

The target audience of this site are as follows: 
-
- **B2C:**
  * Medium to hight ticket sale
  * Couples at any age wanting to add special memories
  * Someone seeking for a place to organize a special event such as weddings, anniversaries, or any other of the sort 
  * Someone looking for the special gift to offer

- **B2B:**
  * Companies that want to rent the events area
  * Companies that might want to offer a special gift to their premium clients or collaborators
  
## PROJECT GOALS

The project goals are as follows:
- 
  * The site aims at providing B2C customers with luxuriously themed private spaces where to have any meal of the day.
  * The site aims at providing B2B customers with luxuriously themed spaces for team building, staff gathering, and events.
  * Any users can register for an account to store, read, update and cancel their bookings.
  * B2B users can send a contact form to receive personalized atention from the team, depending on the type of event desired.
  * B2C services available can be stored in a shopping bag and bought online through Stripe API.
  * All users can subscribe to the monthly newsletter.


## USER STORIES

### As a first time B2C or B2B visitor 
- [X] View available worlds.
- [X] View world detail pages.
- [X] View each worlds' details page images in full size
- [ ] Check the About page.
- [X] Send a request through a form
- [X] Sign up for an account after a conscient decision, to be able to make a booking.


### As an Authorized User 
- [X] Easily log in and log out.  
- [X] Easily recover my password in case I forget it.
- [X] Receive an email to confirm my registration, so that I can be sure of my credentials.
- [X] View a confirmation message after registering.  
- [X] Make a booking selecting the world and time.   
- [X] View a list with my bookings after sending the booking form.
- [X] Update or delete my bookings.  
- [X] View confirmation message on the site for every action taken.
- [X] Be sure that no one else can access my bookings. 

## SITE OWNER STORIES
As a site owner, the following functionalities have been included on this site, to manually access and set the following:
- [X] Add, update or delete worlds directly from the admin.  
- [X] Style the font size and display of each world's details page.
- [X] Add, update of delete images from the world's details page.
- [X] Access contact requests sent by users throkugh the contact form to the admin.
- [X] Display clearly if the request sender is an authenticated user or not.
- [X] Know if the request sender is a acting on behalf of a company.
- [ ] Edit the about page from the admin.


## USER PROFILES

### B2C
- Steve is a romantic man in his thirties and wants to surprise his partner with a very special gift for a special occasion
- Siham is looking for a special gift for her parents' anniversary
- Wendy and Peter want to celebrate their 25th anniversary and build more special memories together. 

### B2B
- Oisin is the CEO of a large company and wants to offer a special treat to the managers after reaching an importnt milestone.
- Maeve is the owner of a family-owned establishment and wants a special 1st price for a raffle.



## WIREFRAMES

### MOBILE & TABLET (Portrait)

<details>
<summary>Click here to see the Mobile & Tablet (portrait) Wireframes</summary>
- HOME Page
 
  - ![image](https://github.com/user-attachments/assets/bdcef926-47f9-47eb-86b5-23580f5f2448)

- WORLDS Page
  - ![image](https://github.com/user-attachments/assets/b8ae0f97-1a63-4d0c-a0cb-be636aa19962)

- WORLD DETAILS Page
  - ![image](https://github.com/user-attachments/assets/2570940e-31ce-4774-86a2-e8073c9d5f51)

- NEW BOOKING Page (form)
  - ![image](https://github.com/user-attachments/assets/a042a479-bba2-405f-b75f-c89924ac140a)

- MY BOOKINGS Page (list)
  - ![image](https://github.com/user-attachments/assets/9802a0f9-9418-4c19-a654-e494d49eb5f4)

- CONTACT Page (form)
  - ![image](https://github.com/user-attachments/assets/d208fb55-37d4-408e-97dc-5454c191ee2e)

- ABOUT Page
  - 
</details>  

  
### DESKTOP & TABLET (Landscape)

<details>
<summary>Click here to see the Desktop & Tablet (landscape) Wireframes</summary>
- HOME Page
  
  - ![image](https://github.com/user-attachments/assets/39bc1b2d-1cc4-4619-b63a-2d98d5a1ddd0)

- WORLDS Page
  - ![image](https://github.com/user-attachments/assets/c007a6fe-a6ff-426b-af68-eb420f1e78ea)
  
- WORLD DETAILS Page
  - ![image](https://github.com/user-attachments/assets/7445f09b-e381-4ffe-8636-f530ea9c3c7b)

- NEW BOOKING Page
  - ![image](https://github.com/user-attachments/assets/97f377ed-9551-471f-abb1-b680d94d0142)

- MY BOOKINGS Page
  - ![image](https://github.com/user-attachments/assets/10638afe-57ed-418c-bfcf-d85f4d5d1707)

- CONTACT Page
  - ![image](https://github.com/user-attachments/assets/462ad81a-57f4-4f23-a44b-47b13f51ee4b)

- ABOUT Page
  - 
</details>


# AGILE METHODOLOGY
Agile methodologies and principles guide the planning and creation of thi site. While not adhering strictly to traditional Agile methodologies, such as scheduled sprints or scrums, the development process has been based on Agile principles, focusing on flexibility, continuous improvement, and rapid adaptation to change. Instead of using sprints, we focus directly on the priority level of the User Stories within each epic.  

The approach is straightforward: develop features in a logical sequence, addressing core functionalities first before expanding to more complex features.

## GITHUB PROJECT - KANBAN
When bugs or issues are encountered, they are recorded as bug issues and added to the backlog, to the 'bug' column. This allows us to continue progressing in other areas while periodically revisiting and prioritizing the backlog based on severity and impact. This method ensures that we maintain development, while systematically addressing and resolving issues.

A project kanban board has been used to track progress, moving user stories between 'Todo', 'In Progress', 'Bug', and 'Done' columns as appropriate.
You can check the Kanban project [here](https://github.com/users/Ethra8/projects/8)


# TESTING

## COMPATIBILITY AND RESPONSIVE TESTING

### PRESELECTING TESTING TARGETS
- To meaningful testing of site, [Stat Counter](https://gs.statcounter.com) has been used, in order to get an insight of the following:
    
    * **BROWSER MARKET SHARE** - Most commonly used browsers worldwide:

    ![image](https://github.com/user-attachments/assets/7a7c49ff-13d3-48f9-ae03-1a4e84a70167)

     * **BROWSER VERSION MARKET SHARE** - Most commonly used browser versions worldwide:

    ![image](https://github.com/user-attachments/assets/05f21ad4-3469-4e97-b870-f6f6334751f5)

    * **OS MARKET SHARE** - Most commonly used operation systems worldwide:

    ![image](https://github.com/user-attachments/assets/217ec506-783f-455c-b6e3-821f5269c326)

    * **MOBILE vs DESKTOP vs TABLET MARKET SHARE** - Most commonly used devices worldwide:

    ![image](https://github.com/user-attachments/assets/7b5b8335-2f93-46a8-908b-4e470b42f2a4)

    * **SCREEN RESOLUTION STATS** - Most common screen resolution (in pixels) worldwide:

    ![image](https://github.com/user-attachments/assets/550ec6df-12c2-4055-8662-53c6758dc221)



### TESTING TARGETS TABLE
Following all the above information, compatibility and responsive testing has been done on the most common *browser versions*, *OS*, and *screen resolution* combinations, by using [Browser Stack](https://chrome.google.com/webstore/detail/browserstack/nkihdmlheodkdfojglpcjjmioefjahjb) Chrome extension, which has been downloaded, the *Chrome Dev tool's emulator*, and real devices owned by me. 

Please find the correspondent **compatibility and responsive testing** reflected in the following table:

| TEST no.| TOOL               | DEVICE               | BROWSER            | OS              | VIEWPORT width x height (px) |
|---------|--------------------|----------------------|--------------------|-----------------|------------------------------|
| 1       | Chrome Dev emulator| Samsung Galaxy S20   | Chrome 117         |Windows 10       |360 x 800                     | 
| 2       | BrowserStack       | Samsung Galaxy S22   | Chrome             |Android 12.0     |360 x 780                     |
| 3       | BrowserStack       | Samsung Galaxy S22   | Edge               |Android 12.0     |360 x 780                     |
| 4       | BrowserStack       | iPhone 12 Mini       | Safari             | iOS 16.0        |360 x 780                     |
| 5       | Blisk              | iPhone SE 2022       | Chrome             | iOS             |375 x 667                     |
| 6       | REAL mobile device | Samsung Galaxy A22 5G| Chrome             | Android 13.0    |384 x 857                     |
| 7       | BrowserStack       | iPhone 13            | Safari 17.0        | iOS             |390 x 844                     |
| 8       | BrowserStack       | iPhone 14 Pro        | Safari 16.3        | iOS             |393 x 852                     |
| 9       | REAL Laptop Device | PC Notebook HP -15-bs013ns| Chrome 117    |Windows 10 -64bit|1366 x 768                    |
| 10      | Blisk              | MacBook Pro          | Chrome 117         | macOS           |1440 x 900                    |
| 11      | BrowserStack       | Asus ZenBook UX305   | Edge               |Windows 11       |1920 x 1080                   |
| 12      | BrowserStack       | Asus ZenBook UX305   | Firefox 117        |Windows 11       |1920 x 1080                   |
| 13      | BrowserStack       | MacBook              | Safari 16.5        | OS X Ventura    |1920 x 1080                   |



# TECHNOLOGIES and METHODOLOGIES USED
**The following technologies have been used to create this site and to deploy it. The AGILE methodology has been approached and a kanban board is linked to this project. For further det that can be viewed [here](#)**
## LANGUAGES
  - **Python 3.12.2**
  - **JS ES6**
  - **CSS3**
  - **HTML5**

## Frameworks, Libraries and Programs
  - **Django 5.1** - Whithin django framework, many libraries and modules have been used. For mode details, please refer to the requirements.txt file in the root directory.
  - **Bootstrap 5**
  - **Cloudinary** - Database for images
  - Chrome Dev Tools - To inspect the elements, and be able to spot what element was having an unexpected behaviour, and correct it more efficiently. Also have used Lighthouse reports to check and improve core web vitals, including accessibility issues.
  - [Favicon](https://favicon.io/) - To create the logo, and the icon on the title included in each page of this site
  - [Font Awesome](https://fontawesome.com/) - For the icons used
  - [Google Fonts](https://fonts.google.com/) - To select fonts and implement them in the site
  - [Github](https://github.com) - To deploy the site online, and Github desktop app to link _Visual Studio Code_ to Github.com
  - [Coolors](https://coolors.co) - To insert colors selected previously directly through visual studio code, but used this tool to display the palette beautifully, and insert it in this readme file.
  - [Amiresponsive](https://ui.dev/amiresponsive) - To display the site in all types of devices simultaneously.
  - [EqualWeb Accessibility Checker](https://chrome.google.com/webstore/detail/equalweb-accessibility-ch/imemciokfejbnonkkinhcdfigdilcllg/related?utm_source=chrome-ntp-icon) - Google Chrome extension to check general errors and contract errors for optimal accessibility.
  - [Juicy Studio](https://juicystudio.com/services/luminositycontrastratio.php) tool to generate accessibility reports related to contrast, following the **WCAG 2.0**'s luminosity contrast algorithm.


# DEPLOYMENT
## VERSION CONTROL
The site was created using Gitpod editor and pushed to Github to the remote repository **‘candlelight-wolds’**.  
The following git commands were given to the terminal throughout development to push updated code to the remote repo on Github:
1. ```git add .``` - Command to add the updated file(s) to the staging area before they are committed to the *main branch*, represented by a '**.**'.
2. ```git commit -m “commit text”``` - Command to commit changes to the local repository queue ready for the final push.
3. ```git push``` - Command to push all updated code to the remote repository on Github.
4. ```python3 manage.py runserver``` - Command to run **python** app on local server.

### SECRETS
To avoid pushing sensible credentials stores in variables (e.g.: DATABASE_URL, SECRET_KEY) to Github:
1. Create an ***env.py*** file on the main directory of the app.
2. Ensure that env.py is included in the ***.gitignore*** file.
3. To include secret variables on the env.py file:
   - (i) On the top of the file, include the imports:
   -```import os
       from pathlib import Path```
   - (ii) Include eac hsecret var following this example:
   - ```os.environ.setdefault('DATABASE_URL', 'your-data-base-url')```
   - (iii) Import Operational System to your ***settings.py***, so it can access the system variables secretly stored in your env.py file:
   - ```import os```
   - (iv) To access the system variables in your settings.py file, use the following method to store them in other safe variables:
   - ```DATABASE_URL = os.environ.get("DATABASE_URL")```
4. BEFORE COMMITTING TO GITHUB:
   - On the terminal, type ```git add .```, then ```git status``` and make sure the env.py file is not in the list. Once you are reassured that it is not in the list of files to be committed, safely commit.

## HEROKU
### App Preparation
1. Create and add the **'Procfile'** to the root directory of the app, and include ```web: gunicorn candlelight.wsgi --log-file -```  Heroku relies on this file to determine how to run your application, ensuring the correct setup of your web server. Use commands like ```web: gunicorn PROJ_NAME.wsgi``` in the 'Procfile' to instruct Heroku on starting your web server with Gunicorn.
2. If you haven't done so yet, create a ***requirements.txt*** file to store necessary modules and libraries:
   - ```pip3 install -r requirements.txt```
3. Ensure you have updated the ***requirements.txt*** file listing all project dependencies. The comnmand to update the file is ```pip3 freeze > requirements.txt```
4. Set up necessary **configuration variables** in Heroku ***setting tab > Config Vars*** *(eg. SECRET_KEY, DATABASE_URL, etc.)*.
5. Add Heroku to your ALLOWED_HOSTS in your app's *'settings.py'* file: ```candlelight-worlds.herokuapp.com```.
   
### Create Heroku App
1. Sign up to an account on [Heroku](https://heroku.com)
2. Create new app. Remember that app name must be unique on the whole of Heroku site.
   - ![image](https://github.com/user-attachments/assets/43f0170f-e3dd-4651-9a32-d287f6237b17)

3. Store all the secret environment variables (secret keys) on **settings** > **Config Vars**:
   - ![image](https://github.com/user-attachments/assets/48671b5e-99a8-4472-97b8-94af79a84ad5)
     
### Deployment Method
1. Ensure that in your **settings.py**, ```DEBUG = False``` before doing the last commit to Github.
2. **On Heroku**, click the **deploy** tab
3. Scroll down and select Github
4. Use the github link and type in the name of your repository
5. Click **deploy from branch** and select *main*
6. Once your application is running, switch to **Automatic Deploys** so that any changes are automatically reflected in Heroku deployed app.  
  
  
# CREDITS & ACKNOWEDGEMENTS

## IMAGES
- [Hero image](https://www.freepik.com/free-photo/couple-having-dinner-valentines-day_6412178.htm#query=dinner%20candlelight&position=32&from_view=keyword&track=ais&uuid=0b778147-a7c9-4ab5-a148-ddd91935661c) by [Freepik](https://www.freepik.com/author/freepik) at [Freepik](https://www.freepik.com/)
- [Candle on the index page background](https://www.freepik.com/free-photo/enchanting-glow-fairy-lights-candles-creating-magical-ambiance_136714970.htm) by AI at [Freepik](https://www.freepik.com)
- Medieval Castle Bedroom - AI generated (ChatGPT)
- Medieval Castle Dinning Table - AI generated (ChatGPT)
- Medieval Castle Jakuzzi - AI generated (ChatGPT)
- Italian Renaissance Villa Dinning Area - AI generated (ChatGPT)
- Italian Renaissance Villa Bedroom - AI generated (ChatGPT)
- Italian Renaissance Villa Jakuzzi - AI generated (ChatGPT)

## ACKNOWLEDGEMENTS
- Sites thoroughly researched: [Stackoverflow](https://stackoverflow.com/), [Django Projecc Forum](https://forum.djangoproject.com/), 

