class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if string is None:
            return 0
        for i, c in enumerate(string):
            if c == ' ':
                string.pop(i)
                string.insert(i, '0')
                string.insert(i, '2')
                string.insert(i, '%')
        return len(''.join(string))
