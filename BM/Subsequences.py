def getSubseq(word: str) -> list[str]:
    res, n = [], len(word)                          # Initialise a list

    for i in range(2 ** n):                         # Iterate through
        sub, j = "", 0                              # Initialise an empty string and a pointer
        while i:                                    # While the current index is non-zero
            sub += word[j] if i & 1 else ''         # Add the character at pointer to the string if set-bit
            i >>= 1                                 # Right-shift the index value
            j += 1                                  # Increment the pointer
        res.append(sub)                             # Append the string to the list

    return res                                      # Return the result
