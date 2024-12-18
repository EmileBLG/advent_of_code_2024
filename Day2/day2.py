from typing import List

def verify_decreasing(report: List[int]) -> bool:
    for i in range(len(report) -1):
        difference = report[i] - report[i + 1]
        if difference < 1:
            return False
        if difference > 3:
            return False
    return True
    

def verify_increasing(report: List[int]) -> bool:
    for i in range(len(report) -1):
        difference = report[i + 1] - report[i]
        if difference < 1:
            return False
        if difference > 3:
            return False
    return True

def verify_report(report: List[int]) -> bool:
    result = None
    if (report[0] - report[1]) > 0:
        result = verify_decreasing(report)
    else:
        result = verify_increasing(report)

    # Verify problem dampener
    if result == False:
        dampener_result = None
        for i in range(len(report)):
            temp_report = report.copy()
            temp_report.pop(i)
            print(temp_report)
            if (temp_report[0] - temp_report[1]) > 0:
                dampener_result = verify_decreasing(temp_report)
            else:
                dampener_result = verify_increasing(temp_report)
            if dampener_result == True:
                return True
        return False

    return True
    

if __name__ == "__main__":

    test_reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]]

    # Read input file
    filename = "input.txt"
    reports = []

    with open(filename, "r+") as file:
        for line in file:
            numbers = line.split()
            level = list(map(int, numbers))
            reports.append(level)

    # Verify reports
    safe_reports = 0
    for report in reports:
        if verify_report(report):
            safe_reports += 1

    print(safe_reports)

    # index = 27
    # print(reports[index])
    # print(verify_report(reports[index]))
