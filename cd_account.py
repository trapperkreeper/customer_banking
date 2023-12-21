"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cd_interest_earned = 0.00
    cd_account = Account(balance, cd_interest_earned)
    # Calculate interest earned
    # ADD YOUR CODE HERE
    
    cd_interest_earned = balance * (interest_rate/100 * months/12)

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE    
    cd_balance = balance + cd_interest_earned
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_balance(cd_balance)
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    cd_account.set_interest(cd_interest_earned)

    # Return the updated balance and interest earned.
    return  cd_account.balance, cd_account.interest
