import logging

import crickbetapi.api.resources as r
import crickbetpai.database.core as db

logger = logging.getLogger(__name__)

class BetValidator:

    def __init__(self):
        pass

    def validate(self, update, team, bet_amount):
        message = update.message
        print(message.date)
        # Get match intance and call for validate
        live_matchs = r.Match().get_live_matchs()
        
        # get user info if user does not exits create one
        # user = db.session.get_user(
        user = None

        if team in live_matchs:
            match = live_match[team]
            match.validate(user, team, bet_amount, time)
        else:
            print('no match for {} team.'.format(team))





