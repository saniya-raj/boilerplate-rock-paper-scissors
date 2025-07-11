# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], my_history=[], strategy=[0]):
    opponent_history.append(prev_play)

    if prev_play == '':
        return "R"

    if len(my_history) < len(opponent_history) - 1:
        my_history.append("R")

    window_size = 3
    if len(opponent_history) < window_size:
        move = "R"
    else:
        seq = "".join(opponent_history[-window_size:])
        next_move_counts = {"R": 0, "P": 0, "S": 0}

        for i in range(len(opponent_history) - window_size):
            if "".join(opponent_history[i:i+window_size]) == seq:
                next_ = opponent_history[i + window_size]
                if next_ in next_move_counts:
                    next_move_counts[next_] += 1

        # Default to "R" if no pattern found
        predicted_move = max(next_move_counts, key=next_move_counts.get)
        counter = {"R": "P", "P": "S", "S": "R"}
        move = counter[predicted_move]

    my_history.append(move)
    return move
