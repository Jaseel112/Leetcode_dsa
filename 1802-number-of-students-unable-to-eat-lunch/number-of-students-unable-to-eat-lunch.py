class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for sw in sandwiches:
            if sw not in students:
                return len(students)

            students.remove(sw)

        return 0 