"""
Module for compute_total_price function
Author: Ittigoon
Date: 220427

"""

import numpy as np

def compute_total_price(pth):
    """
    Take gift_cost and retun sum of total price under 25
    Args:
        pth: (str) file path containing gift price
    Return:
        total_price: (float) sum of price under 25
    """
    # read file
    with open(pth,encoding='UTF8') as file_path:
        gift_costs = file_path.read().split('\n')
    # convert string to int
    gift_costs = np.array(gift_costs).astype(int)
    # add cost after tax
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
    return total_price

if __name__ == "__main__":
    TOTAL_PRICE = compute_total_price('gift_costs.txt')
    print(TOTAL_PRICE)
