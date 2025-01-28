import  runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rt.Runner("Усейн", 10)
        self.runner2 = rt.Runner("Андрей", 9)
        self.runner3 = rt.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for test_key, test_value in cls.all_results.items():
            for key, value in test_value.items():
                result[key] = str(value.name)
            print(result)


    def test_tourne1(self):
        run_1 = rt.Tournament(90, self.runner1, self.runner3)
        res = run_1.start()
        self.all_results[f'test_tourne1 {self.runner1} и {self.runner3}'] = res
        self.assertTrue(list(res.values())[-1].name == str(self.runner3))

    def test_tourne2(self):
        run_2 = rt.Tournament(90, self.runner2, self.runner3)
        res = run_2.start()
        self.all_results[f'test_tourne1 {self.runner2} и {self.runner3}'] = res
        self.assertTrue(list(res.values())[-1] == str(self.runner3))


    def test_tourne3(self):
        run_3 = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        res = run_3.start()
        self.all_results[f'test_tourne1 {self.runner1}, {self.runner2} и {self.runner3}'] = res
        self.assertTrue(list(res.values())[-1] == str(self.runner3))


    if __name__ == '__main__':
        unittest.main()
