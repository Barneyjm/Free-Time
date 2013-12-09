import praw
import wolframalpha
import time
import locale

if __name__ == "__main__":
    user_agent = "CurrencyConvert 1. by /u/cardstocks"
    r = praw.Reddit(user_agent=user_agent)
    r.login('MoneyExchanger', 'jungfop54')
    print "logged in to reddit"
    
    client = wolframalpha.Client('8XR347-UXW4WJP9EX')
    print "connected to Wolfram"
    already_converted = set()
    
    currency_names = ['dollars', 'euros', 'pounds']
    currency_symbols = ['$', 'en_AU.utf8', 'en_BW.utf8', 'en_CA.utf8',
    'en_DK.utf8', 'en_GB.utf8', 'en_HK.utf8', 'en_IE.utf8', 'en_IN', 'en_NG',
    'en_PH.utf8', 'en_US.utf8', 'en_ZA.utf8',
    'en_ZW.utf8', 'ja_JP.utf8']
    
    # default_subs = [adviceanimals,AskReddit,aww,bestof,books,earthporn,
    #    explainlikeimfive,funny,gaming,gifs,IAmA,movies,music,news,pics,
    #    science,technology,television,todayilearned,videos,worldnews,wtf]
    
    
    
    while True:
        subreddit = r.get_subreddit('test')
        all_comments = subreddit.get_comments()
        print "found comments"
        for comment in all_comments:
            try:
                body = comment.body.lower()
                #print body
                if any(word in body for name in currency_names) and comment.id not in already_converted:
                    print word
                    words = body.split()
                    #print words.index("test") 
                    #amount = words.index(
                    op_amount = "35 euro"
                    result = client.query('%s in US dollars' %op_amount)
                    
                    #print(next(result.results).text)
                    #reply = ""
                    reply = "> %s" %op_amount
                    reply = reply + "\n\n I think you meant \n\n"
                    reply = reply + "$" + str(next(result.results).text)
                    print reply
                    #comment.reply(reply)
                    already_converted.add(comment.id)
                else:
                    print "continue"
                    continue
            except:
                continue
        ###
        print already_converted
        time.sleep(30)
            
            
        
