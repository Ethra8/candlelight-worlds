# CANDLELIGHT WORLDS
![image](https://github.com/user-attachments/assets/8bde8516-951f-4d6c-acc5-739914f6e475)


## PROJECT OVERVIEW
- A booking site for a business that offers different **out-of-the-box romantic day or night experiences** including meals vailable in two different time frames: daytime & nightime -daytime includes brunch and lunch, and nightime includes dinner and breakfast.
- This new concept involves **private spaces called worlds, each exquisitely decorated to transport our guests to different times and places**. Each private world includes three areas: The **Dining Area**, an in-room or bathroom king-size **Jakuzzi**, and a **Resting Area** (or *siesta* area) furnished with a king size bed and fine linen.
- The project's name reflects the very ***essence*** of the primary idea of the owner, which is to make **worlds fully immersed in a warm candlelight lighting**, which undoubtedly fosters a unique and unforgetable atmosphere.
- Our **tasty dishes** are carefully selected with recipes from around the world, **adapted to each world's theme** and served by our discreet and professional table service.


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
  * [Design Choices](#design-choices)
    - [Color Palette and Rationale of Use](#color-palette)
    - [Typography and Rationale of Use](#typography)
  * [Wireframes](#wireframes)
  * [Features](#features)
  * [Pages](#pages)
  * [CRUD Functionality](#crud-functionality)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
  * [Send Verification Email](#verification-email)
- [TESTING](#testing)
  * [Code Validation](#code-validation)
  * [Defect Tracking](#defect-tracking)
    - [Github Issues](#github-issues)
    - [Defects of Note](#defects-of-note)
    - [Outstanding Defects](#outstanding-defects)
  * [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
    - [Preselecting Testing Targets](#preselecting-testing-targets)
    - [Testing Targets Table](testing-targets-table)
    - [Test Result Videos](test-results-videos)
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
  * [AGILE Methodology](#agile-methodology)
     - [Github Project - Kanban](#github-project---kanban)
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
  
- **B2C:**
  * Couples at any age wanting to add special memories
  * Someone looking for the special gift to offer

- **B2B:**
  * Companies that might want to offer a special gift to their premium clients or collaborators
  
## GOALS

### PROJECT GOALS
  
  * The site aims at providing customers with luxuriously themed private spaces where to have any meal of the day.
  * Any users can register for an authenticated account to store, read, update and cancel their bookings.
  * All users can send a request via a contact form to receive personalized atention from the team.

### EXTERNAL USER'S GOAL

  * The user would like to book a world in an out-of-the-box experience/restaurant and a particular time and date.
  
### SITE OWNER'S GOAL

  * The site owner would like the ability to take online bookings for their eatery.


## USER STORIES
To make the user experience on the site seamless and meaningful, the following stories have been followed as a guide to implementing functionalities of the site:
#### As a first time B2C or B2B visitor 
- [X] View available worlds.
- [X] View world detail pages.
- [X] View each worlds' details page images in full size
- [X] Check the About page.
- [X] Send a request via a contact form
- [X] Sign up for an account after a conscient decision, to be able to make a booking.
  
#### As an Authorized User 
- [X] Easily log in and log out.  
- [X] Easily recover my password in case I forget it.
- [X] Receive an email to confirm my registration, so that I can be sure of my credentials.
- [X] View a confirmation message after registering.  
- [X] Make a booking selecting the world and time.   
- [X] View a list with my bookings after sending the booking form.
- [X] Update or delete a booking.  
- [X] View confirmation message on the site for every action taken.
- [X] Be sure that no one else can access my bookings. 
  
## SITE OWNER STORIES
To make the site owner's life easier, the following functionalities have been included on this site, to manually access and update the following from the admin panel, without touching any code:
- [X] Add, update or delete worlds directly from the admin.  
- [X] Edit and style the text of each world.
- [X] Add, update or delete images from each world.
- [X] Access from the admin the contact requests sent by users via the contact form.
- [X] Display clearly if the request sender is an authenticated user or not.
- [X] Display clearly if the request sender is a acting on behalf of a company.
- [ ] Edit and style the text, display and image of the about page from the admin panel.
  
  
## USER PROFILES
### B2C
- Steve is a romantic man in his thirties and wants to surprise his partner with a very special gift for a special occasion
- Siham is looking for a special gift for her parents' anniversary
- Wendy and Peter want to celebrate their 25th anniversary and build more special memories together. 

### B2B
- Oisin is the CEO of a large company and wants to offer a special treat to the managers after reaching an importnt milestone.
- Maeve is the owner of a family-owned establishment and wants a special 1st price for a raffle.


# UI

## DESIGN CHOICES

## HERO IMAGE
This site has the following hero image:  
  
  ![bg-candles1 c539123d66b8](https://github.com/user-attachments/assets/d55c2807-32cb-4dc2-8041-5bc74599c283)  
  

## COLOR PALETTE
This site has the following palette, picked specifically to emulate real candlelight and the shadows it provokes. The colours have carefully been picked inspired by the hero image of the site, which is always ppresent, fixed on the body element of the *base.html* file:   
  
  ![candlelight color palette](https://github.com/user-attachments/assets/a2c1ebea-e3f2-40ea-87a1-6fa16cbb9ef9)  
  
  
## TYPOGRAPHY
This site's fonts have been selected from [Google fonts](https://fonts.google.com/):
- [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montserrat): Used on all the paragraphs of the site, and it is the default font of the body element.
- [Montserrat Alternates](https://fonts.google.com/specimen/Montserrat+Alternates?query=montserrat): Used only for the name of the worlds, to give a special *exotic* touch without deviating of the main font style specified above.
- [Lato](https://fonts.google.com/specimen/Lato?query=lato): Used only for the **main title** of the site and for the **logo**.
- [Shadows Into Light](https://fonts.google.com/specimen/Shadows+Into+Light?query=Shadows+Into+Light): Used only for the **slogan** *'travel through space and time'* on the landing page below the main title.

## WIREFRAMES

### MOBILE & TABLET (Portrait)

<details>
<summary>Click here to see the Mobile & Tablet (portrait) Wireframes</summary>
- HOME Page
 
  - ![image](https://github.com/user-attachments/assets/bdcef926-47f9-47eb-86b5-23580f5f2448)

- WORLDS Page
  - ![image](https://github.com/user-attachments/assets/b8ae0f97-1a63-4d0c-a0cb-be636aa19962)

- WORLD DETAILS Page
  - ![image](https://github.com/user-attachments/assets/f5d59d71-70bf-4c8d-b86c-ecf0046fb301)

- NEW BOOKING Page (form)
  - ![image](https://github.com/user-attachments/assets/a042a479-bba2-405f-b75f-c89924ac140a)

- MY BOOKINGS Page (list)
  - ![image](https://github.com/user-attachments/assets/9802a0f9-9418-4c19-a654-e494d49eb5f4)

- CONTACT Page (form)
  - ![image](https://github.com/user-attachments/assets/d208fb55-37d4-408e-97dc-5454c191ee2e)

- ABOUT Page
  - ![image](https://github.com/user-attachments/assets/dca1cdec-264f-4a42-8078-3c1331951d5b)


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
  - ![image](https://github.com/user-attachments/assets/a0eb920b-754e-4eb5-982a-1a6460911556)

- ABOUT Page
  - ![image](https://github.com/user-attachments/assets/531ef85a-96bd-4612-b8c2-528b49e48ef4)

</details>


## FEATURES     
**Responsiveness**: All pages and features are fully responsive - please refer to the [Testing Targets Table](#testing-targets-table) or the [Responsive Testing Videos](#test-result-videos) for further details.
- 
**Accessibility**: This site takes accessibility very seriously, and has performed different tests. All the reports can be checked [here](#accessibility-testing)
-
This site contains the following features:
- **NAVIGATION BAR**: Fixed to the top to make it easy for users to navigate around the site at any time. Contains links to ***worlds, contact, and about page***, and acces to ***user's account***, which includes a dropdown whose options vary depending on whether the user is authenticated or not. If it is an **authenticated user**, the user icon dropdown shows the options ***new booking, my bookings, logout***; Whereas when the user is **not authenticated** in case the user is not authenticated, the dropdown options are ***login, register***:
  * **Mobile & Tablet (portrait)**
    |collapsed| uncollapsed|
    |---------|------------|
    |![image](https://github.com/user-attachments/assets/35d96ba1-02f2-4b87-a77e-461aab85d596)|![image](https://github.com/user-attachments/assets/3727364d-f1c8-4ede-ba52-e98592dd5e58)|


  * **Desktop & Tablet (landscape)**
      
   ![image](https://github.com/user-attachments/assets/6175b242-af16-48de-b152-3a86f5bfd155)

     

- **Backgroung image**: Fixed to the background of the body, the hero image takes up all of the available space in all types fo devices.
- **Background overlay**: Fixed an the upper layer of the background image, it increases opacity of hero image fixed on the body to *improve visual accessibility* of text.
- **Footer**: Pushed to the bottom, contains social media icons with links to each social media pages.
- **Booking Form**: A *crispy form* to book a world. The form contains a styled *Book Now* button below the following fields:
  * ***World selector***: Prepopulates automatically when user accesses the bookign form from the *Book Now!* button on the *world details page*
  * ***Date picker***
  * ***Time frame*** selector
- **Contact Form**: A ***crispy form*** to contact the site's owner. a styled *Submit* button below the following fields, all of which are mandatory but the *company name* field:
  * ***name****
  * ***company name*** - in case a company wants to contact, and keep trac kof B2B customers and request.
  * ***email****
  * ***message****
- **Buttons**: All buttons are styled equally for design consistency. The *background colour* is the main theme colour *#f69700*. On *hover*, it slightly darkens to *#b57002* while the *font* colour remains dark grey *#21201e*.
- **Icons**: All icons are taken from *Fontawesome*, and have been styled to match the site's design:
  * *User icon*: Placed on the navigation bar, it enables unidentified users to easily login or register for an account, and also enables authentified users to access their booking list, and to logout. It has been styled matching the main colour of the theme #f69700.
  * *Update Booking icon*: Placed on each individual booking item on the *Booking List* page, it enables the user upon clicking it to update the booking to a new date, time, or world all together. Its colour matches the font's light grey of the site #dbd0ba, and *on hover*, it turns to the main theme's *'candlelight'* colour #f69700.
  * *Delete Booking icon*: Placed on each individual booking item on the *Booking List* page, it enables the user upon clicking it to delete the booking. Its colour matches the font's light grey of the site #dbd0ba, and *on hover*, it turns to the main theme's *'candlelight'* colour #f69700.

  
## PAGES
This site contains the following responsive pages, all of which contain the following features which are placed on the **body** element of the *base.html* template, that acts as the main dynamic *django template* for all the other pages of the site. For further details on each feature of the **body** which frames each page, please refer to [features](#features).  
These are the features of the **body**, present in all pages:  
- **Navigation Bar**
- **Backgroung hero image**
- **Back transparent overlay**
- **Footer**

  
### HOME PAGE
The **home page** corresponds to the *index.html* template, acting as the landing page of the site, from the *home app* from the *home.views.index* view in the *home app and contains the following features:
- **Main body element** - As detailed on the ***pages section description*** [above](#pages)
- **Main Header of the site**:
  * ***Title*** of the site: Its colours guide the theme of the site -*CandleLight* in #f69700, and *Worlds* in white, standing out from the light grey of the rest of the text on the site.
  * ***Slogan*** of the site: *'Travel through space and time'* styled in a light grey #dbd0ba font *Shadows Into Light*.

#### DESKTOP
  
  ![image](https://github.com/user-attachments/assets/315d5c51-4eee-4aa1-b84d-328f347184d5)

#### MOBILE

  ![image](https://github.com/user-attachments/assets/4edbc2b4-b2a5-4ee9-882e-eaecda381613)

  
### WORLDS PAGE
The **worlds page** corresponds to the *worlds.html* template from the *worlds app*, and contains the following features:
- **Main body element** - As detailed on the ***pages section description*** [above](#pages)
- **List of individual world cards**: Each world card is responsive, and includes a *short description*, the *picture* of the world's *dining area*, and a *button* to "see details" of that specific world.  

#### DESKTOP
  
  ![image](https://github.com/user-attachments/assets/8f442a73-d68f-4d94-9636-28ac66a8e714)   

#### MOBILE

  ![image](https://github.com/user-attachments/assets/68584e00-4b70-4135-a802-4fa635cb4337)  

  
### WORLD DETAILS PAGE
The **world details page** corresponds to the *world_details.html* template from the *worlds app*, and contains the following features:
- **Main body element** - as detailed [above](#pages)
- **Details of the selected world**: Responsive display of the world's details, which include:
   * *Title* - The world's name.
   * *Detailed description* of each of the three areas it includes *(dining area, jakuzzi, and resting area)*
   * *Three images* - Each one corresponding to one of the world's areas. 
   * *Price* - The world's price
   * *Button* - A button styled as detailed in the [feature section](#features) that reads 'Book Now!'.

 #### DESKTOP

   ![image](https://github.com/user-attachments/assets/98021936-5759-44a5-8047-69d714b909f2)   

 #### MOBILE

   ![image](https://github.com/user-attachments/assets/5ad29dce-5e11-482b-b5b2-4701078636c3)


### BOOKING FORM PAGE
The **booking form page** corresponds to the *booking_new.html* template from the *bookings app*, and can only be accessed if a user is authenticated, and stored in the user's account. It contains the following features:
- **Main body element** - As detailed on the ***pages section description*** [above](#pages)
- **Booking Form**: Responsive *django-crispy* form, which generates taking the user includes te following fields, all mandatory:
   * *Title* - 'Booking Form'.
   * *World* - A dropdown with all the worlds for the user to make the selection. When the user accesses the page from a specific world's details page, this field is prepolulated with that world.
   * *Date* - A date picker to select the date.
   * *Time* - A dropdown with two available time frames (daytime or nightime) for the user to select.
   * *Button* - A button styled as detailed in the [feature section](#features) that reads 'Book Now'.

#### DESKTOP

  ![image](https://github.com/user-attachments/assets/3b6ca673-9874-4ec2-9827-8d0d67474bdc)

#### MOBILE

  ![image](https://github.com/user-attachments/assets/612126e8-cde6-478f-a4d5-4fcbc0da2b82)


### BOOKING LIST PAGE
The **booking form page** corresponds to the *booking_new.html* template from the *bookings app*, and can only be accessed if a user is authenticated, and stored in the user's account. It contains the following features:
- **Main body element** - As detailed on the ***pages section description*** [above](#pages)
- **Booking Form**: Responsive *django-crispy* form, which generates taking the user includes te following fields, all mandatory:
   * *Title* - 'Booking Form'.
   * *World* - A dropdown with all the worlds for the user to make the selection. When the user accesses the page from a specific world's details page, this field is prepolulated with that world.
   * *Date* - A date picker to select the date.
   * *Time* - A dropdown with two available time frames (daytime or nightime) for the user to select.
   * *Button* - A button styled as detailed in the [feature section](#features) that reads 'Book Now'.

### BOOKING UPDATE PAGE

  
### CONTACT PAGE

  
### 404 ERROR PAGE
Whenever the user erroneously changes an url, or a 404 error occurs, this page will display, instead of the default page that google would display for the error. The page mimics the home page in style and display of the elements contained, and has been minimally adapted for the purpose of the page:
- **Main body element** - As detailed on the ***pages section description*** [above](#pages)
- **Header** - Mimics the home page header, also with the same added black transparency with a 0.95 opacity for an optimal accessibility. It contains: 
   * *Title* - '404 Error'.
   * *Button* - A button styled as detailed in the [feature section](#features) that reads 'Back Home'.

#### MOBILE

  ![image](https://github.com/user-attachments/assets/badec76b-ed5c-4553-a229-64d06535d276)


#### DESkTOP

  ![image](https://github.com/user-attachments/assets/be12bb78-6b23-48d9-a1f2-746c8cb1ec51)



## CRUD FUNCTIONALITIES
The following basic *CRUD* functionalities have been implementes to this site, as detailed below:  
  
### CREATE
1. Users can **create an account** by accessing the *sing-up* option in the dropdown of the user-icon placed in the navigation bar. They then become authenticated users.
2. The authenticated user can **create a booking** via the *booking form*, generated by crispy forms after the ***bookings.models.Booking*** **model** and ***bookings.forms.BookingForm*** **form** displayed by the ***bookings.views.booking_new*** **view** via two different urls the ***/bookings/new*** **url** on the ***booking_new.html*** **template** which is stored in the project directory folder ***bookings/booking_new.html***.
### READ

### UPDATE

### DELETE

## VERIFICATION MAIL - STMP
The user authentication requires **email verification** for the registration to succeed. This site uses sends verification emails via *smtp*. To do so, please follow these instructions if you are using Gmail services:  

### EMAIL ACCOUNT SETUP

1. Create an account for the site. 
2. Activate 2-Way Authentication - This is a requirement for the following crucial step:

   ![image](https://github.com/user-attachments/assets/ca27a242-f372-415c-b829-617db5944c39)
   
4. Create App Password:
   
   ![image](https://github.com/user-attachments/assets/8f46a8b4-9aba-4619-8168-9870973d9c91)

5. Include the name of the app -or site-, and create the app password, which is automatically generated:  

   ![image](https://github.com/user-attachments/assets/de079b2e-3b16-40f7-b8ef-69c3dbe856cc)
  
  
### SETTINGS
To implement stmp emaling service necessary for user authentication and email verification upon regis
  
1. On the ***settings.py*** file, include the following environment variables:
  ```
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
  EMAIL_USE_TLS = False
  EMAIL_PORT = 587 # HTTPS secure port - for development, use 465 HTTP
  EMAIL_USE_SSL = True
  EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
  DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
  ```
  
NB: The EMAIL_BACKEND during the development fase is ```EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'```, and emails get printed in the console. Remember to comment out or create 'if' statement before deplloy in order to change the default django backend the *smtp* .

2. **IMPORTANT WARNING: Never disclose private information nor credentials such as EMAIL_HOST_USER or EMAIL_HOST_PASSWORD!:
   Store the above environment variables on the ***env.py*** with your own credentials, and include the *app password* in the EMAIL_HOST_PASSWORD var:**
   ```
   os.environ['EMAIL_HOST_USER'] = '<example@email.com>'
   os.environ['EMAIL_HOST_PASSWORD'] = '<app-password-generated-without-spacing>'
   os.environ['DEFAULT_FROM_EMAIL'] = '<emailsendertocustomer@example.com>'
   ```

### CONFIGURE ADMIN PANEL - SEND EMAIL
Default configuration of the sender from whom the user receives mails sent from the site need to be customized. Otherwise, this is the email sender the user receives with the default configuration:  
  
  ![image](https://github.com/user-attachments/assets/a983a69f-1b60-4a90-85d7-86a264e95fcf)  

- **To replace the default <example.com> displayed with the site url**:
  1. Go to admin **Sites**, and select default site:  
  
    ![image](https://github.com/user-attachments/assets/b6f5e810-17ff-4d27-a90a-cb53c10dab17)  
    
    ![image](https://github.com/user-attachments/assets/f9fc7b85-be42-4f1c-97f7-5eb403400bf9)  
  
  2. **Update default settings** of site name and url:  
    
    ![image](https://github.com/user-attachments/assets/9d40ec27-b7f5-4c94-8a9e-a41bcae84ad3)  
    ![image](https://github.com/user-attachments/assets/e14a4179-5b5c-44af-93d6-a42274e323d4)  
    
  
# TECHNOLOGIES and METHODOLOGIES USED
The following technologies, frameworks, libraries, programs and methodologies have been used to create this site and to deploy it. The AGILE methodology has been approached and a kanban board is linked to this project. More details on the sections below: 
-
  
## LANGUAGES
  - **Python 3.12.2**
  - **JS ES6**
  - **CSS3**
  - **HTML5**
  
## FRAMEWROKS, LIBRARIES and PROGRAMS
  - **Django 5.1** as MVC Framework - Within django framework, many libraries and modules have been used. Some of the more relevant are states below, but for further reference, please refer to the requirements.txt file in the root directory. - Check [Django 5.1 Documentation](https://docs.djangoproject.com/en/5.1/)
  - **Bootstrap 5** - Check documentation [here](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
  - **Cloudinary** - Database for images uploaded through the admin panel to configure each worlds item. Check documentation [here](https://cloudinary.com/developers#:~:text=Android-,Documentation,-Check%20out%20our)
  - **PostgreSQL** Relational Database - To store static files, such as the custom *styles.css* file of the site.
  - **Django Summernote** - To enable the site owner to style the description of a world when creating or updating it. Documentation can be found [here](https://github.com/lqez/django-summernote/blob/main/README.md)
  - Chrome Dev Tools - To inspect the elements, and be able to spot what element was having an unexpected behaviour, and correct it more efficiently. Also have used Lighthouse reports to check and improve core web vitals, including accessibility issues.
  - [Favicon](https://favicon.io/) - To create the necessary files for the logo to be on the upper part of the browser tab next to the site tir.
  - [Font Awesome](https://fontawesome.com/) - For the icons used
  - [Google Fonts](https://fonts.google.com/) - To select fonts and implement them in the site
  - [Github](https://github.com) - To deploy the site online, and Github desktop app to link _Visual Studio Code_ to Github.com
  - [Coolors](https://coolors.co) - To insert colors selected previously directly through visual studio code, but used this tool to display the palette beautifully, and insert it in this readme file.
  - [Amiresponsive](https://ui.dev/amiresponsive) - To display the site in all types of devices simultaneously.
  - [EqualWeb Accessibility Checker](https://chrome.google.com/webstore/detail/equalweb-accessibility-ch/imemciokfejbnonkkinhcdfigdilcllg/related?utm_source=chrome-ntp-icon) - Google Chrome extension to check general errors and contract errors for optimal accessibility.
  - [Juicy Studio](https://juicystudio.com/services/luminositycontrastratio.php) tool to generate accessibility reports related to contrast, following the **WCAG 2.0**'s luminosity contrast algorithm.
  - [Blisk](https://blisk.io/devices) to check the viewport of multiple devices, very useful for selecting testing targets.
  - [Viewport Sizer](https://viewportsizer.com/devices/) - Used to check the viewport of multiple devices, very useful for selecting testing targets.
  - [BrowserStack](browserstack.com) to test responsiveness by emulating different devices, operating systems and browser vendors.
  - [XRecorder](https://videoeditor-videorecorder-screenrecorder.en.uptodown.com/android) for Android, to record the compatibility and responsiveness testing performed on real Android device.
  - [Google Gmail](https://support.google.com/mail/answer/56256?hl=en#:~:text=Gmail-,Create%20a%20Gmail%20account,-To%20sign%20up): Used as email provider to send  emails to users and customers, also via *smtp*.  
    
    
## AGILE METHODOLOGY
Agile methodologies and principles has guided the planning and creation of this site. Eventhough it does not strictly adhere to traditional Agile methodologies, the development process has been based on Agile principles, focusing on flexibility, continuous improvement, and an agile adaptation to change. The focus has been put on the priority level of the [***User Stories***](#user-stories), adding extra features once the basic functionality had been satisfied. The development of features has been made in a logical sequence, addressing core [***CRUD functionalities***](#crud-functionalities) first before expanding to the other features.
  
   
### GITHUB PROJECT - KANBAN
When bugs or issues are encountered, they are recorded as bug issues and added to the backlog, to the 'bug' column. This allows us to continue progressing in other areas while periodically revisiting and prioritizing the backlog based on severity and impact. This method ensures that we maintain development, while systematically addressing and resolving issues.

A **kanban board** has been linked to this project, and has been used to track progress, moving **user stories** between *'Todo'*, *'In Progress'*, *'Done'*, *'Bug'*, and *Fixed Bug* columns as appropriate.
You can check the Kanban project [here](https://github.com/users/Ethra8/projects/8)



# TESTING

## CODE VALIDATION
### HTML5
No errors nor warnings appear uppon HTML code validation. The validate the HTML code, I have used the [Nu HTML Checker](https://validator.w3.org/nu/) from W3C.
- **HOME PAGE** *home/index.html* file  
  ![image](https://github.com/user-attachments/assets/d20e0472-885f-4675-b3c0-622b614973cd)
  
- **WORLDS PAGE** *worlds/worlds.html* file  
  ![image](https://github.com/user-attachments/assets/5c612c61-4e6a-4119-b6e3-65a9a55a8a35)
  
- **WORLD DETAILS PAGE** *worlds/world_details.html* file  
  ![image](https://github.com/user-attachments/assets/1f3714d3-1a5c-4002-a747-90b2384b3c9f)

- **NEW BOOKING PAGE** *bookings/booking_form.html* file
  ![image](https://github.com/user-attachments/assets/bc636956-dc6f-45e5-be14-6969e691bb64)  
  
- **MY BOOKINGS PAGE** *bookings/booking_list.html* file
  ![image](https://github.com/user-attachments/assets/bc74861a-8d5b-4dc2-b894-dd24d5a439a1)
  
- **BOOKING UPDATE PAGE** *bookings/booking_update_form.html* file
  ![image](https://github.com/user-attachments/assets/5a3b2c11-0da4-4f87-907d-382d4628a80f)  
  
- **BOKING DELETE PAGE** *bookings/booking_confirm_delete.html file
  ![image](https://github.com/user-attachments/assets/315825ce-bbd7-49a3-8624-6a38885428ce)
  
- **CONTACT PAGE** *contacts/contact.html* file
  ![image](https://github.com/user-attachments/assets/8fcd6012-e4c2-4e4f-9da7-57cff4ab9d2c)

- **ABOUT PAGE** *about/about.html* file
  ![image](https://github.com/user-attachments/assets/10a6543c-d151-4c99-8db8-e907ddb718d8)

- **ACCOUNT PAGES** *templates/account/** files have all same short config, so I have passed the following as validation proofs:
  ![image](https://github.com/user-attachments/assets/eaddd8f5-c689-42b0-b2c1-0c4896677d17)  
  ![image](https://github.com/user-attachments/assets/319b11ec-0408-42fb-8094-72ea51790109)  
  ![image](https://github.com/user-attachments/assets/4cc3d681-7479-4528-be8c-4ca4a11e3511)  
  



      
### CSS3
No CSS errors have been found uppon performing the CSS validator test provided by W3C - [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/):  

  ![image](https://github.com/user-attachments/assets/ff7de6d9-a19b-429e-b086-ad007e703c8f)


### JS ES6
The validation of the code has been successful. The validator used has been [JShint](https://jshint.com/). In order to remove inaccurate warnings related solely to the fact that it by itself does not support JS ES6, I [found the helpful and easy way](https://teamtreehouse.com/community/why-does-jshint-give-me-these-warnings-about-es6#:~:text=By%20default%2C%20JSHint%20gives%20you%20warnings%20if%20you%20use%20new%20ES6%20features) to make the tool read and analyse the ES6 code effectively, by simply adding this comment at the top of your file/code:  
```// jshint esversion: 6```  

- The following JS ES6 code is located at the bottom of the booking_form.html file inside django's {% block extras %}{% endblock %} 
  
  ![image](https://github.com/user-attachments/assets/ad88ca01-6230-460d-8893-9880253e87c6)

- The following JS ES6 code is located at the bottom of the world_details.html file inside django's {% block extras %}{% endblock %} 
  
  ![image](https://github.com/user-attachments/assets/ea6d26a8-dcfe-432f-a3e0-5dbb809bb885)


### PYTHON 3.12
Validation has been done using [CI Python Linter by Code Institute](https://pep8ci.herokuapp.com/), and the results have been the following:
- 

## DEFECT TRACKING

### GITHUB ISSUES
The defects or bugs that have appeared while programming this site have been tracked using **Github Issues** tool, and have been placed in the *bug* column of the *[project's kanban](https://github.com/users/Ethra8/projects/8/views/1)* to be easily tracked and fixed. Once fixed, they have been moved to the correspondent *FIxed Bug* column on the kanban.

### DEFECTS OF NOTE
No defects of note have been detected on the site.
  
### OUTSTANDING DEFECTS
No outstanding defects have been detected on the site.


## COMPATIBILITY AND RESPONSIVE TESTING  

### PRESELECTING TESTING TARGETS
- For a meaningful testing of the site, [Stat Counter](https://gs.statcounter.com) has been used, in order to get an insight of the following:
    
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
Following all the above information, compatibility and responsive testing has been done on the most common *browser versions*, *OS*, and *screen resolution* combinations, by using [Browser Stack](https://chrome.google.com/webstore/detail/browserstack/nkihdmlheodkdfojglpcjjmioefjahjb) Chrome extension, the *Chrome Dev tool's emulator*, and real devices. On the mobile reasl device, XRecorder app has been used. 

Please find the correspondent **compatibility and responsive testing** reflected in the following table:

| TEST no.| TOOL               | DEVICE               | BROWSER            | OS              | VIEWPORT width x height (px) |
|---------|--------------------|----------------------|--------------------|-----------------|------------------------------|
| [1](#test-1)        | Chrome Dev emulator| [Samsung Galaxy S8](https://blisk.io/devices/details/galaxy-s8)   | Chrome 117 |Windows 11  |360 x 740             | 
| [2](#test-2)        | BrowserStack       | [Samsung Galaxy S20](https://blisk.io/devices/details/galaxy-s20)   | Edge    |Android 11.0 |360 x 800           |
| [3](#test-3)        | BrowserStack       | Samsung Galaxy S22   | Edge               |Android 12.0     |360 x 780                     |
| [4](#test-4)        | BrowserStack       | iPhone 12 Mini       | Safari             | iOS 16.0        |360 x 780                     |
| [5](#test-5)        | BrowserStack       | [iPhone XS](https://blisk.io/devices/details/iphone-xs)| Safari   | iOS 15.0   |375 x 812            |
| [6](#test-6)        | REAL mobile device | Samsung Galaxy A22 5G| Chrome             | Android 13.0    |384 x 729                     |
| [7](#test-7)        | BrowserStack       | [Samsung Galaxy S22 Ultra](https://blisk.io/devices/details/galaxy-s22-ultra)| Chrome | Android 13.0  |384 x 824  |
| [8](#test-8)        | BrowserStack       | [iPhone 14](https://blisk.io/devices/details/iphone-14) | Safari 16.5  | iOS    |390 x 844                   |
| [9](#test-9)        | REAL Laptop Device | PC Notebook HP -15-bs013ns| Chrome 117    |Windows 10 -64bit|1366 x 768                    |
| [10](#test-10)       | Blisk              | MacBook Pro          | Chrome 117         | macOS           |1440 x 900                    |
| [11](#test-11)       | BrowserStack       | Asus ZenBook UX305   | Edge               |Windows 11       |1920 x 1080                   |
| [12](#test-12)       | BrowserStack       | Asus ZenBook UX305   | Firefox 117        |Windows 11       |1920 x 1080                   |
| [13](#test-13)       | BrowserStack       | MacBook              | Safari 16.5        | OS X Ventura    |1920 x 1080                   |


### TEST RESULT VIDEOS
#### TEST 1
  
  https://github.com/user-attachments/assets/d89bee18-7c29-42b7-9e46-d9610ef703b6


TEST 2
-

https://github.com/user-attachments/assets/974cfbd9-25ab-4338-8c72-54f99c63d793


TEST 3
-
TEST 4
-
TEST 5
-
TEST 6
-

https://github.com/user-attachments/assets/23fa1a68-13d4-40b8-8cca-e5cecfb7778a


TEST 7
-  

https://github.com/user-attachments/assets/94540408-fa29-4702-8653-f4cdb78a8500

  
TEST 8
-  

https://github.com/user-attachments/assets/aebd1c9b-e0bd-4dda-9b94-44b5e51c5645



TEST 9
-
TEST 10
-


## ACCESSIBILITY TESTING




## MANUAL TESTING
### ACCOUNT & USER AUTHENTICATION
- [X] Registration
   ![image](https://github.com/user-attachments/assets/e667753e-910d-4898-8048-32c0931e3d3b)
   
- [X] Email Verification:  
   ![image](https://github.com/user-attachments/assets/1d255a5c-0c4e-4cf8-8f86-f42fb356dd02)  
   ![image](https://github.com/user-attachments/assets/f08d45c8-7edd-479e-ab98-d3a82baa18c5)  
   ![image](https://github.com/user-attachments/assets/a902a04c-7cc6-4136-a39a-fb2c5012bef7)

- [X] Login
- [X] Logout
- [X] Password Recovery - Email with link to recover password received successfully:  
   ![image](https://github.com/user-attachments/assets/ea59ec54-85e0-4f44-832a-dc058a3d7030)  
   ![image](https://github.com/user-attachments/assets/8f664589-241b-4fab-9c4a-7796e95932f2)
- [X] All accounts' email addresses are stored separately, and can be manually verified by the admin, if needed. Also very useful for emailing campaigns:
      ![image](https://github.com/user-attachments/assets/e6e2c976-0902-47e8-b36c-499e5fe79219)

- [X] Site owner can create different *groups* from the admin to give different types of permissions to the users in that group:
      ![image](https://github.com/user-attachments/assets/afd57894-1f22-4c90-a120-b0179802a0e0)


  
### BOOKINGS
- [X] **C**reate booking
- [X] **R**ead or view booking from *My Bookings* link on the navbar's user icon's dropdown menu
- [X] **U**pdate booking - Change date, time, or world, checking for availability
- [X] **D**elete booking uppon confirmation of deletion
- [X] Users bookings are **secured**, and can only be accessed once logged into the same account, as bookings are linked to a particular user:  
      1. View bookings page from my user: ![image](https://github.com/user-attachments/assets/de284b96-ad0a-4df7-8f51-3122020aefe2)  
      2. When copying the url, and trying to access while being logged out, site demands to be logged in:
        ![image](https://github.com/user-attachments/assets/4668e9f0-70e7-4159-8e66-0d381fc4760f)

- [X] When the user accesses the booking form from a specific world's details page, the *world dropdown* on the form is preselected.

### CONTACT FORM
- [X] If user is authenticated, the **email field is prepopulated** with the user email:
      ![image](https://github.com/user-attachments/assets/7c760770-7151-4863-aec5-a22e3c349859)  
            
- [X] Site owner can **keep track of user requests sent via the contact form**. All content is stored in the admin panel, for further review by the site owner, and confirmation message appears to user. The site owner can check the *'read'* checkbox once the request has been read:
      ![image](https://github.com/user-attachments/assets/d68cb6bb-6998-4a8f-a3f7-75bade24e339)
      ![image](https://github.com/user-attachments/assets/30744eb2-01ef-4112-b536-f4c9c89e5ba2)
      ![image](https://github.com/user-attachments/assets/0e9acab6-8a03-48b6-ae41-fd718e3f840d)
      ![image](https://github.com/user-attachments/assets/ed826552-bc68-42f3-8376-e26bee5a58f9)
      ![image](https://github.com/user-attachments/assets/e3d90107-a340-4e27-a20d-5fb96c043b9b)
      
### ABOUT
- [X] Site owner can manually edit the content of the about page, including the text and the section image, being also able to style the text via the *Summernote editor*. Many *abouts* configurations can be stored, which could be useful for seasonal customization:
      ![image](https://github.com/user-attachments/assets/4842b75d-cbac-4a92-b8d3-b2eadceada07)
      ![image](https://github.com/user-attachments/assets/952e65ac-42b0-473a-a364-457d610481ce)


      



      




  
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
1. Ensure that in your **settings.py**, ```DEBUG = False``` before doing the last commit to Github before deploying to Heroku.
2. **On Heroku**, click the **deploy** tab on the top navigation bar.
3. Scroll down and select Github as 'Deployment method'
4. Use the github link and type in the name of your repository
   ![image](https://github.com/user-attachments/assets/ea9b0af6-b0ad-4bcb-9b2c-842e2fa738db)

5. Scroll down, to **'Manual Deploy'** configuration and select ***main*** on the dropdown for the ***branch the deploy***
6. Then click on **deploy from branch**
   ![image](https://github.com/user-attachments/assets/4b1a00cd-9f53-4540-a5cb-316c150b6578)
7. Once the app is loaded, click on the 'View' button that appears only then.
8. Once your application is running, you can switch to **Automatic Deploys** so that any changes in the repositori are automatically reflected in Heroku deployed app.  
  
  
# CREDITS & ACKNOWEDGEMENTS

## IMAGES
- [Hero image](https://www.freepik.com/free-photo/enchanting-glow-fairy-lights-candles-creating-magical-ambiance_136714970.htm) by [
frimufilms](https://www.freepik.com/author/frimufilms) at [Freepik](https://www.freepik.com/)
 
**NB:** All other images on the site have been generated with AI using *ChatGPT* exclusively for this site by the author, and can be accessed by clicking on each. 

## ACKNOWLEDGEMENTS
- Sites thoroughly researched: [Stackoverflow](https://stackoverflow.com/), [Django Projects Forum](https://forum.djangoproject.com/).
- [rusingh *Ru*'s Blog](https://rusingh.com/)
- [Open Source](https://opensource.com) for their article on [smtp](https://opensource.com/article/22/12/django-send-emails-smtp).
- [Team Tree House](https://teamtreehouse.com/) for their forum. It helped me [validate JS ES6](#JS-ES6) code on [JShint](https://jshint.com/) properly to ignore warnings related to JS ES6 that the tool os not supporting by default. Check discussion [here](https://teamtreehouse.com/community/why-does-jshint-give-me-these-warnings-about-es6)
  

