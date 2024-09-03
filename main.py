from typing import List

def findNumbers(nums: List[int]) -> int:
    count_of_digits: List[int] = [len(str(i)) for i in nums]
    count: int = 0
    for i in count_of_digits:
        if i % 2 == 0:
            count += 1
    return count

def main() -> None:
    print(findNumbers([12,345,2,6,7896]))
    print(findNumbers([555,901,482,1771]))
    
if __name__ == "__main__":
    main()