# Smart Tech Repair

## Project Description
Smart Tech Repair is a small business specialized in repairs of phones, laptops, tablets, gaming, (smwart)watches and much more. The company aims to deliver fast and reliable service to its customers. The customers can either do an online booking or walk-in to the store during the opening hours. 


### Current process (ist)
Customers lookup for information on the business profile of the company on Google and give a call to Smart Tech. On the phone they request for information. The technician needs to find out the price (as these drop and go up quickly) and the availibility of the part and often has to keep the customer waiting over the phone or give a call back after finding out the information. 


### New process (soll)
Customer leave its details and the a descripion of the issue behind. The technician prepares for this and contact the customer. The ticket status is updated to keep the customer up-do-date and has a history of tickets that were created before.

### Scope
During this project the focus will be on the device type: phones. As these categories are the most common onces with the most repairing requests. Furthermore, the aim to solve the following issues:
1. Make the process easier so that the technician has information in advance and is fully prepared when contacting the customer
2. Create an application that the customer can create a ticket with the issue for the device.
3. check the history of repairs with Smart Tech so that for any requests in the future the technician can give a personalized service.
4. Option to login and check the status as the user


## The model

### Data model
The models consists of five classes. I havent used the class service for this project, but left it in the project for future enhancements.

![data-model](docs/data-model.PNG)


### The classes

#### Phonemodel
For storing the phones by manufacturer and series. Made this unique by adding slug

|Key|Name|Type|Extra info|
|---|----|----|----------|
|manufacturer|Charfield|Choices|
|series|Charfield||
|slug|slugfield||Unique - combination of manufacturer and series|


#### Part
For saving the parts.

|Key|Name|Type|Extra info|
|---|----|----|----------|
||part|Charfield|choices|

#### Service
Each phone has a different price for the part. Therefore, I created this table. Innitialy, I used the table Part for the price. During the process I recognized that I had created a more to more relation. Due to time constraints I didnt use this table and I left it in for future enhancements.

|Key|Name|Type|Extra info|
|---|----|----|----------|
|Foreign Key|Phonemodel|Phonemodel||
|Foreign Key|Broken_part|Part||
||Price|DecimalField|2 places decimal|


#### Ticket

|Key|Name|Type|Extra info|
|---|----|----|----------|
|Primary Key|ticket_number|Charfield|Unique|
|Foreign Key|phonemodel|Phonemodel||
|Foreign Key|customer|User||
|Foreign Key|broken_part| Part||
||status|Integerfield|Choices - default = pending|
||imei|Charfield||


#### User

This is the build in table of Django. I used this for authentication purposes. 


## Agile 

### Project phases
|Phase|Start date|End date|Description|
|-----|----------|--------|-----------|
|0|10/12|14/12|Project preparation|
|1|15/12|19/12|Create front end with Bootstrap|
|2|19/12|24/12|Create Read ticket|
|3|24/12|29/01|Update Delete ticket|
|4|29/12|03/01|Testing and finalise|


#### sprint 0 Project Planning
In this sprint I prepared myself for the project by setting up the environment, database and doing an initial deployment to Heroku (just to make sure that connections are working fine). I created my first main app, which is the book_repair. And I created the model as well as creating the product backlog items. I planned a meeting with my mentor to discuss my project. The following changes I decided to make:

Make the scope of the project smaller by:
1. Building the application for the device type phones only. Initially, I wanted to go with the categories laptops, tablets and phones. Looking at the time constraints I decided to focus on the functionality rather than different types of devices. 
2. For the brands, I chose to go with the two biggest ones Apple and Samsung (In Samsung specifically for the s-series). As these are the ones with the highest number of requests.
3. Dropping the invoice functionality. Adding this to the future enhancements. For now I want to focus only on the booking system with the CRUD functionality. 

Other considerations

Different services take different amount of times. However, for this project, I will consider each service to have a duration of one hour.


#### sprint 1 Create Front-end with Bootstrap

At first, I was planning to use a Bootstrap template and edit the template to make my own. However, to learn more about Bootstrap and make this a fully custom project, I decided to start from blank and bring my ideas to the front. When I started with this I saw myself using css. Later in the process I discovered that Bootstrap has more to offer and I can actually make use of that. I learnt the margins and paddings in Bootstrap. Also, copied the grid at places(in the homepage and the book repair page) from the Bootstrap library. This was very easy to use as it gave me the flexibility through all screen sizes.

#### sprint 2 Create ticket

This was the the most complicated phase for me as Django consists of multiple files and sometimes I had to look which bit to place where. In this phase I created the ticket form to save new information to the database. I made use of the course content, but realised that I was doing something wrong. I was trying to combine three forms in one which was causing lots of issues. I was able to solve the issues, but I knew that going forwards with this would not be the best solution. 

I combined three forms:
1. I created a table for customer instead of using the user table. Which would mean that the customer has to fill every time its personal details when creating a ticket. This was one part of the form.
2. I used the part from the Part table instead of using the foreign key from the Ticket table in the form
3. The ticket form (which I would only need to use)

And the biggest issue with this setup was that the logged in user could create multiple customers and access the customers. Also, I realised that the User table is very powerfull and I should be using that. 

Because of the issues above I was not able to finish the sprint goal within the time frame. As I was not fully sure how to solve these issues I kept the PBI for creating a new customer on hold. Because of this reason I had a overlap with sprint 3. 


#### sprint 3 Update and delete

This sprint had a overlap with the previous one. In this sprint I changed model. Managed to retrieve the data and update and delete. Some major blockers for me in this sprint were:

1. Removing the Customer table and using the User table instead. As I had mulptiple relations with the Customer table this was giving me errors. I made the mistake of first removing the customer and then trying to replace. This broke my application and I was not able to understand where things were not going right. I then uncomitted the changes. First I changed all the places the data is used by the customer data. When I was sure that there was no link left I was able to delete the Customer with no errors.
2. I added a ticket number for all requests.
3. I added a slugfield for a user-friendly url. This caused the issue of empty fields in the database as I already had added the the phonemodels and the series. I started with allowing Null values. Then I wrote a shell script to push the data to the database for all phonemodels. 

At the end of this sprint I have some pending tasks open: Redirecting to correct pages.


## Deployment


## Bugs and fixes


