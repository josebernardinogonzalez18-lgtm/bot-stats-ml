import unittest
import pandas as pd

class TestPreprocessing(unittest.TestCase):
    def test_goal_diff_calculation(self):
        df = pd.DataFrame({'goals_home': [3, 1], 'goals_away': [1, 1]})
        df['goal_diff'] = df['goals_home'] - df['goals_away']
        self.assertEqual(df['goal_diff'].iloc[0], 2)
        self.assertEqual(df['goal_diff'].iloc[1], 0)

if __name__ == '__main__':
    unittest.main()