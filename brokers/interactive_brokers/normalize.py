from database import Scraped, Historical

symbols = [(record.symbol) for record in Scraped.select()]