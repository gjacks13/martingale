""""""  		  	   		  		 			  		 			     			  	 
"""Assess a betting strategy.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		  		 			  		 			     			  	 
All Rights Reserved  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Template code for CS 4646/7646  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  		 			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		  		 			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  		 			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 			  		 			     			  	 
or edited.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  		 			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		  		 			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 			  		 			     			  	 
GT honor code violation.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
-----do not edit anything above this line---  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		  		 			  		 			     			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		  		 			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import numpy as np  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def author():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT username of the student  		  	   		  		 			  		 			     			  	 
    :rtype: str  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return "gjackson67"  # replace tb34 with your Georgia Tech username.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def gtid():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    :return: The GT ID of the student  		  	   		  		 			  		 			     			  	 
    :rtype: int  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    return 903742455  # replace with your GT ID number  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def get_spin_result(win_prob):  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
    :param win_prob: The probability of winning  		  	   		  		 			  		 			     			  	 
    :type win_prob: float  		  	   		  		 			  		 			     			  	 
    :return: The result of the spin.  		  	   		  		 			  		 			     			  	 
    :rtype: bool  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    result = False  		  	   		  		 			  		 			     			  	 
    if np.random.random() <= win_prob:  		  	   		  		 			  		 			     			  	 
        result = True  		  	   		  		 			  		 			     			  	 
    return result  		  	   		  		 			  		 			     			  	 

def martiangale(win_prob):
    ceiling = 80
    episode_winnings = 0
    while episode_winnings < ceiling:
        won = False
        bet_amount = 1
        while not won:
            # spin with win probablity of landing on black
            won = get_spin_result(win_prob)
            if won == True:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
                
def martiangale_bankroll_contraint(win_prob):
    bankroll = 256
    ceiling = 80
    episode_winnings = 0
    while (episode_winnings < ceiling) and (not bankroll_depleted(bankroll, episode_winnings)):
        won = False
        bet_amount = 1
        while not won:
            # spin with win probablity of landing on black
            won = get_spin_result(win_prob)
            if won == True:
                episode_winnings = episode_winnings + bet_amount
            else:
                # check if episode winnings depleted our bankroll
                if bankroll_depleted(bankroll, episode_winnings):
                    break

                episode_winnings = episode_winnings - bet_amount
                bet_amount = calculate_max_possible_bet(bankroll, episode_winnings, bet_amount)
                
def bankroll_depleted(bankroll, episode_winnings):
    # bet amounts should never put us in debt; so winnings will equal (-1 * bankroll)
    return True if episode_winnings == (-1 * bankroll) else False
    
# def set_bet_amount(bankroll, episode_winnings, bet_amount):
#     max_possible_bet = calculate_max_possible_bet(bankroll, episode_winnings, bet_amount)
#     return max_possible_bet

def calculate_max_possible_bet(bankroll, episode_winnings, desired_bet):
    max_possible_bet = 0
    if episode_winnings <= 0:
        potential_remaining = (bankroll - abs(episode_winnings)) - desired_bet
        remaining = (bankroll - abs(episode_winnings))
        max_possible_bet = desired_bet if potential_remaining > 0 else remaining
    
    if episode_winnings > 0:
        potential_remaining = episode_winnings - desired_bet
        max_possible_bet = desired_bet
        if (potential_remaining < 0) and (bankroll < abs(potential_remaining)):
            # if abs of potential_remaining exceeds winnings and bankroll, max value equals sum of winnings and bankroll
            max_possible_bet = episode_winnings + bankroll
    print("max possible bet: ", max_possible_bet)
    return max_possible_bet		  		 			  		 			     			  	 
 		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
def test_code():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Method to test your code  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    win_prob = 0.60  # set appropriately to the probability of a win, this is the probability of landing on black	
    # 47.37 = .4737 for black?	  	   		  		 			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		  		 			  		 			     			  	 
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		  		 			  		 			     			  	 
    # add your code here to implement the experiments  		  	   		  		 			  		 			     			  	 
  	
    # calculate_max_possible_bet(bankroll, episode_winnings, desired_bet)
    max = calculate_max_possible_bet(256, -254, 80)	  	   		  		 			  		 			     			  	 
    print("final max: ", max)
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    test_code()  	
    