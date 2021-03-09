"""
Author: Yikan Wang
This file contains a program that takes user name of Github
And prints out the number of commits

I pledge my honor that all HW was done by myself
"""

import unittest

from Repo_Display import get_repo_info


class TestGetRepo(unittest.TestCase):
    def test_normal_behavior(self):
        # test normal case
        expected = [
            'Repo: BulletJournal Number of commits: 30',
            'Repo: cloudComputing Number of commits: 1',
            'Repo: PoolGame Number of commits: 5'

        ]
        self.assertEqual(get_repo_info('wanismvp'), expected)

    def test_edge_case(self):
        # test edge case
        self.assertEqual(get_repo_info('Xander764'), 'Cannot Get Repo From This User')
        self.assertEqual(get_repo_info('wanisnotmvp012'), 'Cannot Get Repo From This User')
        self.assertEqual(get_repo_info('wanisnotmvp123'), 'Cannot Get Repo From This User')


if __name__ == '__main__':
    # edge case
    unittest.main()
