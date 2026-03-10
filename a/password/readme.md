# Methods FRQ: Password Rules

Secure passwords are password that are easy for the user to remember and hard for others to guess. Someone trying to guess a password must get it exactly right: "password" is not the same as "p@ssword" or "p8ssword". Thereform, password rules often require digits and special characters to be a part of a user's password. Password rules also often specify a minimum length, since longer passwords are more secure.
<br><br>
Consider an application that requires user passwords to meet all three of the following requirements:
- Length of at least 8 characters
- Contains at least 1 digit
- Contains at least one of the special characters '@', '%', or '#'

<br>The boolean method `passwordRuleCheck` is intended to return `true` if the string `userPass` meets all three requirements and `false` otherwise.
<br><br>
Examples:
| **userPass** | **Meets Requirements?** | **Reason** |
| -------- | ------- | ------- |
| "c@mputer" | No | Does not contain a digit |
| "c*mput3r" | No | Does not contain amy of the special characters '@', '%', or '#' |
| "c9#p" | No | Too short |
| "c9mp%ter" | Yes | At least 8 characters in length, contains a digit, and contains one of the special characters '@', '%', or '#' |
<br>
Write the boolean method `passwordRuleCheck`, which takes `userPass` as a parameter and returns `true` if the string `userPass` meets all three requirements and `false` otherwise.<br><br>

**Precondition:** The parameter `userPass` is a string which is neither null or empty.<br>
**Postcondition:** `passwordRuleCheck` returns a correct boolean value.
