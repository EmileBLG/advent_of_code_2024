from collections import Counter

if __name__ == "__main__":
    filename = "input.txt"
    left_list = []
    right_list = []


    # Read the text file
    with open(filename, "r+") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Sort the lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the distances
    distances = []

    for left, right in zip(left_list, right_list):
        distances.append(abs(left - right))

    print(f"Sum of the distance : {sum(distances)}")


    # Part 2 : similarity score
    count = Counter(right_list)

    similarity_score = 0

    for element in left_list:
        if element in count:
            similarity_score += element * count[element]

    print(f"Similarity score : {similarity_score}")

