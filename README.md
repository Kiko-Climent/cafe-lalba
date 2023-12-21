# CAFETERIA L'ALBA
![Cafeteria l'Alba]()
Portfolio 4 project as part of the Diploma in Full Stack Software Development by Code Institute.
___

Open for almost three decades, **Cafeteria l'Alba** restaurant in *Alicante* (Valencia / Spain) has been the heart of our family, where my siblings, cousins, aunts, and uncles have grown up and had the opportunity to work and learn all there is to know about the hospitality business.

The restaurant opened its doors in 1986, thanks to my mother, *Pepa Garcia*, and my aunt, *Rosa Garcia*, following a family tradition dating back to the 1960s when my grandfather, *José García*, opened the precursor business, *'El Casino'*, located in a small town in the province of Alicante called Sella, our hometown.

Today, my brother, *Jose Climent*, manages the restaurant, offering customers a wide variety of typical specialties from Alicante's gastronomy, focusing mainly on the preparation of traditional stews and rice dishes typical of the inland of the Alicante province.

Due to the deep family roots connecting me to this establishment, working on this project has held a very special significance for me.

Link to live site - []

___

## Site Objectives

The main goal behind creating this webpage is to put into practice all the frameworks and libraries we've learned throughout the Code Institute course. This has enabled me to develop a website for my brother's restaurant. I've incorporated an online table reservation system as well as a functionality that allows customers to get in touch with the administrator.

Through this, I aim to showcase my skills while assisting my brother with his business, particularly concerning table organization.

Regarding **web development**, the most important thing has been:

- ### Create a readable and clean frontend page

The site is 100% responsive with all kind of devices, having a friendly and intuitive navigation.

- ### Make use of backend functionality

The use of the backend framework allows users to get in touch with the administrator, create a user account and book a table if they wish, being this last functionality able to read, update and delete.

- ### Store data on an external cloud database

I used ElephantSQL to store the PostgreSQL database for this project.

___

# User Experience / UX

## Target Audience

The target audience is composed of users who are lovers of traditional food or those who wish to discover the incredible delicacies offered by Alicante's gastronomy.

## User Stories

## New Visitor Goals

- **Explore the menu**: New visitors might want to browse through the wide range of lesser-known dishes offered by the restaurant.
- **Register an Account**: Visitors interested in making reservations may want to create an account to access the online reservation system.
- **Contact the Administrator**: Those with specific inquiries or needing more information might wish to reach out to the restaurant via the contact form.
- **Discover underrated dishes**: Informing customers and helping them explore traditional dishes from the inland region of Alicante province.
- **Discovering tradition**: Creating engagement through a family business that has been passed down from generation to generation, tradition as a fundamental pillar of the company

## Existing Visitor Goals

- **Make a Reservation**: Returning visitors who've registered an account might aim to use the reservation system to book a table.
- **Explore New Dishes**: Return to explore specials or try out new items added to the menu.
- **Contact the Administrator**: In case of issues or additional questions, existing visitors may choose to contact the restaurant again through the contact form.
- **Update Existing Booking**: Visitors with an existing account might want to update a future booking, either by updating number of people, time or date; or by removing the booking"
___

# Design

## Colour Scheme
The Colour Scheme implemented on this project was implemented after having a brainstorming with the owner of the restaurant, my brother _Pepe Climent_, he wanted to have something sober in order the user could focus more on the info and pictures displayed on the page.

## Typgography
The font used on the page is *Inconsolata*. After conducting thorough research among many of the fonts provided by Google Fonts, we found that _Inconsolata_ was the one that best matched the physical menu that customers can find at the restaurant.

## Logo
The logo used in the header has been sourced from _Font Awesome_. Both my brother and I believe that a classic pot perfectly symbolizes the restaurant's principles. It represents traditional food meant to be enjoyed with a spoon, as the restaurant specializes in stews and rice dishes.

## Wireframes

## Flow Diagram

## Database Plan

___

# Features

## Registration:
The user can create an account:
[]

## Book a table:
Once the account has been created, the user is alowed to place a booking.
[]

## Update Booking:
If the user whishes, the booking could be update it.
[]

## Delete Booking:
Of ocurse the possibity of removing the booking is also allowed.
[]

## My Bookings:
A detailed list of past and future bookings from the user is also possible to visit under "My Reservations"
[]

## Log in / Log out:
The user is allowed to log into his account in order to make use of the functionalities of the restaurant, *Create a New Booking, Update it or Delete it*
[]

## Contact Form:
Both _New_ and _Existing_ users can contact the administrator for inquiries without the need for user validation to access this feature.
[]

## Admin Panel:
The page administrator can access the _Admin Panel_ by entering their credentials. Within this panel, he will find a comprehensive dashboard displaying _Information_ from Users, _Bookings_, and _Messages_.
[]

## Future Features:
- Add a _*users profile page*_ where stored data can be edited.
- Add a _*reviews section*_, where new and existing users can leave feedack and rate dishes, service, etc..
- Add the functionality of _*online orders*_, where users can _place_ and _pick up_ their food orders.
- Implement a plan of the restaurant so users can select an specific table.
- Implement a system that notificates the user with an e-mail about new-reservations, updates, etc..

## Features Not Included

# Technologies Used
The following technologies were used in order to develope and create this project:

- Gitpod:
- Github:
- Heroku:
- Cloudinary:
- 


# Tests

## Manual Testing:

### USER:

- **Sign Up**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Username Field | Field should accept only valid characters | Entered a username with letters, numbers, and @/./+/-/_ | Pass | Pass |
Username Field | Field should accept only valid characters | Entered a username with '#' character | Fail | Pass |
Username Field | Field should not allow spaces in the username | Entered a username without spaces | Pass | Pass |
Username Field | Field should not allow spaces in the username | Entered a username with spaces | Fail | Pass |
Email Field | Should only accept a valid email format | Entered a valid email with '@' | Pass | Pass |
Email Field | Should only accept a valid email format | Entered a invalid email without '@' | Fail | Pass |
Email Field | Should only accept a valid email format | Entered blank field | Fail | Pass |
First Name Field | Field should be filled up | Entered blank field | Fail | Pass |
First Name Field | Field should be filled up | Entered name | Pass | Pass |
First Name Field | Field should be filled up | Entered characters like '@''#' | Pass | Pass |
Last Name Field | Field should be filled up | Entered blank field | Fail | Pass |
Last Name Field | Field should be filled up | Entered blank name | Pass | Pass |
Last Name Field | Field should be filled up | Entered characters like '@''#' | Pass | Pass |
Password Field | Should accept a combination of letters and numbers | Entered less than 8 characters | Fail | Pass |
Password Field | Should accept a combination of letters and numbers | Entered only numbers | Fail | Pass |
Password Field | Should accept a combination of letters and numbers | Entered only letters | Fail | Pass |
Password Field | Should accept a combination of letters and numbers | Entered letters and numbers | Pass | Pass |
Password (again) Field | Should match the original password field | Entered matching field | Pass | Pass |
Password (again) Field | Should match the original password field | Entered non matching field | Fail | Pass |
Sign-up submision | Upon successful entry, user should be registered | Completed the form and clicked 'Sign Up' button | Pass | Pass |
Sign-up submision | Upon successful entry, user should be registered | Filled up form with existing data from other user | Fail | Pass |

- **Sign In**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Username Field | Field should accept only registered users | Entered non existing user | Fail | Pass |
Username Field | Field should accept only registered users | Entered existing user | Pass | Pass |
Password Field | Field should accept only valid passwords | Entered invalid password | Fail | Pass |
Password Field | Field should accept only valid passwords | Entered valid password | Pass | Pass |
Sign-in submision | Upon successful entry, user should be loged in | Completed the form and clicked 'Sign In' button | Pass | Pass |

- **Log out**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Log out submission | Finish session | Open log out in navbar menu and click "Log-out" | Pass | Pass |


- **Contact**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Name | Should accept any kind of letters, numbers and characters if provided | Enter a valid name | Pass | Pass |
Subject | Should accept any kind of letters, numbers and characters | Enter valid subject | Pass | Pass |
Subject | Should accept any kind of letters, numbers and characters | Enter blank field | Fail | Pass |
Subject | Should accept any kind of letters, numbers and characters | Enter blank field 'spacing'| Fail | Fail |
Email | Should accept a valid email format | Enter a valid email format | Pass | Pass |
Email | Should accept a valid email format | Enter an invalid email format (no '@') | Fail | Pass |
Email | Should accept a valid email format | Enter blank fiel | Fail | Pass |
Notes | Should allow entering additional information | Enter text in the notes field | Pass | Pass |
Notes | Should allow entering additional information | Enter blank fiel | Fail | Pass |

- **Reservations / Create a booking**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Name | Should accept valid letters | Enter a valid name | Pass | Pass |
Name | Should accept valid letters | Enter blank field | Fail | Pass |
Name | Should accept valid letters | Enter just characters | Pass | Fail |
Name | Should accept valid letters | Enter name and characters | Pass | Fail |
Number of People | Should allow a maximum of 4 people | Enter 1, 2, 3 and 4 | Pass | Pass |
Number of People | Should allow a maximum of 4 people | Not possible to enter more than 4 and less than 1 | Pass | Pass |
Start Time | Should only allow selection from available times (18:00, 19:00, 20:00, 21:00) | Choose one of the available options | Pass | Pass |
Start Time | Should only allow selection from available times (18:00, 19:00, 20:00, 21:00) | Not Possible to chose a different time | Pass | Pass |
Start Time | Shouldn't allow selection from available times in case fully booked | Choose one of the available options | Pass | Pass |
Date | Should only allow future dates | Select a future date | Pass | Pass |
Date | Should only allow future dates | Select present day | Fail | Pass |
Date | Should only allow future dates | Select a past date | Fail | Pass |
Phone (NOT REQUIRED) | Should accept valid phone numbers | Enter numbers | Pass | Pass |
Phone (NOT REQUIRED) | Should accept valid phone numbers | Enter letters | Pass | Fail |
Phone (NOT REQUIRED) | Should accept valid phone numbers | Enter blank field | Pass | Pass |
Email | Should accept a valid email format | Enter a valid email format | Pass | Pass |
Email | Should accept a valid email format | Enter an invalid email format (no '@') | Fail | Pass |
Email | Should accept a valid email format | Enter blank fiel | Fail | Pass |
Notes (NOT REQUIRED) | Should allow entering additional information | Enter text in the notes field | Pass | Pass |
Notes (NOT REQUIRED) | Should allow entering additional information | Enter blank fiel | Fail | Pass |
Booking submision | Upon successful entry, user should book a table | Completed the form and clicked 'Submit' button | Pass | Pass |

- **Reservations / Reservations List**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Update booking | Should allow user to open "Update Booking Page" | Open "Reservation List page" after click in "My Reservations" and click "Update Booking" | Pass | Pass |
Delete booking | Should allow user to open "Delete Booking Page" | Open "Reservation List page" after click in "My Reservations" and click "Delete Booking" | Pass | Pass |

- **Reservations / Update Booking**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Start Time | Should only allow selection from available times (18:00, 19:00, 20:00, 21:00) | Choose one of the available options | Pass | Pass |
Start Time | Should only allow selection from available times (18:00, 19:00, 20:00, 21:00) | Not Possible to chose a different time | Pass | Pass |
Start Time | Shouldn't allow selection from available times in case fully booked | Choose one of the available options | Pass | Pass |
Date | Should only allow future dates | Select a future date | Pass | Pass |
Date | Should only allow future dates | Select present day | Fail | Pass |
Date | Should only allow future dates | Cannot select a past date | Pass | Pass |
Number of People | Should allow a maximum of 4 people | Enter 1, 2, 3 and 4 | Pass | Pass |
Number of People | Should allow a maximum of 4 people | Not possible to enter more than 4 and less than 1 | Pass | Pass |
Booking update submission | Upon successful entry, user should update the previous booking | Completed the form and clicked 'Submit' button | Pass | Pass |

- **Reservations / Delete Booking**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Booking delete submission | Confirm Delete | Open delete booking page in My Reservations and click on "Confirm Delete" | Pass | Pass |




















