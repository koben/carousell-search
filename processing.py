from pycarousell import CarousellSearch
import arrow
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.orm import sessionmaker
#import chatbot as robot
from myconfigurations import RESULTS_COUNT
import re

# product url is
# https://www.carousell.com.my/p/$listingId

Base = declarative_base()

class CarousellListing(Base):
    __tablename__ = 'itemlistings'
    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer)
    seller = Column(String)
    title = Column(String)
    currency_symbol = Column(String)
    price = Column(Float)
    time = Column(String)

engine = create_engine('sqlite:///searchListings.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def find_stuff(search_query):
    my_want = CarousellSearch(search_query, results=RESULTS_COUNT)
    results = my_want.send_request()

    for r in results:
        listingId = r['listingCard']['id']
        timeCreated = r['listingCard']['aboveFold'][0]['timestampContent']['seconds']['low']
        seller = r['listingCard']['seller']['username']
        title = r['listingCard']['belowFold'][0]['stringContent']
        price = r['listingCard']['belowFold'][1]['stringContent']
        price_cur = 'RM'
        price_str = re.sub(price_cur, '', price)
        if "," in price_str:
            price_str = re.sub(',', '', price_str)
        price_float = float(price_str)
        #skip results without query in listing title
        if search_query not in (title.lower()):
            continue
        #check if listing is in DB already
        check = (session.query(CarousellListing).filter_by(listing_id=listingId).first())
        #if it is not in DB
        if check is None:
            listing = CarousellListing(
                listing_id = listingId,
                seller = seller,
                title = title,
                currency_symbol = price_cur,
                price = price_float,
                time = arrow.get(timeCreated).format('DD/MM/YYYY HH:MM')
            )
            session.add(listing)
            session.commit()
            line_item = (seller, title, price_float,
                        arrow.get(timeCreated).format('DD/MM/YYYY HH:MM'))
            #robot.post_message(', '.join(line_item))
        print(line_item)
        print('https://www.carousell.com.my/p/%s' % listingId)
    return
