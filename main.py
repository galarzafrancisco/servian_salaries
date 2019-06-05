from bs4 import BeautifulSoup
import urllib.request
import re
import os

site_url = os.environ.get('SITE_URL') or 'https://jobs.lever.co/servian'

def make_soup(url):
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def get_job_links(main_url):
    soup = make_soup(main_url)
    link_elements = soup.find_all("a", {"class": "posting-btn-submit"})
    links = [element.get('href') for element in link_elements]
    return links

def get_salary(soup):
    position = soup.find('h2').text
    salary = re.findall('\$\d+K*k*\s*.\s*\$*\d+K*k*', soup.text)
    return {
        'position': position,
        'salary': salary
    }

job_links = get_job_links(site_url)

if __name__ == '__main__':
    for job_link in job_links:
        soup = make_soup(job_link)
        salary = get_salary(soup)
        if (salary['salary']):
            print('{} - {} - {}'.format(salary['salary'], salary['position'], job_link))