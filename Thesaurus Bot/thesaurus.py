# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 17:00:17 2014

@author: James Barney
"""
import ast
import nltk
from nltk.tokenize.punkt import PunktToken
import os
import praw
import wolframalpha
import time

from collections import Counter

def get_authentication():
    with open('auth.txt', 'r') as f:
        for line in f:
            yield line
    
    #return username, password, client_id
    
def get_thesaurus(fname):
    if os.path.isfile(fname):
        with open(fname, 'r') as f:
            print("Found existing thesaurus.")
            thesaurus = ast.literal_eval(f.read())
            
    else:
        print("Couldn't find an existing thesaurus.")
        thesaurus = {} 
        
    return thesaurus
    
def get_reply(common, amount, result):
    reply = "Hey! You used the word %(common)s like %(amount)s times in that last comment.\n\n\
    Here are some synonyms you might try next time!\n" % {'common': common, 'amount': amount}
    for word in result:
        reply += "    " + word + '\n'
        
    reply += "\n\n I'm a bot in progress! Please be gentle!"
    
    return reply
    
def rewrite_thesaurus(already_found, fname):
    with open(fname, 'wb') as f:
        f.write(str(already_found))
        
# Function: Add cID to set, then save set to done.txt
def save_done(cID): # cID = comment.id
    # Add comment ID the the set
    done.add(cID)
    try:
        # Append comment.id to done.txt
        with open("done.txt", "a") as file:
            file.write(cID + "\n")
    except:
        print("Error saving done.txt!")


######Setup#######
# Load done from done.txt
with open("done.txt", "r") as file: # Open done.txt in readonly-mode
    done = set(file.read().split()) # Create set





user_agent = "Thesaurus Bot 1.0 by /u/cardstocks"

auth = get_authentication()

MAX_AMOUNT = 6
username = auth.next()[:-1]
password = auth.next()[:-1]
wolfram_ID = auth.next()

r = praw.Reddit(user_agent=user_agent)
r.login(username,password)
print "logged in to reddit"

client = wolframalpha.Client(wolfram_ID)
print "connected to Wolfram"


fname = 'text.txt'
already_found = get_thesaurus(fname)

ignore = {'the','a','if','in','it','of','or', 'and', 'be', 'this', 'them', 
          'as', 'i', 'an', 'and', 'but'}

####################

# default_subs = [adviceanimals,AskReddit,aww,bestof,books,earthporn,
#    explainlikeimfive,funny,gaming,gifs,IAmA,movies,music,news,pics,
#    science,technology,television,todayilearned,videos,worldnews,wtf]


# 'https://www.google.com/search?q='+noun+'+'+word

#################### Main Loop ####################
comments = praw.helpers.comment_stream(r, 'all', limit=None) # Continually scan the comment stream
for comment in comments:
    if (comment.id not in done) and (str(comment.author) != username): # Check if comment already done, or if we made the comment ourself
        # Check for regex match in comment.body
        # Since set() cant have duplicates, we use set() to make sure we dont explain something twice in one comment
        #match = set(re.findall(r"(?:\+|\!|u\/)(?:explain|explanationbot|explainationbot|explainbot)(?:: ?| )(.*?)(?=  |\n|\.|$|\?|\+|\!|u\/)", str(comment.body), re.IGNORECASE))
        if len(comment.body) < 8:
            print comment.body
        #and (len(comment.body) == 1)
        
        #counter = Counter(x for x in nltk.word_tokenize(comment.body.lower()) if x not in ignore and x.isalpha())

        #print counter
        
        #for word in counter.most_common(1):
        #common = "asdf" ##counter.most_common(1)[0]
        #amount = 7 #count.most_common(1)[1]
        """
        if amount > MAX_AMOUNT:
            print "getting synonyms for %s" %common
            if common not in already_found:
                query = client.query('%s synonym' %common)
                result = nltk.word_tokenize(next(query.results).text)
                time.sleep(5)
                print result
                for i in result:
                    try:
                        result.remove('|')
                    except (ValueError) as e:
                        break
                print result
                new_entry = {common: result}
                print new_entry
                already_found.update(new_entry)
            else:
                print "else"
                
                result = already_found[common]
                print result
            
            rewrite_thesaurus(already_found, fname)
            
            
            str_amount = str(amount)
            reply = get_reply(common, str_amount, result)
            print reply
        """
    else:
        continue
        
        
    
