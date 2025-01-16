import runner
import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        n = Runner('Valera')
        for i in range(10):
            n.walk()
        self.assertEqual(n.distance, 50)

    def test_run(self):
        n = Runner('Valera')
        for i in range(10):
            n.run()
        self.assertEqual(n.distance, 100)

    def test_challenge(self):
        n = Runner('Valera')
        n1 = Runner('Elena')
        for i in range(10):
            n.walk()
            n1.run()
        self.assertNotEqual(n.distance, n1.distance)


if __name__ == '__main__':
    unittest.main()
