# Reddit Image Downloader

## Prerequisite
* Reddit Account
* Reddit developers app
* Python praw library installed

### How to make Make Reddit Developers Apps

1. First login to your reddit account, then go to the [Reddit App Page](https://www.reddit.com/prefs/apps)
2. Fill the form under "create application" and click "create app".
![Screenshot of form](/howTo/createForm.jpg)

### USAGE
* Clone the project into your local machine.
* Go to your created app page and copy client_id, client_secret, and user_agent values.
![Application creds](/hotTo/appPage.jpg)

* Then open creds.json file and insert these copied values. And your good to go.
* Open terminal in folder where project is cloned and run this command python picBot.py -sub "Art" -n 20 -sort "top" -t "month".
* -sub: Name of the subreddit 
* -n: number of images you want to download
* -sort: sort subreddit by i.e. new, best, top, etc.
* -t: timeline i.e. day, week, month ,etc. **-t is optional and only used when you sort by 'Top'**.
