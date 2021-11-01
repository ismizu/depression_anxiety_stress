#----- Contains the basic functions used throughout the notebook -----#
import pickle

#--- Retrieve Survey Text ---#
def survey_key(question_code):
    
    '''Input question number
    Outputs question text'''
    
    #Load dict of survey keys/values
    load_survey_questions = open('pickled_data/survey_questions.pickle','rb')
    survey_questions = pickle.load(load_survey_questions)
    load_survey_questions.close()
    
    question_text = survey_questions[question_code]
    
    return question_text