import re


class Trie:
    def __init__(self, path=''):
        self.strings = []
        self.dict = {}
        self.count_strings = 0
        self.path = path

    def add_string(self, string):
        trie = self

        for letter in string:
            trie.count_strings += 1
            if letter not in trie.dict:
                trie.dict[letter] = Trie(trie.path + letter)
            trie = trie.dict[letter]
        trie.count_strings += 1
        trie.strings.append(string)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        answer = self.path + ":\n  count_strings:" + str(self.count_strings) + "\n  strings: " + str(
            self.strings) + "\n  dict:"

        def indent(string):
            p = re.compile("^(?!:$)", re.M)
            return p.sub("    ", string)

        for letter in sorted(self.dict.keys()):
            subtrie = self.dict[letter]
            answer = answer + indent("\n" + subtrie.__repr__())
        return answer

    def within_edits(self, string, max_edits):
        # This will be all trie/string pos pairs that we have seen
        found = set()
        # This will be all trie/string pos pairs that we start the next edit with
        start_at_edit = set()

        # At distance 0 we start with the base of the trie can match the start of the string.
        start_at_edit.add((self, 0))
        answers = []
        for edits in range(max_edits + 1):  # 0..max_edits inclusive
            start_at_next_edit = set()
            todo = list(start_at_edit)
            for trie, pos in todo:
                if (trie, pos) not in found:  # Have we processed this?
                    found.add((trie, pos))
                    if pos == len(string):
                        answers.extend(trie.strings)  # ANSWERS FOUND HERE!!!
                        # We have to delete from the other string
                        for next_trie in trie.dict.values():
                            start_at_next_edit.add((next_trie, pos))
                    else:
                        # This string could have an insertion
                        start_at_next_edit.add((trie, pos + 1))
                        for letter, next_trie in trie.dict.items():
                            # We could have had a a deletion in this string
                            start_at_next_edit.add((next_trie, pos))
                            if letter == string[pos]:
                                todo.append((next_trie, pos + 1))  # we matched farther
                            else:
                                # Could have been a substitution
                                start_at_next_edit.add((next_trie, pos + 1))
            start_at_edit = start_at_next_edit
        return answers


if __name__ == '__main__':
    # Sample useage
    product_list = ['Tata Salt Lite 1Kg', 'more Superior/Choice Whole Wheat Chakki Fresh Atta 10 Kg',
                'more Superior/Choice Whole Wheat Chakki Fresh Atta 5 Kg',
                'Aashirvaad Sharbati Select Atta 5 Kg',
                'Aashirvad Salt 1 Kg', 'Catch Black Salt 200 Gm Bottle', 'Tata Salt 1 Kg',
                'More Life Sharbati Atta With Multigrains 5 Kg', 'more Life Sharbati Atta With Multigrains 1 Kg',
                'More Choice Nakuldana 100 g', 'Aashirvaad Superior MP Wheat Atta 1 Kg', 'Selecta Premium Rawa 500 G',
                'Parth Jaggery 950 Gm', 'Parth Jaggery 450 Gm', 'Selecta Premium Rawa 1 Kg',
                'Sprinkle Crystal Salt 1 Kg', 'Aashirvaad Atta With Multigrains 1 Kg',
                'Aashirvaad Atta With Multigrains 5 Kg.', 'Aashirvaad Superior MP Wheat Atta 5 Kg',
                'Aashirvaad Superior MP Wheat Atta 10 Kg', 'Catch Table Salt 100 Gm Sprinkler.',
                'Aashirvaad Sharbati Select Atta 1 Kg', 'more. Selecta Low Sodium Salt 1 Kg',
                'More Choice Ragi Flour 1 kg', 'More Choice Bombay Sooji 1 kg']

    trie = Trie()
    for item in product_list:
        item = item.lower()
        print(item)
        trie.add_string(item)
    # trie.add_string('tatasaltlit')
    # print(trie.path)
    # trie.add_string('bar')
    # trie.add_string('baz')
    # # trie.add_string('kat')
    # trie.add_string('cadbery')
    print(trie.within_edits('dalaaa', 25))
