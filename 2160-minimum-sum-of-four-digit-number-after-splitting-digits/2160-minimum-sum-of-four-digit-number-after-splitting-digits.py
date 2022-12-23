class Solution:
    def minimumSum(self, num: int) -> int:
        
        # 합이 가장 작은 조건: 두 자리 + 두 자리
        # 십의 자리는 작은 수가 와야 하고 일의 자리에 큰 수가 오도록 한다
        num_list = [int(i) for i in str(num)]
        num_list.sort()
        
        return num_list[0] * 10 + num_list[1] * 10 + num_list[2] + num_list[3]