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

- **Sign In**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
Username Field | Field should accept only valid characters | Entered a username with letters, numbers, and @/./+/-/_ | Pass | Pass |
Username Field | Field should accept only valid characters | Entered a username with '#' character | Fail | Pass |
Username Field | Field should not allow spaces in the username | Entered a username without spaces | Pass | Pass |
Username Field | Field should not allow spaces in the username | Entered a username with spaces | Fail | Pass |
Email Field | Should only accept a valid email format | Entered a valid email with '@' | Pass | Pass |
Email Field | Should only accept a valid email format | Entered a invalid email without '@' | Fail | Pass |
Email Field | Should only accept a valid email format | Entered blank field | Fail | Pass |



