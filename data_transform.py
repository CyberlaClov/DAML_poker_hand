import pandas as pd


def linear_transform(data):
    """
    Transforms the input DataFrame by counting the occurrences of each rank and suit.

    Parameters:
    data (pd.DataFrame): The input DataFrame containing card data with columns for suits and ranks.

    Returns:
    pd.DataFrame: A DataFrame with the counts of each rank (1 to 13) and each suit (1 hearts, 2 spades, 3 diamonds, 4 clubs).
    """
    transformed_data = pd.DataFrame()

    suit_columns = ["S1", "S2", "S3", "S4", "S5"]
    rank_columns = ["C1", "C2", "C3", "C4", "C5"]

    # Count the number of times each rank (1 to 13) appears in the rank columns
    for rank in range(1, 14):
        transformed_data[f"rank_{rank}"] = (data[rank_columns] == rank).sum(axis=1)

    # Count the number of times each color (1 hearts, 2 spades, 3 diamonds, 4 clubs) appears in the suit columns
    for color in range(1, 5):
        transformed_data[f"color_{color}"] = (data[suit_columns] == color).sum(axis=1)

    return transformed_data
