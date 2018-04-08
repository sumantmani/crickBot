import logging

from crickbetapi.config import config
import crickbetapi.constants as c

logger = logging.getLogger(__name__)


class BetParser:

    def __init__(self):
        pass

    def parse(self, update):
        if not update:
            return False
        
        # a bet is in form or {team bet_point} or {bet_point team}
        is_bet = False
        team = None
        bet_amount = None
        try:
            m = update.message.text
            m = m.lstrip().rstrip()
            m = m.split(' ')
            
            if len(m) == 2:
                if m[1].upper() in teams:
                    m[0], m[1] = m[1], m[0]

                if m[0] and m[0].upper() in c.all_teams and m[1].isdigit():
                    is_bet = True
                    team = m[0].upper()
                    bet_amount = int(m[1])

        except Exception as e:
            print(e)
        
        if is_bet:
            # class handler
            # we have update, team, bet_amount
            # validate bet
            print(team, bet_amount)
            

        return is_bet


class BetValidator:

    def __init__(self):
        self.todays_teams = ['kkr', 'rcb']
        self.team_to_match = {
            'kkr': 'KKR vs RCB',
            'rcb': 'KKR vs RCB',
        }

    def validate(self, udpate, team, bet_amount):
        if team not in self.todays_teams:
            # invalid request
            pass
        match = self.team_to_match[team]

        print(match)

