# test_fuzzyquery.py

from querybuilder.fuzzyquery import FuzzyQuery

def test_fuzzyquery():
    assert (FuzzyQuery("inbox.message", "sponsor")).addSetting("fuzziness", "AUTO").get() == {'query': {'fuzzy': {'inbox.message': {'fuzziness': 'AUTO', 'value': 'sponsor'}}}}

def test_fuzzyquery_advanced():
    fq = FuzzyQuery("inbox.message", "sponsor")
    fq.addSetting("fuzziness", "AUTO")
    fq.addSetting("max_expansions", 50)
    fq.addSetting("prefix_length", 0)
    fq.addSetting("transpositions", True)
    assert fq.get() == {'query': {'fuzzy': {'inbox.message': {'fuzziness': 'AUTO',
                                                'max_expansions': 50,
                                                'prefix_length': 0,
                                                'transpositions': True,
                                                'value': 'sponsor'}}}}