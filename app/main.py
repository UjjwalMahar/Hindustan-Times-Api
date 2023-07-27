from fastapi import FastAPI
from bs4 import BeautifulSoup as Bs
import requests
import os
from dotenv import load_dotenv
import uvicorn


app = FastAPI()


# Load the environment variables from .env file

load_dotenv()

# Get the proxy credentials from the environment variables

proxy_username = os.getenv("PROXY_USERNAME")
proxy_password = os.getenv("PROXY_PASSWORD")
proxy_ip = os.getenv("PROXY_IP")
proxy_port = os.getenv("PROXY_PORT")

# Construct the proxy URL with the credentials

proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_ip}:{proxy_port}"


agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

@app.get("/")
def read_root():
    return {"go to tags"}

@app.get("/top-world-news")
def top_world_news():
    url = "https://www.hindustantimes.com/world-news"
    response = requests.get(url, proxies={'http': proxy_url}, headers=agent)

    # Check if the request was successful
    if response.status_code == 200:
        print("Success")
    else:
        print("UnSuccessful")
    soup = Bs(response.content, 'html.parser')

    # #Function to return world top news form the hindustan times 

    world_headline = soup.find_all('h3',{"class":"hdg3"})
    headline = []  
    for tag in world_headline:
        tags = tag.find_all("a")
        for data in tags:
            headline.append(data.get_text())
    return headline

@app.get("/top-news")
def top_news_title():
    url = "https://www.hindustantimes.com/"
    response = requests.get(url, proxies={'http': proxy_url}, headers=agent)

    # Check if the request was successful
    if response.status_code == 200:
        print("Success")
    else:
        print("UnSuccessful")
    soup = Bs(response.content, 'html.parser')

    # #Function to return world top news form the hindustan times 

    world_headline = soup.find_all('h3',{"class":"hdg3"})
    headline = []  
    for tag in world_headline:
        tags = tag.find_all("a")
        for data in tags:
            headline.append(data.get_text())
    return headline


@app.get("/top-india-news")
def top_india_title():
    url = "https://www.hindustantimes.com/"
    response = requests.get(url, proxies={'http': proxy_url}, headers=agent)

    # Check if the request was successful
    if response.status_code == 200:
        print("Success")
    else:
        print("UnSuccessful")
    soup = Bs(response.content, 'html.parser')

    # #Function to return world top news form the hindustan times 

    world_headline = soup.find_all('h3',{"class":"hdg3"})
    headline = []  
    for tag in world_headline:
        tags = tag.find_all("a")
        for data in tags:
            headline.append(data.get_text())
    return headline

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)