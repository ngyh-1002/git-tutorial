'''
작동원리: 7월 기온 날씨리스트를 받아서 슬라이딩 윈도우를 코드를 활용해 윈도우 포지션값을 사용자에게 받은 다음,
마지막 윈도우 포지션 값에 최솟값과 최댓값을 보여주는 로직 

함수 maxSlidingWindow(nums, k):
    만약 nums가 비어있다면:
        nums를 반환

    최대값들을 저장할 빈 리스트 results_max 생성

    nums의 길이에서 k를 뺀 후 1을 더한 값까지 반복 (i는 윈도우의 시작 인덱스)
        현재 윈도우 (nums[i]부터 nums[i+k-1]까지)를 가져옴
        현재 윈도우 내의 최대값을 계산
        그 최대값을 results_max 리스트에 추가

    results_max 리스트의 마지막 요소를 반환 (가장 마지막 윈도우의 최대값)
함수 minSlidingWindow(nums, k):
    만약 nums가 비어있다면:
        nums를 반환

    최소값들을 저장할 빈 리스트 results_min 생성

    nums의 길이에서 k를 뺀 후 1을 더한 값까지 반복 (i는 윈도우의 시작 인덱스)
        현재 윈도우 (nums[i]부터 nums[i+k-1]까지)를 가져옴
        현재 윈도우 내의 최솟값을 계산
        그 최솟값을 results_min 리스트에 추가

    results_min 리스트의 마지막 요소를 반환 (가장 마지막 윈도우의 최솟값)
'''
from typing import List

class Solution:
    # 최대 슬라이딩 윈도우 값을 찾는 메서드
    def maxSlidingWindow(self, nums: List[int], k: int):
        # 1. 예외 처리: 입력 리스트가 비어 있으면 빈 리스트를 반환
        if not nums:
            return nums
            
        # 각 윈도우의 최대값을 저장할 리스트 초기화
        r = []
        # 2. 슬라이딩 윈도우 순회:
        # 'i'는 현재 윈도우의 시작 인덱스
        # 'len(nums) - k + 1'은 총 윈도우의 개수 (즉, 'i'가 가질 수 있는 최대 값 + 1)
        # 예를 들어, nums가 10개이고 k가 3이면, i는 0부터 7까지 (10-3+1=8)
        for i in range(len(nums) - k + 1):
            # 3. 현재 윈도우의 최대값 계산 및 저장:
            # nums[i:i + k]는 현재 슬라이딩 윈도우를 나타내는 부분 리스트
            # max() 함수로 이 부분 리스트 내의 최대값을 찾아 'r'에 추가
            r.append(max(nums[i:i + k]))
            
        # 4. 결과 반환: 'r' 리스트의 마지막 요소 (즉, 가장 마지막 슬라이딩 윈도우의 최대값) 반환
        return r[-1] 
    
    # 최소 슬라이딩 윈도우 값을 찾는 메서드
    def minSlidingWindow(self, nums: List[int], k: int):
        # 1. 예외 처리: 입력 리스트가 비어 있으면 빈 리스트를 반환
        if not nums:
            return nums
            
        # 각 윈도우의 최솟값을 저장할 리스트 초기화
        x = [] 
        # 2. 슬라이딩 윈도우 순회: (maxSlidingWindow와 동일)
        for i in range(len(nums) - k + 1):
            # 3. 현재 윈도우의 최솟값 계산 및 저장:
            # nums[i:i + k]는 현재 슬라이딩 윈도우
            # min() 함수로 이 부분 리스트 내의 최솟값을 찾아 'x'에 추가
            x.append(min(nums[i:i + k])) 
            
        # 4. 결과 반환: 'x' 리스트의 마지막 요소 (즉, 가장 마지막 슬라이딩 윈도우의 최솟값) 반환
        return x[-1]

# --- 코드 실행 부분 ---

# Solution 클래스의 인스턴스 생성
sol = Solution()

# 한 달간의 가상 기온 데이터 리스트
one_month_temperature = [
    27, 28, 29, 28, 26, 25, 27, 29, 30, 31,
    30, 29, 28, 27, 28, 29, 30, 31, 32, 31,
    30, 29, 28, 27, 29, 30, 31, 32, 33, 32,
    31
]

# 사용자로부터 기간(k) 입력 받기
k = int(input(" 날씨를 알고싶은 기간을 입력하세요 : "))

# k 값의 유효성 검사: k가 리스트 길이보다 크거나 0 이하인 경우
if k > len(one_month_temperature) or k <= 0:
    print("유효하지 않은 기간입니다. 1부터 31 사이의 숫자를 입력해주세요.")
else:
    # maxSlidingWindow 메서드를 호출하여 최고 기온 계산 및 출력
    print(f'지난 {k}기간 동안 최고기온 : {sol.maxSlidingWindow(one_month_temperature, k)}도')
    # minSlidingWindow 메서드를 호출하여 최저 기온 계산 및 출력
    print(f'지난 {k}기간 동안 최저기온 : {sol.minSlidingWindow(one_month_temperature, k)}도')
