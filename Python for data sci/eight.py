def is_sublist(main_list, sub_list):
    n, m = len(main_list), len(sub_list)
    
    # empty sublist is always contained
    if m == 0:
        return True
    
    for i in range(n - m + 1):   # slide window
        if main_list[i:i+m] == sub_list:
            return True
    return False


# Example
main = [1, 2, 3, 4, 5]
sub1 = [2, 3]
sub2 = [3, 5]

print("Does", main, "contain", sub1, "?", is_sublist(main, sub1))  # ✅ True
print("Does", main, "contain", sub2, "?", is_sublist(main, sub2))  # ❌ False

