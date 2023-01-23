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
  		  	   		  		 			  		 			     			  	 
Student Name: Garvey Jackson (replace with your name)  		  	   		  		 			  		 			     			  	 
GT User ID: gjackson67 (replace with your User ID)  		  	   		  		 			  		 			     			  	 
GT ID: 903742455 (replace with your GT ID)  		  	   		  		 			  		 			     			  	 
"""  		  	   		  		 			  		 			     			  	 
  		  	   		  		 			  		 			     			  	 
import numpy as np
# import matplotlib.pyplot as plt
  		  	   		  		 			  		 			     			  	 
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

def martingale(win_prob, max_spins = 1000):
    print("max_spins: ", max_spins)
    winnings = np.zeros(max_spins + 1, dtype=np.int_)
    print("original winnings: ", winnings)
    curr_spin = 0
    ceiling = 80
    episode_winnings = 0
    while (episode_winnings < ceiling) and (curr_spin < max_spins):
        won = False
        bet_amount = 1
        while not won and (curr_spin < max_spins):
            won = get_spin_result(win_prob)
            curr_spin += 1
            print("curr_spin: ", curr_spin)
            if won == True:
                episode_winnings = episode_winnings + bet_amount
                winnings[curr_spin] = bet_amount
                print("new winnings: ", winnings)
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2
                winnings[curr_spin] = bet_amount * -1
                print("new winnings: ", winnings)
    return winnings
                
def martingale_bankroll_constraint(win_prob, max_spins = 1000):
    winnings = np.zeros(max_spins + 1)
    curr_spin = 0
    bankroll = 256
    ceiling = 80
    episode_winnings = 0
    while (episode_winnings < ceiling) and (not bankroll_depleted(bankroll, episode_winnings)) and (curr_spin < max_spins):
        won = False
        bet_amount = 1
        while not won and (not bankroll_depleted(bankroll, episode_winnings)) and (curr_spin < max_spins):
            won = get_spin_result(win_prob)
            curr_spin += 1
            if won == True:
                episode_winnings = episode_winnings + bet_amount
                winnings[curr_spin] = bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = calculate_max_possible_bet(bankroll, episode_winnings, bet_amount)
                winnings[curr_spin] = bet_amount * -1
    return winnings
                
def bankroll_depleted(bankroll, episode_winnings):
    # bet amounts should never put us in debt; so winnings will equal (-1 * bankroll)
    return True if episode_winnings == (-1 * bankroll) else False

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
    return max_possible_bet   	  		 			  		 			     			  	 
	  		 			  		 			     			  	 
def test_code():  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    Method to test your code  		  	   		  		 			  		 			     			  	 
    """  		  	   		  		 			  		 			     			  	 
    win_prob = .474  # set appropriately to the probability of a win, this is the probability of landing on black	
	  	   		  		 			  		 			     			  	 
    np.random.seed(gtid())  # do this only once  		  	   		  		 			  		 			     			  	 
    print(get_spin_result(win_prob))  # test the roulette spin  
    # martingale(win_prob)		  	   		  		 			  		 			     			  	 
    # add your code here to implement the experiments
    
    spins_per_episode = 1000
    
    # figure 1
    episode_count = 2
    experiment_1_array_a = np.zeros((episode_count,4))
    print("origininal experiment_1_array_a: ", experiment_1_array_a)
    print("origininal experiment_1_array_a index 0: ", experiment_1_array_a[0])
    print("origininal experiment_1_array_a index 1: ", experiment_1_array_a[1])
    for i in range(episode_count):
        print("i: ", i)
        arr = martingale(win_prob, 3)
        print("appending to final: ", arr)
        experiment_1_array_a[i] = arr
        print("updated experiment_1_array_a: ", experiment_1_array_a)

    print("final experiment_1_array_a: ", experiment_1_array_a)
    # print("final arr: ", arr)
  		  	   		  		 			  		 			     			  	 
if __name__ == "__main__":  		  	   		  		 			  		 			     			  	 
    test_code()  	
    
