def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True



#Javascript example

# var checkIfPalindrome = function(s) {
#     let left = 0;
#     let right = s.length - 1;
#     while (left < right) {
#         if (s[left] != s[right]) {
#             return false;
#         }
#         left++;
#         right--;
#     }
#     return true;
# }



#Java example

# public boolean checkIfPalindrome(String s) {
#     int left = 0;
#     int right = s.length() - 1;
#     while (left < right) {
#         if (s.charAt(left) != s.charAt(right)) {
#             return false;
#         }
#         left++;
#         right--;
#     }
#     return true;
# }



#C++ example

# bool checkIfPalindrome(string s) {
#     int left = 0;
#     int right = s.size() - 1;
#     while (left < right) {
#         if (s[left] != s[right]) {
#             return false;
#         }
#         left++;
#         right--;
#     }
#     return true;
# }