# Smart Tech Repair

## Project Description

Smart Tech Repair is a small business specialized in repairs of phones, laptops, tablets, gaming, (smwart)watches and much more. The company aims to deliver fast and reliable service to its customers. The customers can either do an online booking or walk-in to the store during the opening hours. 

Online bookings: Customers lookup for information on the business profile of the company on Google and give a call to Smart Tech. On the phone they request for information such as the price and the availibility. The company needs information about the device and the issue. As this process goes all over the phone mistakes are likely to happen.

When the customer brings in the device, the device is tested (if the device is still in working condition). The customer leaves behind the device together with the password of the device for testing throughout the repair and the contact details. When the repair is done the technician calls the customer to say that the device is ready for collection.

## Scope
During this project the focus will be on the device type: phones. As these categories are the most common onces with the most repairing requests. Furthermore, the aim to solve the following issues:
1. Create a online booking system for the customer so that the customer can see the information online, make online booking according to the availibility.
2. Create a backend for the technician so that the correct customer information is visible.
3. Create a system so that the technician can update the customer about the status of the repair.
4. Create a system that sends an invoice to the customer on click of a button by the technician. //nice to have

## Project phases
|Phase|Start date|End date|Description|
|-----|----------|--------|-----------|
|0|10/12|14/12|Project preparation|
|1|15/12|19/12|Create front end with Bootstrap|
|2|19/12|24/12|Create Read functionality|
|3|24/12|29/01|Update Delete functionality|
|4|29/12|03/01|Testing and finalise|


## User stories


### sprint 0
In this sprint I prepared myself for the project by setting up the environment, database and doing an initial deployment to Heroku (just to make sure that connections are working fine). I created my first main app, which is the book_repair. And I created the model as well as creating the product backlog items. I planned a meeting with my mentor to discuss my project. The following changes I decided to make:

Make the scope of the project smaller by:
1. Building the application for the device type phones only. Initially, I wanted to go with the categories laptops, tablets and phones. Looking at the time constraints I decided to focus on the functionality rather than different types of devices. 
2. For the brands, I chose to go with the two biggest ones Apple and Samsung (In Samsung specifically for the s-series). As these are the ones with the highest number of requests.
3. Dropping the invoice functionality. Adding this to the future enhancements. For now I want to focus only on the booking system with the CRUD functionality. 

Other considerations

Different services take different amount of times. However, for this project, I will consider each service to have a duration of one hour.


### sprint 1

Initialy, I was planning to use a Bootstrap template and edit the template to make my own. However, to learn more about Bootstrap and make this a fully custom project, I decided to start from blank and bring my ideas to the front. When I started with this I saw myself using css. Later in the process I discovered that Bootstrap has more to offer and I can actually make use of that. I learnt the margins and paddings in Bootstrap. Also, copied the grid at places(in the homepage and the book repair page) from the Bootstrap library. This was very easy to use as it gave me the flexibility through all screen sizes.

### sprint 2
This was the the more complicated part of the project as working in Django requires placing a piece of code in multiple places. In this part I discovered that my model was not always correctly setup or that I was missing a small detail in one of the files. Django does provide good feedback in the browser which helped me solving issues. 

The biggest issue I faced here was with creating the form and submitting information

### sprint 3

Issues faced

1. Changed the model removed devices caused issues in the database. I removed the migration file and added it again
2. I was having issues with the routing


