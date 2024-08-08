def find_indexes(nums: list[int], target: int) -> list[int]:
    hash_map: dict[int, int] = {}

    for i, num in enumerate(nums):
        try:
            return [i, hash_map[target - num]]
        except KeyError:
            hash_map[num] = i

    return []
