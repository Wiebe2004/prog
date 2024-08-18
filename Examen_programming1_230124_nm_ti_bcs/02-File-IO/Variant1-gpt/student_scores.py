def calculate_total_score(scores):
    total_scores = {}
    for name,grades in scores.items():
        total_scores[name] = sum(grades)
    return total_scores


# scores = {
#     "Alice": [85, 78, 88],    # Alice's scores in Math, English, Chemistry
#     "Bob": [90, 88],          # Bob's scores in Chemistry, Math
#     "Charlie": [92, 85]       # Charlie's scores in Math, Chemistry
# }

# print(calculate_total_score(scores))

# total_scores = {"Alice": 251, "Bob": 251, "Charlie": 177}


def highest_scorer(scores):
    lijst = []
    hoogste = max(scores.values())
    for name,score in scores.items():
        # score = int(score)
        if score == hoogste:
            lijst.append(name)
            hoogste = score
    return lijst


# print(highest_scorer(total_scores))

def calculate_student_stats(input):
    with open(input) as file:
        doc = file.readlines()

    scores = {}

    for line in doc:
        name,subject,score = line.split(', ')
        score = int(score)
        if name not in scores:
            scores[name] = [score]
        else:
            scores[name].append(score)


    total_score = calculate_total_score(scores)
    highest_score = highest_scorer(total_score)

    with open('student_results.txt', 'w', encoding='utf-8') as outFile:
        outFile.write(f"Total number of student: {len(scores)}\n")
        outFile.write(f"Highest score: {max(total_score.values())}\n")
        outFile.write(f"Highest scorer(s):\n")
        for student in highest_score:
            outFile.write(f"\t{student}\n")

calculate_student_stats('scores.txt')