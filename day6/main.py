from collections import deque

# distinct_length = 4   # For part 1
distinct_length = 14  # For part 2

def is_unique(buffer):
    unique = set(buffer)
    return len(unique) == len(buffer)

if __name__ == "__main__":
    buffer = deque()

    with open('input.txt', 'rt') as file:
        line = file.read()

        for i, letter in enumerate(line):
            if i < distinct_length:
                buffer.append(letter)
                if i == distinct_length-1:
                    if is_unique(buffer):
                        num_chars = distinct_length
                        break
            else:
                buffer.popleft()
                buffer.append(letter)
                if is_unique(buffer):
                    num_chars = i + 1
                    break
    
    print("First marker after character:", num_chars)