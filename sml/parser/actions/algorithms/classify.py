from ...util.grammar import *
from ...util._constants import choice_columns, column
from .classify_algorithms import svm, logistic, forest, bayes, knn

from pyparsing import Literal, oneOf, Optional, Word, OneOrMore, MatchFirst, delimitedList, CaselessLiteral

def define_classify():
    '''
    Algorithm Definition of Classify Keyword
    :returns pyparsing object
    '''

    algoPhrase = (Literal ("algorithm") + Literal("=")).suppress()

    svmd = svm.define_svm()
    logd = logistic.define_logistic()
    forestd = forest.define_forest()
    bayesd = bayes.define_bayes()
    knnd = knn.define_knn()
    algo = algoPhrase + MatchFirst([svmd, logd, forestd, bayesd, knnd]).setResultsName("algorithm")

    #define so that there can be multiple verisions of Classify
    classifyKeyword = oneOf(["Classify", "CLASSIFY"]).setResultsName("classify")

    #Phrases to organize predictor and label column numbers
    predPhrase = (Literal("predictors") + Literal("=")).suppress()
    labelPhrase = (Literal("label") + Literal("=")).suppress()

    #define predictor and label column numbers
    predictorsDef = choice_columns.setResultsName("predictors")
    labelDef = column.setResultsName("label")

    #combine phrases with found column numbers
    preds = predPhrase + predictorsDef
    labels = labelPhrase + labelDef
    
    option = MatchFirst([preds, labels, algo])
    options = delimitedList(option, delim=',')
    classify = classifyKeyword + openParen + Optional(options) + closeParen

    return classify
