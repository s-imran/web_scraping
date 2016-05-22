import sys
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


URL_MAIN = "http://ieeexplore.ieee.org/search/searchresult.jsp?queryText=machine%20learning&refinements=4291944822&rowsPerPage=10"


def extract_infos_from_description(description):
    try:
        for c in description.find_all("a", class_="ng-binding ng-scope"):
            conf = c.string
        for y in description.find_all("span", class_="ng-binding ng-scope"):
            string = y.string
            if "Year" in string:
                year = string.split(":")[1]
        info = {"year": str(year), "conf": str(conf)}
    except:
        info = {"year": "None", "conf": "None"}
    finally:
        return info


def main(page_number, output_file, driver):
    url = URL_MAIN
    if page_number > 0:
        url = URL_MAIN + "&pageNumber={}".format(page_number)
    if page_number == 4000:
        print "Reached end"
        driver.close()
        sys.exit()
    print "url:{}".format(url, page_number)

    try:
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source)
        for l in soup.find_all("div", class_="article-list List-results ng-isolate-scope"):
            for d in l.find_all("div", class_="description u-mb-1"):
                info = extract_infos_from_description(d)
                output_file.write("{}, {}\n".format(info["year"], info["conf"]))
    finally:
        main(page_number + 1, output_file, driver)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    with open("/home/saad/Desktop/ml_years_conf.txt", "a") as f:
        main(3767, f, driver)
