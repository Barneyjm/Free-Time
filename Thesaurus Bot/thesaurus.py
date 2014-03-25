# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 17:00:17 2014

@author: James
"""

import praw
import wolframalpha
import time
import locale

from Collections import Counter

if __name__ == "__main__":
    user_agent = "Thesaurus Bot 1.0 by /u/cardstocks"
    r = praw.Reddit(user_agent=user_agent)
    r.login('MoneyExchanger', 'jungfop54') #remove from readable.
    print "logged in to reddit"
    
    client = wolframalpha.Client('8XR347-UXW4WJP9EX')
    print "connected to Wolfram"
    
    # default_subs = [adviceanimals,AskReddit,aww,bestof,books,earthporn,
    #    explainlikeimfive,funny,gaming,gifs,IAmA,movies,music,news,pics,
    #    science,technology,television,todayilearned,videos,worldnews,wtf]
    
    already_found = {}  #really we want to read this from a file. and save when we close it
    
    
    
    while True:
        subreddit = r.get_subreddit('test')
        all_comments = subreddit.get_comments()
        print "found comments"
        for comment in all_comments:
            try:
                body = comment.body.lower()
                tokens = nltk.tokenize(body)              
                count = Counter(tokens)
                
                for word in count.most_common(1):
                    common = word[0]
                    amount = word[1]
                    print "getting synonyms for %s" %word[0]
                    if common not in already_found:
                        result = client.query('%s synonym' %word[0])
                        new_entry = {word: result}
                        already_found.append(new_entry)
                    else:
                        result = already_found[common]                     
                    
                #print body
                if any(word in body for name in currency_names) and comment.id not in already_converted:
                    print word
                    words = body.split()
                    #print words.index("test") 
                    #amount = words.index(
                    most_common = "massive"
                    result = client.query('%s synonym' %op_amount)
                    
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
            
            
        
