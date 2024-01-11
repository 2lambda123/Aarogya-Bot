import unittest

from answer_search import AnswerSearcher


class TestAnswerSearcher(unittest.TestCase):
    def setUp(self):
        self.answer_searcher = AnswerSearcher()

    def test_search_main(self):
        # Test case for disease_symptom question type
        sqls = [
            {
                'question_type': 'disease_symptom',
                'sql': ['MATCH (n)-[r:HAS_SYMPTOM]->(m) RETURN n.name, m.name']
            }
        ]
        expected_result = ['The symptoms of Disease1 include: Symptom1, Symptom2']
        self.assertEqual(self.answer_searcher.search_main(sqls), expected_result)

        # Test case for empty answers
        sqls = [
            {
                'question_type': 'disease_symptom',
                'sql': ['MATCH (n)-[r:HAS_SYMPTOM]->(m) RETURN n.name, m.name']
            }
        ]
        expected_result = []
        self.assertEqual(self.answer_searcher.search_main(sqls), expected_result)

    def test_answer_prettify(self):
        # Test case for disease_symptom question type
        question_type = 'disease_symptom'
        answers = [
            {'n.name': 'Disease1', 'm.name': 'Symptom1'},
            {'n.name': 'Disease1', 'm.name': 'Symptom2'},
            {'n.name': 'Disease2', 'm.name': 'Symptom3'}
        ]
        expected_result = 'The symptoms of Disease1 include: Symptom1, Symptom2'
        self.assertEqual(self.answer_searcher.answer_prettify(question_type, answers), expected_result)

        # Test case for empty answers
        question_type = 'disease_symptom'
        answers = []
        expected_result = ''
        self.assertEqual(self.answer_searcher.answer_prettify(question_type, answers), expected_result)

if __name__ == '__main__':
    unittest.main()
