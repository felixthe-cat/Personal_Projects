from types import NoneType
from bs4 import BeautifulSoup
import requests

def run():
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

def debug():
    with open('Part-Time_RA_Websites','r') as websites:
        f = open('Part-time_RA_Descriptions','a')
        content = websites.read()
        website_list = content.split('\n')
        # print(website_list)

        for website in website_list:
            experiment_links = []
            experiment_title = []
            html_text = requests.get('http://sl-iitr.vlabs.ac.in/List%20of%20experiments.html').text
            soup = BeautifulSoup(html_text, 'lxml')

            list = soup.find('div',{'class': 'vlabs-page-content px-5 pb-4 flex-grow-1 markdown-body'}).find_all('li')
            print(list)
            for element in list:
                experiment_link = element.find('a')
                # print(experiment_link['href'])
                experiment_links.append(experiment_link['href'])
                experiment_title.append(experiment_link.text.strip())

            # chapter = soup.find('h2').text
            # text = '\n\nTopic: '+ chapter + '\n\n'
            # f.write(text)

            print(experiment_links)
            # experiment_title = ['Study of various parts of Auto Level', 'Study of Plane Table and its Accessories', 'Detail Plotting by Radiation Method', 'Detail Plotting by Intersection Method', 'Carry out Contouring in the field', 'Study of Global Positioning System (GPS) and its Accessories', 'Observations using GPS', 'Observations of vertical and horizontal angles using total station (Total station)', 'To find out elevations of various points on the ground using auto-level by Profile Levelling method', 'To find out elevations of various points on the ground using auto level (Fly Level)', 'Detail Plotting by Resection Method']
            

            for index, link in enumerate(experiment_links):
                print('-----------------------------------------------------------------------------------------------------------')
                print(link)
                # C:\Users\lawfe\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\certifi\cacert.pem
                # html_text = requests.get(link).text
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                # soup = BeautifulSoup(html_text, 'lxml')
                # description = soup.find('h4').text
                # print('Description:',description)
                # print('\n')
                title = experiment_title[index] + ' ( ' + link +' ) \n'
                f.write(title)
                text = 'Description: \n\n'
                f.write(text)
                 
    return 

run()
            
# http://fm-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://ts-nitk.vlabs.ac.in/transportation-engineering/List%20of%20experiments.html
# https://ee1-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://ee2-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://fmc-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://ms-nitk.vlabs.ac.in/List%20of%20experiments.html
# https://mg-nitk.vlabs.ac.in/List%20of%20experiments.html
