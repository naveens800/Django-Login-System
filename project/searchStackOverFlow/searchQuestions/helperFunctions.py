from django.core.cache import cache
from stackapi import StackAPI, StackAPIError

# this function handles the data structure.
def handleData(questions):
    dataList = []
    if questions is not None:
        for item in questions['items']:
            Dict = {"title": item.get('title'),
                    "question_id": item.get("question_id"),
                    "is_answered": item.get("is_answered"),
                    "answer_count": item.get("answer_count"),
                    "link": item.get('link')
                    }
            dataList.append(Dict)
    return dataList

# this function check requested data is available or not.
def checkAvailability(data):
    if data==None or len(data)==0:
        return False
    else:
        return True

# this function handle question types.

"""Type of questions users may want's to search as follows:
Questions with ['no-answers','un_answered','featured','related','linked','ids'] """
def handleQuesTypes(quesType, ids=None):
    SITE = StackAPI('stackoverflow')
    if not ids:
        # 'DEFAULT' means simply, get all questions on the site.
        if quesType == 'DEFAULT':
            try:
                # if requested results are not present in cache raise valuerror
                questions = cache.get("SITE.fetch('questions')")
                if questions is None:
                    raise ValueError
            except ValueError:
                try:
                    # as results're not present in cache try to fetch it from api
                    questions = SITE.fetch('questions')
                    # if success, set it into cache 
                    cache.set(
                    f"SITE.fetch('questions')", questions, None)
                    # if not, raise stackAPIError.
                except StackAPIError:
                    questions = None
            return handleData(questions)

        # Get all questions on the site with no answers.
        elif quesType == 'NO_ANS':
            try:
                # if requested results are not present in cache raise valuerror
                questions = cache.get("SITE.fetch('questions/no-answers')")
                if questions is None:
                    raise ValueError
            except ValueError:
                try:
                    # as results're not present in cache try to fetch it from api
                    questions = SITE.fetch('questions/no-answers')
                    # if success, set it into cache 
                    cache.set(
                    f"SITE.fetch('questions/no-answers')", questions, None)
                    # if not, raise stackAPIError.
                except StackAPIError:
                    questions = None
            return handleData(questions)

        # Get all questions the site considers unanswered.
        elif quesType == 'UN_ANS':
            try:
                # if requested results are not present in cache raise valuerror
                questions = cache.get("SITE.fetch('questions/unanswered')")
                if questions is None:
                    raise ValueError
            except ValueError:
                try:
                    # as results're not present in cache try to fetch it from api
                    questions = SITE.fetch('questions/unanswered')
                    # if success, set it into cache 
                    cache.set(
                    f"SITE.fetch('questions/unanswered')", questions, None)
                    # if not, raise stackAPIError.
                except StackAPIError:
                    questions = None
            return handleData(questions)
        
        
        # Get all questions on the site with active bounties.
        elif quesType == 'FEATURED':
            try:
                # if requested results are not present in cache raise valuerror
                questions = cache.get("SITE.fetch('questions/featured')")
                if questions is None:
                    raise ValueError
            except ValueError:
                try:
                    # as results're not present in cache try to fetch it from api
                    questions = SITE.fetch('questions/featured')
                    # if success, set it into cache 
                    cache.set(
                    f"SITE.fetch('questions/featured')", questions, None)
                    # if not, raise stackAPIError.
                except StackAPIError:
                    questions = None
            return handleData(questions)
    
    else:
        ids = [int(i) for i in ids.split() if i.isdigit()]
        print(ids)
        # 'DEFAULT' means simply, get all questions on the site.
        if quesType == 'DEFAULT':
            try:
                # if requested results are not present in cache raise valuerror
                questions = cache.get(f"SITE.fetch('questions', ids = {ids})")
                if questions is None:
                    raise ValueError
            except ValueError:
                try:
                    # as results're not present in cache try to fetch it from api
                    questions = SITE.fetch('questions', ids = ids)
                    # if success, set it into cache 
                    cache.set(
                    f"SITE.fetch('questions', ids = {ids})", questions, None)
                    # if not, raise stackAPIError.
                except StackAPIError:
                    questions = None
            return handleData(questions)

        # Get the questions that are related to the
        # questions identified by a set of ids.
        elif quesType == 'RELATED':
            try:
               # if requested results are not present in cache raise valuerror
                questions = cache.get(
                    f"SITE.fetch('questions/related', ids = {ids})")
                if questions is None:
                    raise ValueError
            except ValueError:
                try:
                    # as results're not present in cache try to fetch it from api
                    questions = SITE.fetch('questions/related', ids = ids)
                    # if success, set it into cache 
                    cache.set(
                    f"SITE.fetch('questions/related', ids = {ids})", questions, None)
                    # if not, raise stackAPIError.
                except StackAPIError:
                    questions = None
            return handleData(questions)

        # Get the questions that link to the questions
        # identified by a set of ids
        elif quesType == 'LINKED':
            try:
                # if requested results are not present in cache raise valuerror
                questions = cache.get(
                    f"SITE.fetch('questions/linked', ids = {ids})")
                if questions is None:
                    raise ValueError
            except ValueError:
                try:
                    # as results're not present in cache try to fetch it from api
                    questions = SITE.fetch('questions/linked', ids = ids)
                    # if success, set it into cache 
                    cache.set(
                    f"SITE.fetch('questions/linked', ids = {ids})", questions, None)
                    # if not, raise stackAPIError.
                except StackAPIError:
                    questions = None
            return handleData(questions)