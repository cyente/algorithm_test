class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output_list = []
        flag_list = [True for _ in s]
        # s = list(s)
        idx = 0

        def _isvalid(s):
            if len(s) == 0:
                return True
            count_left = 0
            s = list(s)
            for _s in s:
                if _s == '(':
                    count_left += 1
                if _s == ')':
                    if count_left == 0:
                        return False
                    else:
                        count_left -= 1
            if count_left > 0:
                return False
            else:
                return True

        board_list = {s}

        while True:
            final_output = filter(_isvalid, board_list)
            if final_output:
                return final_output
            board_list = {s[0:i] + s[i + 1:] for s in board_list for i in range(len(s)) if s[i] in set(['(', ')'])}





a = Solution()
print(a.removeInvalidParentheses(''))