# Edward Tseng
# 06/19/15


class Anagrams(object):
    def __init__(self):
        self.filename = '/usr/share/dict/words'

    def run(self):

        dictionary = self.read_file(self.filename)

        anagram_buckets = self.bucket_sort(dictionary)

        filtered_anagrams = self.filter(anagram_buckets)

        self.print_anagrams(filtered_anagrams)

    # Returns a list of words of length at least 4
    def read_file(self, filename):
        return [line.lower().strip() for line in open(filename) if len(line.strip()) >= 4]

    # Groups anagrams in buckets
    def bucket_sort(self, arr):
        bucket = {}

        for word in arr:

            anagram = self.sort_chars(word)

            if anagram in bucket:
                if word not in bucket[anagram]:
                    bucket[anagram].append(word)
            else:
                bucket[anagram] = [word]

        return bucket.values()

    # Converts a word into a sorted char string
    def sort_chars(self, string):
        st = list(string)
        st.sort()
        return "".join(st)

    # Includes only buckets with as many anagrams as there are letters
    def filter(self, buckets):
        return [bucket for bucket in buckets if len(bucket) >= len(bucket[0])]

    def print_anagrams(self, buckets):
        for bucket in buckets:
            print(", ".join(bucket))

if __name__ == "__main__":
    a = Anagrams()
    a.run()
