import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


trending_url='https://github.com/trending'
response = requests.get(trending_url)
page_contents=response.text
doc=BeautifulSoup(page_contents,'html.parser')

# def scrape_trending(trending_url,path):
#     if os.path.exists(path):
#         print('The file {} already exists.'.format(path))
#         return


    
        

#to extract link under h1 tags
def get_link_repos(doc):
    link_selector='h3 lh-condensed'
    repo_tags=doc.find_all('h1',{'class':link_selector})
    links=[]
    for i in range(len(repo_tags)):
        repo_info=get_repo_links(repo_tags[i])
        links.append(repo_info)
    return  links

#to obtain link href
def get_repo_links(h1_tags):
    a_tags=h1_tags.find_all('a')
    link_name=a_tags[0].text.strip()
    base_url='http://github.com'
    final_url=base_url+a_tags[0]['href']
    return final_url


# exctacting username
def get_trending_usernames(doc):
    trending_usernames=[]
    span_selector='text-normal'
    user_title=doc.find_all('span',{'class':span_selector})
    for tags in user_title:
        new_user_title=tags.text.replace(" ","").strip()
        new_title=new_user_title.replace("/","")
        trending_usernames.append(new_title)
    return trending_usernames    

#extracting both username and topic
def get_trending_content(doc):
    whole_content=[]
    whole_selector='h3 lh-condensed'
    whole_title=doc.find_all('h1',{'class':whole_selector})
    for tags in whole_title:
        new_content=tags.text.replace("\n","").strip()
        trending_new_content=new_content.replace(" ","").strip()
        #get_trending_link(trending_new_content)
        whole_content.append(trending_new_content)
    return whole_content    
    # trending_link=[]    
    # for i in range(len(whole_content)):
    #     base_url='http:/github/'
    #     link=base_url+whole_content[i]
    #     trending_link.append(link) 

#get description
def get_trending_description(doc):
    trending_description=[]
    desc_selector='col-9 color-fg-muted my-1 pr-4'
    trending_desc=doc.find_all('p',{'class':desc_selector})
    for tags in trending_desc:
        trending_description.append(tags.text.strip())
    return trending_description    

#scarping 
def scrape_trendings():
    trending_url='https://github.com/trending'
    response=requests.get(trending_url)
    #check_response
    if response.status_code!=200:
        raise Exception('Failed to open the page {}'.format(trending_url))
    trending_dict={'Username':get_trending_usernames(doc),'Repo':get_trending_content(doc),'Description':get_trending_description(doc),'Url':get_link_repos(doc)}    
    trending_df=pd.DataFrame(trending_dict)
    if os.path.exists('Trending.csv'):
        print('The file already exists')
        exit()    
    else:    
        trending_df.to_csv('Trending.csv',index=None)   
        return pd.DataFrame(trending_dict)
    

def scrape_trending_repos():
    print("Scrapping Trending topics from GitHub")
    trendings_df=scrape_trendings()
    for index, row in trendings_df.iterrows():
        print('Scrapping for Trending Repo "{}"'.format(row['Username']))
    #create excel spreadsheet   
    read_file = pd.read_csv (r'E:\\vscode\Webscrapping\\Trending.csv')
    read_file.to_excel (r'E:\\vscode\Webscrapping\\Trending.xlsx', index = None, header=True) 
    print("Scarpping Done!") 

scrape_trending_repos()  

