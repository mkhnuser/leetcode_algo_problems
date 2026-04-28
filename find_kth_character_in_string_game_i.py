import itertools as it
import string


class Solution:
    def kthCharacter(self, k: int) -> str:
        alphabet = string.ascii_lowercase
        word = "a"
        counter = it.count(start=0, step=1)
        # NOTE: Index and reverse index, essentially.
        char_to_index_mapping = {char: next(counter) for char in alphabet}
        counter = it.count(start=0, step=1)
        index_to_char_mapping = {next(counter): char for char in alphabet}

        while len(word) < k:
            to_be_appended = ""

            for char in word:
                char_index = char_to_index_mapping[char]
                char_index += 1
                char_to_be_appended = index_to_char_mapping[char_index % len(alphabet)]
                to_be_appended += char_to_be_appended

            word += to_be_appended

        return word[k - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.kthCharacter(5))
    print(solution.kthCharacter(10))
