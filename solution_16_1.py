""" Count the number of score combinations """

POSSIBLE_POINTS = [7, 3, 2]

def count_number_of_combinations_slow(final_score, points_per_play=POSSIBLE_POINTS):
    """ Exponential in number of differently scoring plays! """

    number_of_combinations = 0

    # just one type of play
    if len(points_per_play) == 1:
        if final_score % points_per_play[0] == 0:
            return 1
        else:
            return 0

    for i in range(final_score // points_per_play[0] + 1):
        # count how many solutions there are with i of score 0
        remaining_score = final_score - i * points_per_play[0]

        number_of_combinations += count_number_of_combinations(remaining_score, points_per_play[1:])

    return number_of_combinations



def count_number_of_combinations(final_score, points_per_play=POSSIBLE_POINTS):
    """
    Uses DP to make it O(sn) in both time and space. 
    """

    num_combinations_for_score = [[1] + [0] * final_score for _ in points_per_play]

    for i in range(len(points_per_play)):
        for j in range(1, final_score + 1):
            without_this_play = (num_combinations_for_score[i - 1][j]
            if i >= 1 else 0)
            with_this_play = (
                num_combinations_for_score[i][j - points_per_play[i]]
                if j >= points_per_play[i] else 0
            )
            num_combinations_for_score[i][j] = (without_this_play + with_this_play)

    return num_combinations_for_score[-1][-1]