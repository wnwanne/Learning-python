# TODO:
#  1. write a function to calculate
#  the difference between two scores.
#  2. write a function that determines
#  who's winning.


def diff(score1, score2):
    diff_score = score2 - score1
    return diff_score


def who_wins(scores):
    team_names = []  # could use list(scores)
    for tn in scores:
        team_names.append(tn)

    if scores[team_names[0]] > scores[team_names[1]]:
        print(str(team_names[0]) + " Wins!")
    elif scores[team_names[0]] == scores[team_names[1]]:
        print("Its a tie!")
    else:
        print(str(team_names[1]) + " Wins!")


score1 = 10
score2 = 12
team_name1 = 'cavs'
team_name2 = 'celtics'

scores = {
    team_name1: score1,
    team_name2: score2
}

print(diff(score1, score2))
who_wins(scores)

