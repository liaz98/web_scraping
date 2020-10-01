from bs4 import BeautifulSoup
import requests
import csv
source = requests.get('https://www.gkseries.com/general-knowledge/geography/geo-tectonics/geography-mcqs').text
soup = BeautifulSoup(source, 'lxml')
csv_file=open('web_scraping.csv', 'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['QUESTION','OPTION: A','OPTION: B','OPTION: C','OPTION: D','ANSWER'])
i=0
for question in soup.find_all('div', class_="mcq"):
    question_content=question.find('div', class_="question-content")
    question_content.span.decompose()
    i+=1
    question_content=question_content.text.strip()
    question_content=str(i)+" "+question_content
    num=0
    answer=question.find('div', class_="collapse")
    answer=answer.find('div', class_="card")
    answer=answer.find('blockquote').text.strip()
    option_list=[]
    for option in question.find_all('div', class_="option"):
        option.span.decompose()
        num+=1
        question_option=option.text
        option_list.append(question_option)
    converted_list=[]
    for element in option_list:
        converted_list.append(element.strip())
    csv_writer.writerow([question_content,converted_list[0], converted_list[1], converted_list[2], converted_list[3], answer])

csv_file.close()

    