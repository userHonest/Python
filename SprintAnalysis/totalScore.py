import matplotlib.pyplot as plt

def main(survey_responses):
    # Calculate total score and average
    total_score = sum(score for person_responses in survey_responses for score in person_responses)
    average_score = total_score / (len(survey_responses) * len(survey_responses[0]))

    # Round the average score to 1 decimal place
    average_score = round(average_score, 1)

    return total_score, average_score


## List with the scores from the survey
survey_responses = [
    [4.6, 4.3, 4.2, 4.2]  

]

total_score, average_score = main(survey_responses)

# Creating a bar chart for the average score
plt.bar("Average Score", average_score, color = "#56B4E9")
plt.ylim(0,5)
plt.ylabel('Score')
plt.title('Team satisfaction during the whole project')
plt.text("Average Score", average_score/2, str(average_score), ha='center', va='bottom', fontsize=25, color='black')

plt.show()

print("Total score:", total_score)
print("Average score:", average_score)
