import random
from nltk.corpus import wordnet

cardioExercise = ["Running", "Swimming", "Cycling", "Rowing", "Walking"]
strengthExercise = ["Bicep Curls", "Plank", "Push-Ups", "Deadlift", "Tricep Dips"]
allExercise = cardioExercise + strengthExercise

dislikedExercise = []
likedExercise = []

def getExercise(exerciseType_p = "all"):

    for exercise in allExercise:
        if exercise not in dislikedExercise:
            likedExercise.append(exercise)

    if (exerciseType_p == "cardio"):
        relevantExercises = []
        for exercise in likedExercise:
            if exercise in cardioExercise:
                relevantExercises.append(exercise)
        if (len(relevantExercises) > 0):
            return random.choice(relevantExercises)

    elif (exerciseType_p == "strength"):
        relevantExercises = []
        for exercise in likedExercise:
            if exercise in strengthExercise:
                relevantExercises.append(exercise)
        if (len(relevantExercises) > 0):
            return random.choice(relevantExercises)

    else:
        relevantExercises = []
        for exercise in likedExercise:
            if exercise in allExercise:
                relevantExercises.append(exercise)
        if (len(relevantExercises) > 0):
            return random.choice(relevantExercises)

    print("Sorry, I couldn't find any exercises you liked")
    if (exerciseType_p == "cardio"):
        return random.choice(cardioExercise)
    elif (exerciseType_p == "strenth"):
        return random.choice(strengthExercise)
    else:
        return random.choice(allExercise) #getExercise
def getSynonym(word_p):
    synonyms = []

    for synonym in wordnet.synsets(word_p):
        for lemma in synonym.lemmas():
            synonyms.append(lemma.name())

    return random.choice(synonyms) #getSynonym


#Program Start
print(getSynonym("Hello").capitalize() + ", how may I help?")

exitState = False
while (exitState == False):
    userInputInterpreted = False

    userInput = input(">")

    #Disliked Exercises
    if ("dislike" in userInput.lower() or (("don't" in userInput.lower() or "dont" in userInput.lower()) and "like" in userInput.lower())):
        userInputInterpreted = True
        exerciseRecognised = False
        for exercise in allExercise:
            if (exercise.lower() in userInput.lower()):
                print("I know that exercise, I'll remember that in the future")
                dislikedExercise.append(exercise)
                exerciseRecognised = True
        if (exerciseRecognised == False):
            print("I'm not sure I know that exercise, but understood")

    if ("exercise" in userInput.lower()):
        userInputInterpreted = True
        #How Much Exercise
        if ("how" and "much" in userInput.lower()):
            secondaryUserInput = input("You should aim to do ~60 Minutes of activity a day\n"
                  + "Have you done any exercise today?"
                  + "\n>")
            if ("no" in secondaryUserInput.lower() or "none" in secondaryUserInput.lower() or "haven't" in userInput.lower() 
                or "havent" in userInput.lower() or ("have" in secondaryUserInput.lower() and "not" in secondaryUserInput.lower())):
                print("Not great, why don't you try " + getExercise().lower())
            elif ("yes" in secondaryUserInput.lower() or "have" in userInput.lower()):
                print(getSynonym("Congratulations").capitalize() +  ", keep it up")
            else:
                print("Sorry, I'm not quite sure I understand")
            
        #Recommend Exercise
        if ("most" in userInput.lower() and "calories" in userInput.lower()):
            print("Why don't you try " + getExercise("cardio").lower())
        elif ("least" in userInput.lower() and "calories" in userInput.lower()):
            print("Why don't you try " + getExercise("strength").lower())
        elif ("recommend" in userInput.lower()):
            print("Why don't you try " + getExercise().lower())

    elif ("sat" in userInput.lower() or "chilled" in userInput.lower() or "slept" in userInput.lower()):
        userInputInterpreted = True
        print(getSynonym("Bad").capitalize() + ", why don't you try " + getExercise().lower())

    #Terminate Program
    elif ("goodbye" in userInput.lower() or "bye" in userInput.lower() or "exit" in userInput.lower()):
        print(getSynonym("Bye").capitalize())
        userInputInterpreted = True
        exitState = True

    elif ("ok" in userInput.lower()):
        userInputInterpreted = True
        print(getSynonym("Good").capitalize())

    if (userInputInterpreted == False):
        print("Sorry, I'm not quite sure I understand")
