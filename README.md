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

Regarding web development, the most important thing has been:

- ### Create a readable and clean frontend page

The site is 100% responsive with all kind of devices, having a friendly and intuitive navigation.

- ### Make us of backend functionality

The use of the backend framework allows users to get in touch with the administrator, create a user account and book a table if they wish, being this last functionality able to read, update and delete.

- ### Store data on an external cloud database

I used ElephantSQL to store the PostgreSQL database for this project.

___

# User Experience / UX

## Target Audience

The target audience is composed of users who are lovers of traditional food or those who wish to discover the incredible delicacies offered by Alicante's gastronomy.

___

# Tests

## Manual Testing:

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
Booking update | Upon successful entry, user should update the previous booking | Completed the form and clicked 'Submit' button | Pass | Pass |













