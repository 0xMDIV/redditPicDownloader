# USAGE
#python picBot.py -sub "Art" -n 20 -sort "top" -t "month"

import praw,os,requests,shutil,json,argparse,urllib
from prawcore import NotFound

path = os.getcwd()+'/'
url = "https://www.reddit.com/"
name = 0

def fetch_images(submission):
    url = (submission.url)
    filename = str(submission.id)
    # filename = str(name)
    if url.endswith(".jpg"):
        filename+=".jpg"
        found = True
    elif url.endswith(".png"):
        filename+=".png"
        found = True
    else:
        found = False
    
    if found == True: # if image found save it
        if os.path.isfile(path+args['subreddit']+'/'+filename): # check if the found image already exists in the given path 
            print("This picture already exists")
        else:
            r = requests.get(url)
            with open(filename, 'wb') as w:
                w.write(r.content)

            shutil.move(path+filename,path+args["subreddit"]) # move the downloaded image to the folder(named after subreddit)
            print(filename)

def subreddit(sub, number, sort, time, reddit):
    
    # init the subreddit
    subreddit = reddit.subreddit(args["subreddit"])
    name = 0

    if sort == 'top': # sort search by top with given time_filter i.e day, month etc.
        for submission in subreddit.top(time_filter=time, limit=number): # limit is used to define how many images we want
            name+=1
            if name == number+1:
                break
            else:
                fetch_images(submission)

    if sort == "hot": # sort search by hot
        for submission in subreddit.hot(limit=number):
            name+=1
            if name == number+1:
                break
            else:
                fetch_images(submission)

    if sort == "best": # sort search by best
        for submission in subreddit.best(limit=number):
            name+=1
            if name == number+1:
                break
            else:
                fetch_images(submission)

    if sort == "new": # sort search by new
        for submission in subreddit.new(limit=number):
            name+=1
            if name == number+1:
                break
            else:
                fetch_images(submission)
        

def sub_exists(sub, reddit):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists

def createDir(sub):
    # path+="Art"
    # make a new folder at the given path
    if not os.path.isdir(path+sub):
        os.mkdir(path+sub)
        

# def main():
parser = argparse.ArgumentParser()
parser.add_argument('-sub',"--subreddit", required=True, help="Name of subreddit")
parser.add_argument('-n',"--number", required=True, type=int, help="Number of images")
parser.add_argument('-sort',"--sort", help="Sort by", default='hot')
parser.add_argument('-t',"--time_filter", help="Top of day/month/year", default='day')
args = vars(parser.parse_args())


# load required creds from json file
with open(path+'/cred.json') as f:
        params = json.load(f)

reddit = praw.Reddit(client_id = params['client_id'],
            client_secret = params['client_secret'],
            user_agent = params['user_agent'])

if not sub_exists(args["subreddit"], reddit):
    print(f"Subreddit: {args['subreddit']} not found")
    exit
else:
    createDir(args['subreddit'])
    subreddit(args['subreddit'], args['number'], args['sort'], args['time_filter'], reddit)
