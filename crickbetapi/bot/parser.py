import logging
import re

from crickbetapi.config import config
from validator import BetValidator
import crickbetapi.constants as c


logger = logging.getLogger(__name__)


class BetParser:

    def __init__(self):
        pass

    def parse(self, update):
        if not update:
            return False
        
        is_bet = False
        team = None
        bet_amount = None
        try:
            m = update.message.text
            m = m.lstrip().rstrip()
            m = m.split(' ')
            print(m)

            if len(m) == 1:
                m = self.split_team_bet(m[0])

            if len(m) == 2:
                if m[1].upper() in c.all_teams:
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
            BetValidator().validate(update, team, bet_amount)

        return is_bet

    def split_team_bet(self, text):
        if not text:
            return []

        text = text.upper()

        if text.startswith(tuple(c.all_teams)):
            match = re.match(r"([a-zA-Z]+)([0-9]+)", text, re.I)
        elif text.endswith(tuple(c.all_teams)):
            match = re.match(r"([0-9]+)([a-zA-Z]+)", text, re.I)

        if match:
            items = match.groups()
            print(items)

        return list(items)


