# -*- coding: utf-8 -*-
"""
Lowe's Auction Helper -- Designed to gather data about the auction that Lowe's
puts on to benefit charity and give discounts to employees.

TODO:
    -- add auctions output to JSON or csv
    -- add automated protocol for updating bids/items
    -- add functionality to bid on items
    -- add more sophisticated search
    -- add GUI (probs not)
    
    
Created on Tue Jun 24 17:05:37 2014

@author: James Barney
"""

import urllib2
from bs4 import BeautifulSoup


def fetch_auctions(url):
    """
    Fetches the given URL and preps it for BS4 to work magic.
    """
    url = url    
    auction = urllib2.urlopen(url).read()    
    whole_page = BeautifulSoup(auction)
    
    return whole_page
    

def get_headers():
    """
    Gets the column headers from the auction site.
    """
    h = []
    
    headers = whole_page.find_all("th")  
    head = BeautifulSoup(str(headers)).get_text()[1:-1] 
    
    for word in head.split(","):
        h.append( word.lstrip())
        
    return h
          


def get_auctions():
    """
    Gets the text from the ugly HTML tables on the auction site.
    Returns a list of the auctions (RAW)
    """
    tables = whole_page.find_all("tr")   #ind #2 for auctions
    
    all_auctions = []
    for tr in tables[6:]: #skips past the page header with instructions, etc
        td = tr.find_all("td")
        item_info = []
        
        for t in td: 
            t = BeautifulSoup(str(t))
            item_info.append( t.get_text().strip() )

        if len(item_info) == 7:
            all_auctions.append(item_info)
    
    return all_auctions


def join_header_auctions(header, aucts):
    """
    Joins the column headers and the auctions into a dictionary of dictionaries.
    The key for each item/auction is the hashed string of the item itself. 
    """
    joined = dict()
    
    for auction in aucts:
        joined[hash(str(auction))] = dict(zip(header, auction))
        
    return joined
    
    
def search_by_header(header, search):
    """
    Inclusive search for any matching string in the given header's values for all found auctions.
    """
    results = []
    for key in joined.keys():
        try:
            if search in joined[key][header]:
                results.append( joined[key])
        except KeyError:
            print "KeyError: No column of value " + str(header)
            break
            
            
    return results


"""
#advanced search category=None, lot_number=None, item=None, bidder=None, cur_price=None, min_price=None, value=None
def search_auctions(search):
    for key in joined.keys():
        for head in headers:
            print head
            if any(search in d[head] for d in joined[key]):
                return joined[key]
                
            else:
                print "No result found matching that search."
        
def _search_type():
    pass
"""

  

if __name__ == "__main__":
    whole_page = fetch_auctions("file:///C:/Users/James/Documents/GitHub/Free-Time/Lowes%20Auction%20Helper/auction.htm")
    print whole_page.title.string + " Helper by James Barney"         
         
    headers = get_headers()
    auctions = get_auctions()
    joined = join_header_auctions(headers, auctions)
        
    res = search_by_header('Category', 'Building')
    r = search_by_header('Category', 'Chicken')
    k = search_by_header('Chicken', 'Nope')
    
    h = search_by_header('High Bid', '50')



    