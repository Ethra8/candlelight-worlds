# CANDLELIGHT WORLDS

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
-  [TESTING](#testing)
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
-[CREDITS & ACKNOWEDGEMENTS](#credits-and-acknowledgements)


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
- [X] Sign up for an account after a conscient decision, to be able to make a booking.
- [ ] Check the About page 

### As a first time B2B visitor
- [ ] Easily acces a contact form to receive the special catalogue for company events.  
- [ ] View some pictures of past events as example of activities.  

### As an Authorized User 
- [X] Easily log in and log out.  
- [X] Easily recover my password in case I forget it.
- [X] Receive an email to confirm my registration, so that I can be sure of my credentials.
- [X] View a confirmation message after registering.  

### As an Authorized Customer
- [X] Fill up a form to make a booking.  
- [X] Add desired world to my booking.  
- [X] View my booking after sending the booking form.
- [X] Update or delete my booking/s.  
- [X] View confirmation message on the site for every action taken.  

## SITE OWNER STORIES
As a site owner, the following functionalities have been included on this site, to manually access and set the following:
- [X] Add, update or delete worlds directly from the Admin.  
- [X] Style the font size and display of each world's details page.
- [X] Add, update of delete images from the world's details page.


## USER PROFILES

### B2C
- Steve is a romantic man in his thirties and wants to surprise his partner with a very special gift for a special occasion
- Siham is looking for a special gift for her parents' anniversary
- Wendy and Peter want to celebrate their 25th anniversary and build more special memories together. 

### B2B
- Oisin is the CEO of a large company and wants to offer a special treat to the managers after reaching an importnt milestone.
- Maeve is the owner of a family-owned establishment and wants a special 1st price for a raffle.
- Tony is in charge of finding an out-of-the-box approach to organize a team building activity for the executives of his company.


## WIREFRAMES

MOBILE & TABLET (Portrait) WIREFRAMES:
-
<details>
<summary>Click here to see the Mobile & Tablet (portrait) Wireframes</summary>
- HOME PAGE
  
  ![image](https://github.com/user-attachments/assets/4cb95fc6-fadb-4fd1-ac16-79e3b3c8abe7)  
   
- Worlds Page
  - 
- Booking Page
  - 
- About Page
  - 
</details>  

  
DESTOP & TABLET (Landscape) WIREFRAMES:
-
<details>
<summary>Click here to see the Desktop & Tablet (landscape) Wireframes</summary>
- Home Page

  ![image](https://github.com/user-attachments/assets/0874770d-4670-4e5d-8a17-eccfcaf2c2a4)  
- Worlds Page
  ![image](https://github.com/user-attachments/assets/727dbaf0-40f8-4ba1-8646-0c9a865f6f1d)
  
- Booking Page
  - 
- About Page
  - 
</details>


# AGILE METHODOLOGY
## GITHUB PROJECT - KANBAN
You can check the Kanban project that has been used on the development of this site [here](https://github.com/users/Ethra8/projects/8)


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
 

## CREDITS & ACKNOWEDGEMENTS

### IMAGES
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

