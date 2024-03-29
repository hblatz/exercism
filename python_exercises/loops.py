"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    # student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]  # test
    student_round_scores = []
    for score in student_scores:
        int_score = int(round(score,0))
        student_round_scores.append(int_score)
    
    # print(student_round_scores)  # test
    return student_round_scores


def round_scores2(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    return [round(item) for item in student_scores]


def round_scores3(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    return list(map(round, student_scores))


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    # student_scores = [90,40,55,70,30,25,80,95,38,40]  # test
    fail_count: int = 0
    for score in student_scores:
        if score <= 40:
            fail_count = fail_count + 1

    # print(fail_count)  # test
    return fail_count


def count_failed_students2(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    student_scores = [90,40,55,70,30,25,80,95,38,40]  # test
    # print(sum(1 for score in round_scores2(student_scores) if score <= 40))  # test
    return sum(1 for score in round_scores2(student_scores) if score <= 40)


def count_failed_students3(student_scores):
    """ 
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    return sum(map(lambda n: n <= 40, student_scores))


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    # student_scores =[90,40,55,70,30,68,70,75,83,96]  # test
    # threshold = 75  # test
    best_scores: list = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    
    # print(best_scores)  # test
    return best_scores


def above_threshold3(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    return list(filter(lambda n: n >= threshold, student_scores))


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    # highest = 88  # test
    grade_range = highest - 40
    grade_interval = grade_range/4

    D = 41
    C = int(round(D + grade_interval, 0))
    B = int(round(C + grade_interval, 0))
    A = int(round(B + grade_interval, 0))

    # print([D, C, B, A])  # test
    return [D, C, B, A]


def letter_grades2(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:
 
             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    step = int((highest-40)/4)
    return [41 + step*i for i in range(4)]


def letter_grades3(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    low = 41
    diff = round((highest - low) / 4)
    return [low + diff * i for i in range(4)]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    # student_scores = [100, 99, 90, 84, 66, 53, 47]  # test
    # student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']  # test
    
    rank_name_score = []
    for index, score in enumerate(student_scores):
        student_stats: str = str(index + 1) + ". " + student_names[index] + ": " + str(score)
        rank_name_score.append(student_stats)

    # print(rank_name_score)  # test
    return rank_name_score


def student_ranking2(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    rank = list()
    for i in range(len(student_scores)):
        rank.append("{}. {}: {}".format(i+1,student_names[i],student_scores[i]))
    return rank


def student_ranking3(student_scores, student_names):
    """
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """
    return [
        f"{i + 1}. {student_names[i]}: {student_scores[i]}"
        for i in range(len(student_scores))
    ]


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]  # test
                  
    for student in student_info:
        if student[-1] == 100:
            print(student)  # test
            return student
    return []


def perfect_score3(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    found = []
    for student in student_info:
        if student[1] == 100:
            found = student
            break
    return found
