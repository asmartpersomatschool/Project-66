#In this assignment, you will build a Binary Streak Tracker using Python arrays. They will work with binary arrays, count consecutive streaks of 1s, reset the streak when 0 appears, track the best streak, and use same-direction two pointers with a write pointer to move zeros to the end of an array.
class BinaryStreakTracker:
    def __init__(self, data=None):
        self.data = data if data is not None else []
    def get_longest_streak(self) -> int: 
        max_streak = 0
        current_streak = 0
        for num in self.data:
            if num == 1:
                current_streak += 1
                if current_streak > max_streak:
                    max_streak = current_streak
            else:
                current_streak = 0
        return max_streak
    def move_zeroes_to_end(self) -> list:
        write_ptr = 0
        for read_ptr in range(len(self.data)):
            if self.data[read_ptr] != 0:
                self.data[write_ptr], self.data[read_ptr] = self.data[read_ptr], self.data[write_ptr]
                write_ptr += 1
        return self.data
if __name__ == "__main__":
    sample_data = [1,3,7,1,3,1,0,4,0,0,5,7,9,11,23,0.5]
    print(f"Original Array: {sample_data}")
    tracker = BinaryStreakTracker(sample_data)
    best_streak = tracker.get_longest_streak()
    print(f"Longest Streak of 1's: {best_streak}")
    ordered_array = tracker.move_zeroes_to_end()
    print(f"Array after shifting zeroes: {ordered_array}")