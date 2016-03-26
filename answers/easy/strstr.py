class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        return self.rabin(target, source)

    def rabin(self, a, b):
        al, bl = len(a), len(b)
        B = 10  # treat each string is a decimal number
        if al > bl:
            return -1

        t, ah, bh = B**al, 0, 0

        for i in range(al):
            ah = ah * B + ord(a[i])
            bh = bh * B + ord(b[i])

        for i in range(0, bl-al+1):
            if ah == bh:
                return i
            if i + al < bl:
                bh = bh*B + ord(b[i+al]) - ord(b[i]) * t

        return -1
