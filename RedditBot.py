
import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.random_subreddit()
#print(subreddit)

for submission in subreddit.hot(limit=5):

    print("Title: ", submission.title + " Score:", submission.score)
   # print(reddit.user.me())
    #print("Tags:", submission)
   # 0
for comment in reddit.subreddit('redditdev').comments(limit=25):
    print(comment.author)


#for reddit.submission in reddit.front.new(limit=5):
   # reddit.submission.reply("Why Hello There!")
    

#reddit.domain('imgur.com').new()