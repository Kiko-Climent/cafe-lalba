# CAFETERIA L'ALBA
![Cafeteria l'Alba](/media/mockups.png)
Portfolio 4 project as part of the Diploma in Full Stack Software Development by Code Institute.
___

Open for almost three decades, **Cafeteria l'Alba** restaurant in *Alicante* (Valencia / Spain) has been the heart of our family, where my siblings, cousins, aunts, and uncles have grown up and had the opportunity to work and learn all there is to know about the hospitality business.

The restaurant opened its doors in 1986, thanks to my mother, *Pepa Garcia*, and my aunt, *Rosa Garcia*, following a family tradition dating back to the 1960s when my grandfather, *José García*, opened the precursor business, *'El Casino'*, located in a small town in the province of Alicante called Sella, our hometown.

Today, my brother, *Jose Climent*, manages the restaurant, offering customers a wide variety of typical specialties from Alicante's gastronomy, focusing mainly on the preparation of traditional stews and rice dishes typical of the inland of the Alicante province.

Due to the deep family roots connecting me to this establishment, working on this project has held a very special significance for me.

Link to live site - [https://cafe-lalba-08ae328c9609.herokuapp.com/]

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
The Colour Scheme used in this project was chosen after having a brainstorming with the owner of the restaurant, my brother _Pepe Climent_, he wanted to have something sober in order the user could focus more on the info and pictures displayed on the page.

## Typography
The font used on the page is *Inconsolata*. After conducting thorough research among many of the fonts provided by Google Fonts, we found that _Inconsolata_ was the one that best matched the physical menu that customers can find at the restaurant.
![Typography](/media/Typography.png)

## Logo
The logo used in the header has been sourced from _Flaticon_. Both my brother and I believe that a classic pot perfectly symbolizes the restaurant's principles. It represents traditional food meant to be enjoyed with a spoon, as the restaurant specializes in stews and rice dishes.
![Logo](/media/logo.png)

## Wireframes

## Flow Diagram
Here can be found the 2 diagrams showing the possible flow from both, _User_ and _Admin_
![User Diagram](/media/user_diagram.jpeg) ![Admin Diagram](/media/admin_diagram.jpeg)

## Database Plan
Concerning the _Database Plan_ this is very straighforward,using a _Foreign Key_ to link data from user...
![Data Base Plan](/media/data_base_plan.png)

___

# Features

## Home Page:
The first place users land, the main page or _Landing Page_, already features a _call-to-action_ where users have the option to directly navigate to the _Reservations page_, the website's primary functionality.
![Home Page](/media/home.png)

## Navegation:
The _Navigation bar_ displays all the options that can be selected by the user. In addition to the previously mentioned reservation functionality, the user can access the restaurant _Menu_, a _Contact form_, and of course, the section to input their _Credentials_. An _About_ section is also available, along with a brief quote showcasing the year the restaurant was inaugurated. Also once the user has been _logged in_, an _Alert_ triggers informing the user and a _Log in panel_ shows in the navbar.
![Navbar](/media/navbar.png) ![Navbar2](/media/navbar_logged.png) ![Navbar_small](/media/navbar_small.png) ![Navbar_small2](/media/navbar_small_alert.png)

## About:
The _About_ section introduces the user to the principles and foundations of the restaurant.
![About](/media/about2.png) ![About_small](/media/about.png)

## Menu: 
Concerning the _Menu_ section, the user can have access to the treats that the restaurant offers. Along with it, a _Pictures Carousel_ with some of the dishes is diplayed at the bottom.
![Menu](/media/menu.png) ![Carousel](/media/carousel.png)

## Registration:
The user will need to _Sign Up_ if he wants to have access to the _Reservation_ functionality
![Sign_up](/media/sign_up.png)

## Book a table:
Once the account has been created, the user is alowed to place a booking.
![New_Booking](/media/new_booking.png)

A _Modal_ has been introduced in order to inform the user about the reservation rules:
![Reservation_Rules](/media/modal.png)

If the data introduced is correct a confirmation message with the booking details displays on the screen
![Reservation_Details](/media/reservation_details.png)

In case of wrong data introduced such as, date in the past, or restaurant fully booked for the selected hour, an _alert_ triggers informing the user
![Wrong_data](/media/wrong_data_booking.png)

## My Bookings / Reservation List:
Users registered can have access to all the bookings made, 2 buttong displays in the list, having the possibility of _Update_ or _Delete_ an existing booking.
![Reservations_List](/media/reservations_list.png)

## Update Booking:
If the user whishes, the booking could be update it.
![Update_Booking](/media/update_booking.png)

An _alert_ will be shown in the _reservations list section_ in case of a succesfull booking.
![Update_success](/media/update_succesful.png)

In the other hand, if the data introduced for the update s wrong, the user will be informed,forcing him to introduce new data for the update
![Update_wrong](/media/update_wrong.png)

## Delete Booking:
Of ocurse the possibity of removing the booking is also allowed.
![Delete_Booking](/media/delete_booking.png.png)

Once deleted, the user will be informed in the reservation list.
![Successful_Delete](/media/successful_delete.png)

## Log in:
The user is allowed to log into his account in order to make use of the functionalities of the restaurant, *Create a New Booking, Update it or Delete it*
![Sign_in](/media/sign_in.png)

## Log out:
Here the booking can finish his session.
![Sign_Out](/media/sign_out.png)

## Contact Section:
Both _New_ and _Existing_ users can contact the administrator for inquiries without the need for user validation to access this feature. Also, in order to help the user with the  restaurant _Location_, a map with the address is implemented, along with the _Openning Times_
![Contact](/media/contact_form.png) ![Location](/media/contact_location.png)

Once the message has been sent, an alert triggers giving the possibility of being redirected to _Home_ page.
![Message_Sent](/media/message_succefully.png)

## Admin Panel:
The page administrator can access the _Admin Panel_ by entering their credentials. Within this panel, he will find a comprehensive dashboard displaying _Information_ from Users,_Email Addresses_, _Bookings_, and _Messages_.

![Admin_Panel](/media/admin_panel.png)
![Admin_Users](/media/admin_users.png)
![Admin_Emails](/media/admin_email.png)
![Admin_Messages](/media/admin_messages.png)
![Admin_Bookings](/media/admin_bookings.png)

## 404 Error Message:
A custom _404_ error message was also implemented on this project
![404](/media/404.png)

## Future Features:
- Add a _*users profile page*_ where stored data can be edited.
- Add a _*reviews section*_, where new and existing users can leave feedack and rate dishes, service, etc..
- Add the functionality of _*online orders*_, where users can _place_ and _pick up_ their food orders.
- Implement a plan of the restaurant so users can select an specific table.
- Implement a system that notificates the user with an e-mail about new-reservations, updates, etc..

___

# Technologies Used

- [Gitpod](https://www.gitpod.io/) To create and develope this project.
- [Github](https://github.com/) To store and host the data for the site.
- [Heroku](https://id.heroku.com/) To deploy the project.
- [Cloudinary](https://cloudinary.com/) To storage some images used in the project
- [ElephandSQL](https://www.elephantsql.com/) Used to store PostgreSQL database. 

# Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

___

# Agile

An _Agile_ metodology was implemented in order to develope this project. _Project Board_ and _Issues_ in *GitHub* were used.

- [Project Board](https://github.com/users/Kiko-Climent/projects/6/views/1)

The following *User Stories* were followed to develope the whole site.

- *User Registration*

As a Site User i can Register so that i can book a table, order food and be updated with new adds on the menu

| Acceptance Criteria | Tasks |
| --- | --- |
Users should be able to create a new account by providing at least username, and password. | Create the user interface for the registration form.
User account information (name, email, password) should be securely stored in the database.| Develop a secure storage system for account information.
The registration process should be intuitive and provide appropriate feedback for errors or success. | Establish the login flow after successful registration.
After successful registration, users should be able to log in using the newly created credentials. | Create feedback messages for different states of the registration process (success, errors, etc.).

- *Contact*

As a Site User i can Contact the restaurant so that i can be in touch with them

| Acceptance Criteria | Tasks |
| --- | --- |
There should be a contact form accessible to all users on the restaurant's website. | Create the user interface for the contact form with fields for name, email, subject, and message.
Form submission should validate required fields and display appropriate error messages for any missing or incorrectly formatted information. | Develop validation logic for the contact form fields to ensure required information is provided and in the correct format.
Submission of the form should trigger the contact message to the restaurant. | Create a confirmation message to be displayed to users upon successful form submission, indicating that their message has been sent.
After successful submission, users should receive a confirmation message indicating that their message has been sent to the restaurant. | Incorporate the contact form into the website, making sure it is prominently placed and easily accessible for site users.

- *Reservations:*

As a Site User i can book a table so that i have no problems of space when i visit the restaurant

| Acceptance Criteria | Tasks |
| --- | --- |
Users can select date, time, and number of guests for a reservation. | Develop backend logic to check and confirm availability based on selected date, time, and capacity.
Users receive immediate feedback on successful/unsuccessful booking attempts. | Implement a cancellation feature with appropriate validation.
The system must confirm booking availability based on selected date and time. | Design and implement a user-friendly interface for creating bookings.
Users can leave additional notes | --- |

- *Booking Confirmation*

As a Site User i can get a Confirmation so that im sure that my request has been received

| Acceptance Criteria | Tasks |
| --- | --- |
Users receive an immediate confirmation message or email upon successful booking. | Implement a notification system to immediately confirm successful bookings.
Include reservation details in the confirmation communication (date, time, number of guests). | --- |

- *Update/Cancel Booking:*

As a Site User i can update my bookings so that i can change the info i sent previously in case of an unexpected issue, or cancel an existing booking.

| Acceptance Criteria | Tasks |
| --- | --- |
Users can modify details of an existing reservation (date, time, number of guests). | Develop an interface allowing users to modify their existing reservations.
Changes should reflect in the system immediately upon confirmation. | Implement backend logic to handle changes in reservation details.
Users receive a confirmation notification or email after successfully updating a booking. | Ensure real-time synchronization of updated information in the system.
Users can delete an existing booking. | Alert the user confirming successful updates to bookings.

- *Restaurant Menu:*

As a Site User i can see the Menu so that i know what kind of food the restaurant hast to offer

| Acceptance Criteria | Tasks |
| --- | --- |
Upon visiting the restaurant's website or app, the menu should be easily accessible from the main navigation. | Design an intuitive and visually appealing menu layout.
Each menu item should have a name, description, and price listed. | Enter all menu items with their respective names, descriptions, and prices into the system.
Ensure the menu is readable and accessible across various devices (desktop, mobile, tablet). | Incorporate images or icons for menu items where appropriate and visually enriching.

- *Location & Opening Times:*

As a Site User, I want to view the location of the restaurant and its opening times so that I can plan my visit accordingly.

| Acceptance Criteria | Tasks |
| --- | --- |
Users should be able to access a page displaying the restaurant's location on a map. | Develop a section that shows the opening hours for each day of the week in a clear and organized format.
The map should provide clear directions to the restaurant's physical address. | Implement an API or iframe to embed an interactive map showing the restaurant's address and provide navigational support
The opening times for each day of the week should be visible and easily understandable. | --- |

- *Style:*

As a Site User i can have an atractive style on the page so that i can have a great user experience

| Acceptance Criteria | Tasks |
| --- | --- |
The page should have an aesthetically pleasing design with visually appealing elements (colors, fonts, layouts, etc.). | Develop a style guide that defines the chosen aesthetics, including color palettes, typography, iconography, and UI components.
It should reflect a consistent and coherent visual style across all sections of the page. | Implement the chosen style across the user interface, applying design elements to various sections of the page.
The style should be responsive, ensuring a good user experience across various devices. | Ensure responsiveness by testing the style on different devices and screens, making adjustments as needed to optimize the user experience.
The chosen style should enhance usability, making navigation intuitive and content easily readable. | Review the style to ensure it meets accessibility standards, making adjustments for better accessibility if required.

- *Data from User:*

As a Site Admin i can see contact details so that i can send them a message in case of any issue

| Acceptance Criteria | Tasks |
| --- | --- |
The admin panel should display a section specifically dedicated to viewing user contact details. | Create a dedicated section in the admin dashboard to display user contact details.
Contact details should include at least the user's name, email, and optionally a phone number if provided during registration. | Develop functionality allowing Site Admins to search and filter contact details based on various parameters like name, date range, or user type.

- *Number of Reservations:*

As a Site Admin i can see the number of bookings so that i can do a better organization

| Acceptance Criteria | Tasks |
| --- | --- |
The admin dashboard displays an overview of reservations | Implement restrictions to prevent overbooking or exceedance of set limits.
Reservation numbers update in real-time on the admin dashboard as users make bookings or cancel reservations. | Implement a robust data backup system to ensure reservation records are secure

- *Read messages from Users:*

As a Site Admin  i can read messages from guests so that i'm in touch in case of any issue.

| Acceptance Criteria | Tasks |
| --- | --- |

Messages are timestamped, displaying the date and time they were sent. | Add a section in the admin dashboard to display received messages.
The interface provides options to mark messages as read/unread | Implement timestamp functionality for messages to display the date and time they were sent or received.
Each message contains necessary details such as at least, email/contact, subject and message content. | Ensure the admin message interface is responsive and accessible across various devices (desktop, mobile, tablet).

___

# Tests

## Validation Testings

### HTML & CSS

- HTML: No errors were found after passing through the official [W3 Validator](/media/w3_validator.png)

- CSS: Found this warning when passing the code through the [Jigsaw W3 Validator/Warning](/media/jigsaw_warning.png)
in order to fix that, just changed the code to this [CSS fixed](/media/fixed_jigsaw.png)

After thos changes no errors were found in the [Jogsaw W3 Validator](/media/jigsaw.png)

### Python

The only errors recieved here were where some lines of text exceeded the limit of 79 characters, but these have now been rectified.

Python Files Tested:

- Views
- Forms
- Models
- Urls
- Admin
- Adapter





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
Notes (NOT REQUIRED) | Should allow entering additional information | Enter blank fiel | Pass | Pass |
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

___

### ADMIN:

- **Sign In**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Username Field | Field should accept only admin user | Entered admin user | Pass | Pass |
Username Field | Field should accept only admin user | Entered different user | Fail | Pass |
Password Field | Field should accept only valid passwords | Entered invalid password | Fail | Pass |
Password Field | Field should accept only valid passwords | Entered valid password | Pass | Pass |
Sign-in submision | Upon successful entry, admin should be loged in | Completed the form and clicked 'Sign In' button | Pass | Pass |

- **Log out**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Log out submission | Finish session | Click "log out" on top of panel admin | Pass | Pass |

- **Reservations / Add Booking**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Add Booking | Should redirect to add booking fields | Click on "Add Booking" | Pass | Pass |
Name | Should accept valid letters, numbres and chracters | Enter only letters | Pass | Pass |
Name | Should accept valid letters, numbres and chracters | Enter only numbers | Pass | Pass |
Name | Should accept valid letters, numbres and chracters | Enter numbers & letters | Pass | Pass |
Name | Should accept valid letters, numbres and chracters | Enter numbers & letters | Pass | Pass |
Name | Should accept valid letters, numbres and chracters | Enter only characters | Pass | Pass |
Name | Should accept valid letters, numbres and chracters | Enter numbers, letters & characters | Pass | Pass |
Name | Should accept valid letters, numbres and chracters | Enter spacing | Fail | Pass |
Name | Should accept valid letters, numbres and chracters | Enter blank field | Fail | Pass |
Number of People | Should allow a maximum of 4 people | Enter 1, 2, 3 and 4 | Pass | Pass |
Number of People | Should allow a maximum of 4 people | Enter blank field | Fail | Pass |
Number of People | Should allow a maximum of 4 people | Enter -1 | Pass | Fail |
Start Time | Should allow any time | Choose one of the available options in the restaurante rules | Pass | Pass |
Start Time | Should allow any time | Choose any time of the day | Pass | Pass |
Start Time | Shouldn't allow selection from available times in case fully booked | Choose one of the available options once is fully booked | Pass | Fail |
End Time | Shouldnt allow to write a frametime before start time | Choose frametime after starttime | Pass | Pass |
End Time | Shouldnt allow to write a frametime before start time | Choose frametime before starttime | Pass | Fail |
End Time | Shouldnt allow to write a frametime before start time | Choose frametime after starttime but before the 1 hour window stablished| Pass | Fail |
Date | Should only allow future dates | Select a future date | Pass | Pass |
Date | Should only allow present and future dates | Select present day | Pass | Pass |
Date | Should only allow future dates | Select a past date | Pass | Fail |
Phone (NOT REQUIRED) | Should accept valid phone numbers | Enter numbers | Pass | Pass |
Phone (NOT REQUIRED) | Should accept valid phone numbers | Enter letters | Pass | Fail |
Phone (NOT REQUIRED) | Should accept valid phone numbers | Enter blank field | Pass | Pass |
Email | Should accept a valid email format | Enter a valid email format | Pass | Pass |
Email | Should accept a valid email format | Enter an invalid email format (no '@') | Fail | Pass |
Email | Should accept a valid email format | Enter blank fiel | Fail | Pass |
Notes (NOT REQUIRED) | Should allow entering additional information | Enter text in the notes field | Pass | Pass |
Notes (NOT REQUIRED) | Should allow entering additional information | Enter blank fiel | Pass | Pass |
User | Should allow to select a registered user | Select a registered user | Pass | Pass |
User | Should allow to select a registered user | Cannot Select an unregistered user | Pass | Pass |
Booking submision | Upon successful entry, admin should book a table | Completed the form and clicked 'Submit' button | Pass | Pass |

- **Reservations/ Bookings / Update Booking**

 _In the admin panel, booking section, click on one of the bookings. all the fields tested in the creation of a booking previously done, can be edited with same results._

- **Reservations / Bookings / Delete Booking**

 _In the admin panel, booking section, click on one of the bookings. on the bottom click on delete._

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Delete | Should delete the selected booking | click on "Yes, im sure! | Delete booking | Pass | Pass |
Cancel | Should take back to selected booking | click on "No, take me back" | Back to selected booking | Pass | Pass

- **Contact / Contact Messages**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Contact Messages | Should allow admin to view a list of messages | click "Contact Messages" | Pass | Pass |
Delete Messages | Should allow to delete a selected message from user | click on "Action/Delete" after selecting a message from user | Pass | Pass |

 _Should allow the admin to see the list of messages from users ordered by date and time, the result was a Pass_
 _Should allow the admin to see order the list of messages from users either by subject or email or responded, the result was a Pass_
 _Should allow the admin to filter the list of messages from users ordered by "responded", "not responded" or "all", the result was a Pass_

- **Authentication and Authoritation / Users**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
User Browser | Shold allow to search for an especific user | Search an existing user | Pass | Pass |
User Browser | Shold allow to search for an especific user | Search an unexisting user | Fail | Pass |
Delete User | Should allow to delete an existing user | Select a User and then "Action/Delete" | Pass | Pass |

 _Should allow the admin to see the list of registered users ordered by "Username", "Email"(if provided), "name" and "last name", the result was a Pass_

- **Account / Email Addresses**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Email Browser | Shold allow to search for an especific email from a user | Search by email | Pass | Pass |
Email Browser | Shold allow to search for an especific email from a user | Search by name | Pass | Pass |
Action "Delete email" | Should allow to delete an email from a user | Select an email then click on "Action/Deete" | Pass | Pass |
Action "Mark as verified" | Should allow to mark as verified an email from a user | Select an email then click on "Action/Mark as verified" | Pass | Pass |

 _Should allow the admin to see the list of emails from registered users ordered by "Username", "Primary" and "verified", the result was a Pass_
 _Should allow the admin to filter the list of messages from users by "Primary" and "verified" , the result was a Pass_

___

# Bugs

...
___

# Credits

"For the creation of this project, I relied on some of Code Institute's 'Walkthrough Projects' such as 'I think, therefore i blog,' 'The whiskey blog,' and 'ResumeProject.'

Official documentation from Django and Bootstrap has been crucial in implementing style on the website and coherence to the logic in views, models, and forms.

Other websites that have provided me with significant support include 'Serhalter.com,' 'django.allouth,' 'strip.com,' 'css-tricks.com,' 'devhandbook,' and 'GeekforGeeks.'

I made use of Artificial Intelligence for developing the logic of some functions.

The YouTube channel 'Fazt' was also helpful in better understanding how to implement 'CRUD' in my 'Reservations' app.

My great friend and programmer, 'Javier Fernandez,' also played a pivotal role in some of the functions of this project, helping me stay on the right track to complete this project.

In order to create the README file, i found inspiration in markdaniel1982 "My Fishing adventures"

Special mention to the tutors at Code Institute; without them, many of the elements present in my project wouldn't have been possible or would have taken me much longer to implement."

___

# Media

All the photos included in the carousel of the "MENU" section belong to dishes cooked by my brother, "Pepe Climent," at the restaurant that gives its name to this project, "Cafeteria l'Alba."

Due to the loss of many photos that my brother had stored on one of his computers, I was forced to collect photos from the internet to complete the project's content.

The photo of garlic, tomatoes, and mortar on the about page belongs to "Jaume Pinet."
The photo of our beloved town, "Sella," on the about page belongs to "Nacho Barco," extracted from his blog "Enamorados de Alicante."
The photo on the 404 page was rescued from the website "Barcelo.com."
The photo in the "callout" was taken from the page "Vacalia.com."
The photo on "My Reservations" was taken from the website of the restaurant "La Malvaroca."

















