# test_dictionary_bst.py

import unittest
from dictionary_bst import DictionaryBST


class TestDictionaryBST(unittest.TestCase):

    def setUp(self):
        self.dictionary = DictionaryBST()

    def test_insert_and_search(self):
        self.dictionary.insert("banana", "A yellow tropical fruit.")
        self.dictionary.insert("apple", "A fruit that grows on trees.")
        self.dictionary.insert("cherry", "A small, round, red fruit.")

        self.assertEqual(self.dictionary.search("banana"), "A yellow tropical fruit.")
        self.assertEqual(self.dictionary.search("apple"), "A fruit that grows on trees.")
        self.assertEqual(self.dictionary.search("cherry"), "A small, round, red fruit.")
        self.assertIsNone(self.dictionary.search("pear"))  # not inserted

    def test_duplicate_insertion_updates_meaning(self):
        self.dictionary.insert("apple", "A tech company.")
        self.assertEqual(self.dictionary.search("apple"), "A tech company.")

        self.dictionary.insert("apple", "A fruit that grows on trees.")
        self.assertEqual(self.dictionary.search("apple"), "A fruit that grows on trees.")

    def test_print_alphabetical_order(self):
        entries = {
            "banana": "A yellow tropical fruit.",
            "apple": "A fruit that grows on trees.",
            "cherry": "A small, round, red fruit."
        }

        for word, meaning in entries.items():
            self.dictionary.insert(word, meaning)

        sorted_entries = self.dictionary.print_alphabetical()

        expected = [
            ("apple", "A fruit that grows on trees."),
            ("banana", "A yellow tropical fruit."),
            ("cherry", "A small, round, red fruit.")
        ]

        self.assertEqual(sorted_entries, expected)

    def test_init_with_entries_dict(self):
        entries = {
            "grape": "A small, sweet fruit.",
            "fig": "A soft fruit with many seeds.",
            "date": "A sweet fruit from the date palm."
        }

        dictionary = DictionaryBST(entries)

        self.assertEqual(dictionary.search("grape"), "A small, sweet fruit.")
        self.assertEqual(dictionary.search("fig"), "A soft fruit with many seeds.")
        self.assertEqual(dictionary.search("date"), "A sweet fruit from the date palm.")


if __name__ == "__main__":
    unittest.main()