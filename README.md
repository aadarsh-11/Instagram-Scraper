# Instagram-Scraper
A simple tool to save all the images of an Instragram Handle

## How to use?

- Clone the repo and install dependencies by using this command in the terminal: 

      pip install -r requirements.txt


- This application works on chrome browser so if you don't have, please go ahead and install it from [here](https://www.google.com/chrome/?brand=YTUH&gclid=CjwKCAjw8cCGBhB6EiwAgORey5Bar_RZgnl2L_Tow7uUhqj0yD0lXlSb3Zmev98sj7CYAPt5wIrtohoCmmUQAvD_BwE&gclsrc=aw.ds)
- Download and replace the [chromedriver](https://chromedriver.chromium.org/downloads) with the one which has the version of your chrome browser.
- Just run the [main.py](./main.py) file to run the program

## Note:

- If you do not have D-drive, then change the destination path variable on line 47 in main.py and replace "D:/InstaScraper/" to "C:/InstaScraper/"
- Enter valid credentials of your own instagram when prompted as selenium will scrape instagram using your account.
- Sit back and relax and the program will do everything and then automatically open the folder where the images are saved.
- you can only save images from handles you are allowed to see from your instagram account (i.e the private accounts you follow and all public accounts)
