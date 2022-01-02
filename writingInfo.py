#ADP PROJECT
import requests,bs4
import openpyxl
import docx,os

#imdb actor page 
actor = input('Enter the actor name: ')
res = requests.get('https://www.imdb.com/find?q='+actor.replace('','+'))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
soupelem = soup.select('.result_text a')
actorpage = requests.get('https://www.imdb.com'+soupelem[0].get('href'))
actorpage.raise_for_status()

#actor page soup
soup = bs4.BeautifulSoup(actorpage.text)

#actor info
actorName = soup.select('.header .itemprop')[0].text
actorJobs = list(map(lambda name: name.text[1:],soup.select('#name-job-categories a span')))
actorPhoto = soup.select('#name-poster')[0].get('src')
actorPhotoPath = actorPhoto.split('/')[-1]
# actorDescription = soup.select('.name-trivia-bio-text .inline')[0]
# print(actorDescription.text.split('...')[0])
actorBDsoup = soup.select('#name-born-info')[0]
actorBD = ' '.join(list(map(lambda text:text.strip(),actorBDsoup.text.split('\n'))))
print(actorJobs)

#all the movies of the actor
soupelem = soup.select('#filmo-head-actor + .filmo-category-section .filmo-row')

# wb = openpyxl.Workbook()
# sheet = wb.get_active_sheet()
# sheet['A1'].value = 'Title'
# sheet['B1'].value = 'Year'

# for movies in soupelem:
#     movieYear = movies.select('.year_column')[0].text
#     movieTitle = movies.select('b a')[0].text
#     print(movieTitle+' in '+movieYear)
    

wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
sheet['A1'].value = 'Title'
sheet['B1'].value = 'Year'

for row in range(2,len(soupelem)+2):
    movie = soupelem[row-2]
    sheet['A'+str(row)]=movie.select('b a')[0].text
    sheet['B'+str(row)]=movie.select('.year_column')[0].text[:6]
    
os.makedirs('photos',exist_ok=True)
res = requests.get(actorPhoto)
imageFile = open(os.path.join('photos',os.path.basename(actorPhoto)),'wb')

for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

doc = docx.Document()
doc.add_paragraph(actorName,'Title')
doc.add_picture('./photos/'+actorPhotoPath,width=docx.shared.Cm(5))
doc.add_paragraph('Actor Jobs: '+', '.join(actorJobs))
doc.add_paragraph(actorBD)


wb.save('actorMovies.xlsx')
doc.save('actordesc.docx')
print('success!')