def main(input):
    combo = 0
    deep = 0
    max_value = 0

    for i in range(len(input)):
        if input[i] == 0:
            max_value = max(max_value, combo * deep)
            deep = 0
            combo = 0
        else:
            combo += 1
            deep = max(deep, input[i])

    max_value = max(max_value, combo * deep)
    print(max_value)


# Example usage
input_data = [1, 2, 0, 3, 4, 0, 5, 6]  # Replace with your input
main(input_data)
