import requests, bs4
import openpyxl

# imdb actor page

actor = input("Enter the actor name: ")
# searches the actor in imdb and chooses the first option
res = requests.get("https://www.imdb.com/find?q=" + actor.replace("", "+"))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
soupelem = soup.select(".result_text a")
actorpage = requests.get("https://www.imdb.com" + soupelem[0].get("href"))
actorpage.raise_for_status()

# goes to the actor's page and selects all the movie segements
soup = bs4.BeautifulSoup(actorpage.text, "html.parser")
soupelem = soup.select("#filmo-head-actor + .filmo-category-section .filmo-row")


# excel segment
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
sheet["A1"].value = "Title"
sheet["B1"].value = "Year"


# # prints all the movies to excel
# for row in range(2, len(soupelem) + 2):
#     movie = soupelem[row - 2]
#     sheet["A" + str(row)] = movie.select("b a")[0].text
#     sheet["B" + str(row)] = movie.select(".year_column")[0].text[:6]

wb.save("ActorMovies.xlsx")
