from types import NoneType
from bs4 import BeautifulSoup
import requests

def virtual_lab():
    with open('Part-Time_RA_Websites','r') as websites:
        f = open('Part-time_RA_Descriptions','a')
        content = websites.read()
        website_list = content.split('\n')
        # print(website_list)

        for website in website_list:
            experiment_links = []
            experiment_title = []

            html_text = requests.get(website).text
            soup = BeautifulSoup(html_text, 'lxml')

            list = soup.find('div',{'class': 'vlabs-page-content px-5 pb-4 flex-grow-1 markdown-body'}).find_all('li')
            for element in list:
                experiment_link = element.find('a')
                # print(experiment_link['href'])
                experiment_links.append(experiment_link['href'])
                experiment_title.append(experiment_link.text.strip())

            chapter = soup.find('h2',{'class': 'text-center'}).text
            text = '\n\nTopic: '+ chapter + '\n\n'
            f.write(text)


            for index, link in enumerate(experiment_links):
               
                    
                html_text = requests.get(link).text
                soup = BeautifulSoup(html_text, 'lxml')
                tmp1 = soup.find('h4')
                tmp2 = soup.find('h3')
                tmp3 = soup.find('p')
                description = ''
                if type(tmp1) != NoneType:
                    description = tmp1.text
                elif type(tmp2) != NoneType:
                    description = tmp2.text
                elif type(tmp3) != NoneType:
                    description = tmp3.text
                print('Description:',description)
                print('\n')
                title = experiment_title[index] + ' ( ' + link +' ) \n'
                f.write(title)
                text = 'Description: '+description+'\n\n'
                f.write(text)
    return 

def visual_lab():
    with open('Part-Time_RA_Websites','r') as websites:
        f = open('Part_Time_RA_Visual_Lab_Des','w')
        content = websites.read()
        website_list = content.split('\n')
        # print(website_list)

        for website in website_list:
            experiment_links = []
            experiment_title = []

            html_text = requests.get(website).text
            soup = BeautifulSoup(html_text, 'lxml')

            tmp = soup.find('div', {'class': 'target-entity-content'})
            list = tmp.find_all('li')
            print(list)
            
            chapters = tmp.find_all('h3')
            for chapter in chapters:
                text = '\n\nTopic: '+ chapter.text + '\n\n'
                f.write(text)
            
            for index, li in enumerate(list):
                a = li.find('a')
                i = li.find('i')
                print(a['href'])
                experiment_links.append(a['href'])
                experiment_title.append(a.text.strip())
                # block = soup.find('p','style16')
                # tmp1 = block.find('a')
                # description = tmp1
                # if type(tmp1) != NoneType:
                #     description = tmp1.text
                # elif type(tmp2) != NoneType:
                #     description = tmp2.text
                # elif type(tmp3) != NoneType:
                #     description = tmp3.text
                # print('Description:',description)
                # print('\n')
                title = experiment_title[index] + ' ( ' + a['href'] +' ) \n'
                f.write(title)
                text = 'Description: ' + li.text.strip() + '\n\n'
                # if type(i) != NoneType:
                #     text = text 
                f.write(text)

            

                 
    return 

def reogranise():

    return 

visual_lab()
            
# http://fm-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://ts-nitk.vlabs.ac.in/transportation-engineering/List%20of%20experiments.html
# https://ee1-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://ee2-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://fmc-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://ms-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://mg-nitk.vlabs.ac.in/List%20of%20experiments.html
