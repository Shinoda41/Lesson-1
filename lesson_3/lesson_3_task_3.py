from Adress import Adress
from Mailing import Mailing

box = Mailing(Adress("92108", "San Diego", "Green St", "12", "334"), 
                 Adress("11000", "New York", "1st St", "1", "23"), 
                 "$25.78", "1234567890")

print(f"Letter with the tracking number {box.track} mailed from address: {box.from_adress} to: {box.to_adress}. Cost of mailing: {box.cost}")