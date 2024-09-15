# CANDLELIGHT WORLDS - RESTAURANT

## PROJECT OVERVIEW
**N.B.: This project is still under work, and has onyl reached CRU functionality, the Delete functionality has a bug on deadline, so I'm looking forward for the resubmission. Any constructive feedback would be much appreciated.**

- A booking site for a restaurant that offers out-of-the-box romantic dinners. This new concept involves private rooms carefully decorated to transport our guests to different times and places, all under immersive candlelight lighting.
- These romantic experiences not only include tasty dishes from around the globe served by our discreet and professional table service, but each private room also includes a lounge area with a king-size bed, so that couples can relax and chill after dinner, or even have a siesta!
- Guests also have the option to spend the night, if they wish so, by paying a supplement.

### LIVE SITE

### REPOSITORY

[Check Repository](https://github.com/Ethra8/candlelight-world)

### AUTHOR

Edna Torres Munill

# TABLE OF CONTENTS

- [Project Overview](#project-overview)
  * [Live Site](#live-site)
  * [Repository](#repository)
  * [Author](#author)
- [UX](#ux)
  * [Target Audience](#target-audience)
  * [Project Goals](#project-goal)
  * [User Stories](#user-stories)
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
    - [Email Booking Confirmaton](#email-booking-confirmation)
    - [Service Sorting](#service-sorting)
    - [Search Bar](#search-bar)
    - [404 Error Page](#404-error-page)
    - [Admin Console](#admin-console)
- [AGILE Methodology](#agile-methodology)
  * [Github Project - Kanban](#github-project-kanban)
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
  - Couples at any age wanting to build special memories
  - Extroverted and introverted personalities
  - Hight ticket sale
  - Anyone looking for the special gift like some built-in packs including special services during the stay

- **B2B:**
  * Companies that want to rent various spaces and services as a treat for their team
  * Companie that want something different as a team building activity
  * Companies that might want to offer their premium clients a spacial gift  
  
## PROJECT GOALSS
The project goals are as follows:
- 
  - The site aims at providing B2C customers with luxuriously themed private spaces where to have any meal of the day.
  - The site aims at providing B2B customers with luxuriously themed spaces for team building, or staff gathering.
  - All users can register for an account.
  - B2B users can send a contact form to receive customized offers on the type of service desired.
  - B2C services available can be stored in a shopping bag and bought online through Stripe API.
  - All users can subscribe to the monthly newsletter.

## USER STORIES
### As a B2C visitor 
1. [] Check all the spaces available.
2. [] Check all the services available for each space.
3. [] Sort all services and spaces both by cost, by alphabetical order, and by category
4. [] Sort a specific category
5. [] Search whithin the site for a specific word found in description or name of space or service
6. [] Sign up for an account after a conscient decision, to receive a discount on my first booking and a free treat on my birthday.
7. ### As a B2B visitor
8. [] Easily acces contact form to receive the special catalogue for companies.
9. [] View some pictures of past events as example of activities
10. ### As an Authorized User 
11. [] Easily log in and log out
12. [] Easily recover my password in case I forget it
13. [] Receive an email confirmation after registering
14. [] Personalized user profile to store my order and billing information
15. ### As a Shopper
16. [] View service detail pages
17. [] View spaces detail pages
18. [] Adjust quantity of services to add to my bag
19. [] View items in my bag to be purchased
20. [] Add items to my bag
21. [] Adjust quantity of individual items in my bag
22. [] Delete individual items in my bag
23. [] Easily enter payment information
24. [] Feel secure that my payment information is safe and secure 
25. [] View an order confirmation after checkout
26. [] Receive an email confirmation after checking out

## USER PROFILES
### B2C
- Steve is a romantic man in his thirties that works in an office and wants to surprise his partner with a very special gift for a special occasion
- Siham is looking for a special gift for her parents' aniverssary
- Wendy and Peter want to celebrate their love and build speacial memories together 
## B2B
- Oisin is the CEO of a large company and wants to offer a special treat to the managers after reaching an importnt milestone.
- Maeve is the owner of a family-owned establishment and wants a special 1st price for a raffle.
- Tony is in charge of finding an out-of-the-box approach to organize a team building activity for the executives of his company.




## WIREFRAMES
### MOBILE & TABLET (Portrait) WIREFRAMES
<details>
<summary>Click here to see the Mobile & Tablet (portrait) Wireframes</summary>
- Home Page  
  ![image](https://github.com/user-attachments/assets/4cb95fc6-fadb-4fd1-ac16-79e3b3c8abe7)  
- Worlds Page
  - 
- Booking Page
  - 
- About Page
  - 
</details>  
  
### DESTOP & TABLET (Landscape) WIREFRAMES
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
You can check the Kanban project that has been used on the development of this site [here](#https://github.com/users/Ethra8/projects/8)


## COMPATIBILITY AND RESPONSIVE TESTING

### PRESELECTING TESTING TARGETS
- To meaningful testing of site, [Stat Counter](https://gs.statcounter.com) has been used, in order to get an insight of the following:
    
    * **BROWSER MARKET SHARE** - Most commonly used browsers worldwide:

    ![image](https://github.com/Ethra8/history_beyond_myth/assets/80659091/77d7356e-35e0-4fbf-9d28-2e75215bb96b)

     * **BROWSER VERSION MARKET SHARE** - Most commonly used browser versions worldwide:

    ![image](https://github.com/Ethra8/history_beyond_myth/assets/80659091/2cf8b70e-99ba-46f0-bd41-a88fc75d0649)
    
    * **OS MARKET SHARE** - Most commonly used operation systems worldwide:

    ![image](https://github.com/Ethra8/history_beyond_myth/assets/80659091/9373a798-32b1-4e80-95e6-1406bcda0a37)

    * **MOBILE vs DESKTOP vs TABLET MARKET SHARE** - Most commonly used devices worldwide:

    ![image](https://github.com/Ethra8/history_beyond_myth/assets/80659091/57cabf42-8cee-4263-a6c5-ac1f9ac581f5)

    * **SCREEN RESOLUTION STATS** - Most common screen resolution (in pixels) worldwide:

    ![image](https://github.com/Ethra8/history_beyond_myth/assets/80659091/3b4fd7bf-c127-4323-a8d0-efb71b547417)


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
  - **Python 5.1**
  - **JS ES6**
  - **CSS3**
  - **HTML5**

## Frameworks, Libraries and Programs
  - **Django 3.12.2** framework
  - 
 

## CREDITS & ACKNOWEDGEMENTS

### IMAGES

- [Hero image](https://www.freepik.com/free-photo/couple-having-dinner-valentines-day_6412178.htm#query=dinner%20candlelight&position=32&from_view=keyword&track=ais&uuid=0b778147-a7c9-4ab5-a148-ddd91935661c) by [Freepik](https://www.freepik.com/author/freepik) at [Freepik](https://www.freepik.com/)
- [Medieval Castle Bedroom](https://in.pinterest.com/pin/823525481846848314/)
- [Medieval Castle Dinning Table](https://www.vecteezy.com/photo/24889510-candle-burning-on-table-illuminates-cozy-winter-atmosphere-indoors-generated-by-ai) by [Andrés Ramos](https://www.vecteezy.com/members/gstudioimagen) at https://www.vecteezy.com
- [Medieval Castle Jakuzzi](https://i.pinimg.com/564x/41/b3/1c/41b31cf7ca247ca845797d319ff2dca3.jpg) at [pinterest](https://cl.pinterest.com/pin/440156563579928642/?send=true)
- [Italian Renaissance Villa - Dinning Area](https://www.pinterest.es/pin/145100419219410839/) from [Homes of the Rich](https://homesoftherich.net/2008/11/italian-renaissance-villa-in-california/) at [Pinterest](https://www.pinterest.com)
- [Italian Renaissance Villa - Bedroom](https://homesoftherichest.wordpress.com/wp-content/uploads/2008/11/sanjuan9.jpg)
- [Dungeon Room](https://images.trvl-media.com/lodging/97000000/96670000/96662600/96662507/e042fa2a.jpg?impolicy=resizecrop&rw=1200&ra=fit) from [The Cove at Salem](https://uk.hotels.com/ho3094200224/the-cove-at-salem-salem-united-states-of-america/) at [uk.hotels.com](https://uk.hotels.com/ho3094200224/the-cove-at-salem-salem-united-states-of-america/)
