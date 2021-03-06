"""
This file contains definition of a District class.
Written by Batmend Batsaikhan.
"""
from Main_Project_Scripts.weekly_mode_tracker import WeeklyModeTracker

class District(WeeklyModeTracker):
    def __init__(self, name, enrollment, school_list, grades):
        self.name = name
        self.size = enrollment
        self.school_list = school_list
        self.learning_modes_for_grades = grades

    def get_district_data(self):
        info = f'District name: {self.name}\nEnrollment for this district: {self.size}\nList of schools:\n'

        for school in self.school_list:
            info += f'  {school.name}\n'

        return info

    def getName(self):
        return self.name;

    def getSize(self):
        return self.size

    def getSchoolList(self):
        return self.school_list

    def getLearningModeWeekly(self):
        return self.learning_modes_for_grades