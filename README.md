## Automated filters for gmail.

### Introduction
In this case, we will design a Flask application that will provide us with a way to automatically filter emails in our Gmail account. Specifically, it will create and use Gmail filters based on predefined criteria, such as sender address, subject line, or keywords in the body of the email.

### HTML Files
The application will require the following HTML files:

- `index.html`: This will be the main page of the application. It will contain a form for creating a new filter. The form will include fields for the filter criteria, such as sender address, subject line, and body keywords.
- `filters.html`: This page will display a list of all the filters that have been created. It will include columns for the filter criteria and the actions that the filter will perform (e.g., move to a specific label, archive, or delete).

### Routes

The application will require the following routes:

- `/`: This route will handle requests for the main page of the application. It will render the `index.html` template.
- `/create-filter`: This route will handle requests to create a new filter. It will validate the input from the form on the `index.html` page and then create the filter in Gmail using the Gmail API.
- `/filters`: This route will handle requests for the page that displays a list of all filters. It will render the `filters.html` template and pass in a list of all the filters that have been created.

### Usage

To use the application, a user will first need to create a new filter. To do this, they will visit the main page of the application and fill out the form. Once the form is submitted, the application will validate the input and then create the filter in Gmail using the Gmail API.

Once a filter has been created, it will be displayed on the page that lists all filters. From this page, a user can view the details of a filter, edit the filter, or delete the filter.