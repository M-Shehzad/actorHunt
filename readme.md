# ActorHunt

_This project was made as a part of 5th semester assignment._

[live Demo](https://actor-hunt.herokuapp.com/)

## 🔶 Introduction

Film Making industry has always been a part of our culture. Based on the massive movie information, it would be interesting to understand the actor/actress biography and the number of movies they’ve starred in.
The Internet Movie Database (IMDb) is one of the world’s most popular sources for movie, TV and celebrity content with more than 100 million unique visitors per month.
In this project, we take IMDb actor details as a response variable and display it to the users.

## 🔶 Project Description

The application opens a webpage where the users can search for the actor/actress they need information on. The search then returns the users with actor details and two download options which include a word document with their biography and an excel sheet with the movies or shows they’ve starred in.
Our application ActorHunt provides a database that includes various details of the actors/actress’. The idea of our project is to get data by web scraping the details of the actor/actress from the IMDB website and use a database as a cache for the previously searched actors.

- ### Database

  ActorHunt contains a database with two tables. One stores the details of the actor like name, date of birth, profession, photo and their description and the other table stores the movie or show the actor has starred in and their corresponding year of release.
  The web scraping process is done only when the actor is not found in the database and a copy of the scraped information is stored in the database as a search cache, so the next time the user searches for a previously searched actor, the retrieval time would be reduced.

- ### Web Scraping

  To get the details of the actor/actress, we make a request to the IMDB website and scrape the necessary information using the BeautifulSoup Library.
  WEB APIs (RESTful Web Services)
  The exchange of data between client and server is possible through REST API i.e a POST request to the URL `/search` . We use a POST request to send the searched actor name from the client and receive it in the server. Necessary actions are performed on this request data and finally the response is sent back to the client.

- ### JSON

  The exchange of data on the web takes place using JSON, so in our web application the data is parsed into JSON format and communicated between client and server.
  The actor name is sent as a POST request in JSON format.
  The scraped data of the actor is JSONified and sent as a response to the POST request.

- ### Excel Spreadsheets

  When a user searches for a particular actor/actress , the application performs the necessary actions needed to retrieve the movies and their corresponding year of release, of the searched actor, which is then written into the Excel Spreadsheet that can be downloaded and viewed by the user.

- ### Word Document
  The detailed biographical information and the picture of the searched actor is written into the word document and made available for the user to download and view.

## 🔶 Execution

Demo Video:
https://github.com/M-Shehzad/adp-miniproject/blob/main/Actor%20Search.mp4

_run the application by typing the following in terminal_

`python actorHunt.py`
