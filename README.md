# 🗞️Hindustan Times Newspaper API

![Hindustan Times](https://www.hindustantimes.com/static-content/1y/2023/ht-images/ht-logo.png)

Welcome to the Hindustan Times Newspaper API! This API allows you to access trending headlines or titles listed in Hindustan Times for different news categories. The API provides three main endpoints to retrieve top news from various topics: `/top-world-news`, `/top-india-news`, and `/top-news`.

## 🔗Base URL 

```
https://hindustantimes-1-t3366110.deta.app
```

## Endpoints

### 1. `/top-world-news`

This endpoint retrieves the trending headlines or titles from the world news category in Hindustan Times.

#### Request

```
GET https://hindustantimes-1-t3366110.deta.app/top-world-news
```

#### Response

```json
[" Indo-Canadian Anita Anand promoted to treasury board president by Canadian PM","Eye for an eye! How Worldcoin rewards you for scanning your irises. Read","Mitch McConnell freezes and escorted away during press conference","Niger military detains President, overthrows govt as ‘coup’ declared","Why are US national parks aficionados dying during treks? Here's a grim picture" ..."]
```

### 2. `/top-india-news`

This endpoint fetches the trending headlines or titles from the India news category in Hindustan Times.

#### Request

```
GET https://hindustantimes-1-t3366110.deta.app/top-india-news
```

#### Response

```json
[" INDIA MPs to visit strife-torn Manipur on Saturday, Sunday","‘Modi, Modi vs INDIA, INDIA’: Slogan wars as Oppn seeks PM statement on Manipur","High-decibel unrest in Rajya Sabha: Jaishankar ‘upset’ over Opposition's conduct","'Gehlot ji could not come today as...': PM Modi amid PMO, CM Twitter war","Delhi jeweller stabbed to death in Karol Bagh; 1 employee arrested, 3 absconding", ...]
```

### 3. `/top-news`

This endpoint combines the trending headlines or titles from both world news and India news categories in Hindustan Times.

#### Request

```
GET https://hindustantimes-1-t3366110.deta.app/top-news
```

#### Response

```json
[" INDIA MPs to visit strife-torn Manipur on Saturday, Sunday","High-decibel unrest in Rajya Sabha: Jaishankar ‘upset’ over Opposition's conduct","'Gehlot ji could not come today as...': PM Modi amid PMO, CM Twitter war","PM Modi to inaugurate Gujarat's first Greenfield International Airport today","Indo-Canadian Anita Anand promoted to treasury board president by Canadian PM","Samsung reveals Z Flip 5, Z Fold 5, Galaxy Watch 6 and Tab S9 India prices","Novak Djokovic's father makes colossal 2024 'retirement' wish for Serbia star",,..."]
```

## 🐳Dockerfile

You can also access the api image using docker. 

```
https://hub.docker.com/r/ujjwalmahar/hindustan-times-api
```

## 📝NOTE:

Please note that this API only provides access to the trending headlines or titles from Hindustan Times. The full content of the articles is not included in the response.

That's it! You can now use the Hindustan Times Newspaper API to fetch the latest trending headlines and stay up-to-date with world news, India news, or a combination of both. Enjoy!🎉

## ⚠️Disclaimer:

The Hindustan Times Newspaper API provided here is a third-party service and is not affiliated with Hindustan Times or its official entities. This API has been developed independently to offer users access to trending headlines or titles from Hindustan Times for informational purposes only.