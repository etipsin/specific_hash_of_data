from unittest import TestCase
from specific_hash import SpecificHash, DumpsError


class TestMyHash(TestCase):
    def test_data_is_list(self):
        h = SpecificHash([1, 2, 3, 4])
        self.assertEqual(len(h.get_hash()), 3)

    def test_data_is_short_list(self):
        h = SpecificHash([1])
        self.assertEqual(len(h.get_hash()), 3)

    def test_data_is_dict(self):
        h = SpecificHash({1: 2, 3: 4})
        self.assertEqual(len(h.get_hash()), 3)

    def test_data_is_string(self):
        h = SpecificHash("testtest")
        self.assertEqual(len(h.get_hash()), 3)

    def test_data_is_short_string(self):
        h = SpecificHash("1")
        self.assertEqual(len(h.get_hash()), 3)

    def test_data_is_number(self):
        h = SpecificHash(79032823230)
        self.assertEqual(len(h.get_hash()), 3)

    def test_data_is_small_number(self):
        h = SpecificHash(1)
        self.assertEqual(len(h.get_hash()), 3)

    def test_data_is_object_with_dumps(self):
        class Box:
            def __init__(self):
                pass

            @staticmethod
            def dumps():
                return "This is Box"

        h = SpecificHash(Box())
        self.assertEqual(len(h.get_hash()), 3)

    def test_data_is_object_without_dumps(self):
        class Box:
            def __init__(self):
                pass

        with self.assertRaises(DumpsError):
            SpecificHash(Box())

    def test_count_options_data_is_list(self):
        count_options = 5
        h = SpecificHash([1, 2, 3, 4], count_options=count_options)
        self.assertEqual(len(h.get_hash()), count_options)

    def test_count_options_data_is_dict(self):
        count_options = 7
        h = SpecificHash({1: 2, 3: 4}, count_options=count_options)
        self.assertEqual(len(h.get_hash()), count_options)

    def test_count_options_data_is_string(self):
        count_options = 9
        h = SpecificHash({1: 2, 3: 4}, count_options=count_options)
        self.assertEqual(len(h.get_hash()), count_options)

    def test_count_options_data_is_number(self):
        count_options = 11
        h = SpecificHash({1: 2, 3: 4}, count_options=count_options)
        self.assertEqual(len(h.get_hash()), count_options)

    def test_separator(self):
        separator = ";"
        h = SpecificHash([1, 2, 3, 4, 5, 6, 7, 8], separator=separator)
        self.assertTrue(all(separator in x for x in h.get_hash()))

    def test_same_result_for_same_list_data(self):
        h = SpecificHash([744, 23, 23, 32])
        self.assertEqual(h.get_hash(), ['Kanawari-Azophenyl-Iodine', 'Primi-Resorcine-Soudge',
                                             'Postorder-Lingeries-Gavelkinder'])

    def test_same_result_for_same_dict_data(self):
        h = SpecificHash({"test": 123, "new_test": 777}, separator="*", count_options=7)
        self.assertEqual(h.get_hash(), ['Cackler*Exoascaceae*Incourteously', 'Supergrant*Atmosphereless*Octogynia',
                                        'Wobblier*Beasthood*Kantharos', 'Bennettitales*Potassamide*Congrio',
                                        'Bourgeoise*Nonscandalous*Diastase', 'Dispossed*Ailantery*Youthes',
                                        'Ducato*Pelvigraph*Overspent'])

    def test_same_result_for_same_string_data(self):
        h = SpecificHash("It is my test!!!", count_options=4)
        self.assertEqual(h.get_hash(), ['Sashoon-Branchiocardiac-Sledgemeter', 'Upclimber-Succeedingly-Caulinary',
                                        'Schizopelmous-Overjacket-Shamim', 'Gaincall-Prearranged-Liniments'])

    def test_same_result_for_same_number_data(self):
        h = SpecificHash(41277321, count_options=4)
        self.assertEqual(h.get_hash(), ['Concausal-Cheesecake-Schoolgirlish', 'Subsales-Blesboks-Genealogizer',
                                        'Weapemeoc-Cremationist-Tourneyed', 'Lenticulate-Kibbles-Hectorean'])

    def test_same_result_for_same_object_data(self):
        class Passport:
            @staticmethod
            def dumps():
                return "769338723"

        h = SpecificHash(Passport())
        self.assertEqual(h.get_hash(), ['Martialed-Ekasilicon-Overpsychologized', 'Zaque-Zoogony-Meteorite',
                                             'Planigram-Orchestic-Uniphaser'])