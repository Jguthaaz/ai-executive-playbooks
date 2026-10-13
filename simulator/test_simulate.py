import unittest
from simulate import weighted, compare, load_rows, IMPACT, EFFORT
from pathlib import Path

class DecisionTests(unittest.TestCase):
    def test_known_scores_and_normalization(self):
        self.assertAlmostEqual(weighted([5,4,4,2,5],[25,30,20,10,15]),4.2)
        self.assertAlmostEqual(weighted([5,4,4,2,5],[.25,.30,.20,.10,.15]),4.2)
    def test_invalid_inputs(self):
        for values,weights in [([3],[0]),([3],[-1]),([6],[1]),([float('nan')],[1]),([3],[float('inf')]),([3],[1,2])]:
            with self.assertRaises(ValueError): weighted(values,weights)
    def test_blocked_candidate_cannot_dominate(self):
        rows=[dict(id='x',ready='yes',**{k:3 for k in IMPACT+EFFORT}),dict(id='y',ready='no',**{k:5 for k in IMPACT},**{k:1 for k in EFFORT})]
        result=compare(rows,[1]*5,[1]*5)
        self.assertTrue(result[0]['frontier']);self.assertFalse(result[1]['frontier'])
    def test_sample_matches_published_case(self):
        rows=load_rows(Path(__file__).with_name('opportunities.csv'))
        result=compare(rows,[25,30,20,10,15],[25,25,20,15,15])
        self.assertEqual(len(result),6)
        self.assertAlmostEqual(result[1]['impact'],3.4)
        self.assertAlmostEqual(result[1]['effort'],2.15)

if __name__=='__main__': unittest.main()
