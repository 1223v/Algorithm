def solution(participant, completion):
    participant_dict = {}
    completion_dict = {}

    for i in participant:
        if i in participant_dict:
            participant_dict[i] += 1
        else:
            participant_dict[i] = 1

    for i in completion:
        if i in completion_dict:
            completion_dict[i] += 1
        else:
            completion_dict[i] = 1

    for i in participant_dict:
        if participant_dict[i] != completion_dict.get(i, 0):
            return i

