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
|1|15/12|19/12|Create front end|
|2|19/12|24/12|Create back end|
|3|24/12|29/01|Testing|
|4|29/12|03/01|Finalise|



### sprint 0
In this sprint I prepared myself for the project by setting up the environment, database and doing an initial deployment to Heroku (just to make sure that connections are working fine). I created my first main app, which is the book_repair. And I created the model as well as creating the product backlog items. I planned a meeting with my mentor to discuss my project. The following changes I decided to make:

Make the scope of the project smaller by:
1. Building the application for the device type phones only. Initially, I wanted to go with the categories laptops, tablets and phones. Looking at the time constraints I decided to focus on the functionality rather than different types of devices. 
2. For the brands, I chose to go with the two biggest ones Apple and Samsung. As these are the ones with the highest requests.
3. Dropping the invoice functionality. Adding this to the future enhancements. For now I want to focus only on the booking system with the CRUD functionality. 

## User stories

Customer
As a customer I want so that

Technician

## Features

As a customer 

1. Select device
2. Select the issue
3. Send repair request


As a technician

1. Create an overview of all bookings 
  - Information visible in the overview: customer name, contact, booking date, IMEI number, device
  - Sort by new to old
  - Search booking based on customer name, contact, booking date, IMEI number, device
2. Update status
  - See more details button
  - Create option to change the status: "Not received yet", "In progress", "Completed", "More information required".
3. Send invoice on button click
  - Create invoice template
  - Build email functionality