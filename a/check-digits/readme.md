# String Methods FRQ: Check Digits

When values are transmitted electronically, there may be transmission erros. Check Digits can detect these errors. In a certain program, the Check Digits are the two rightmost characters. If these two rightmost characters are correct, the value is considered valid and free from transmission errors.
<br><br>
For example, in the string `"8934h6"`, the Check Digits are `"h6"`, and `"8934"` is the value being tested. If `"h6"` are the correct Check Digits for `"8934"`, the value is considered valid.
<br><br>
### Part A
Write the String method `getCheckDigits(String val)` which returns the correct Check Digits for `val`, according to the following rules:
<br><br>
The first character of the Check Digits is determined as follows:
- If `val` contains at least one "5", the first character of the Check Digits is "h", and "b" otherwise.
- If `val` begins with "9", the first character of the Check Digits is uppercase, and lowercase otherwise.<br>

The second character of the Check Digits is determined as follows:
- If the length of `val` is 3 or less, the second character of the Check Digits is "3".
- If the length of `val` is between 4 and 6, inclusive, the second character of the Check Digits is "6".
- Otherwise, the second character of the Check Digits is "8".<br><br>

The table below shows some examples of calls to `getCheckDigits`
| **`val`** | **Check Digits Returned** | **Explaination** |
| -------- | ------- | ------- |
| `"259"` | `"h3"` | `val` contains a 5 and does not begin with a 9, so the first character is lowercase h. The length of `val` is 3, so the second character is 3. |
| `"9221"` | `"B6"` | `val` does not contain a 5 and begins with a 9, so the first character is uppercase B. The length of `val` is 4, so the second character is 4. |
| `"9865315"` | `"H8"` | `val` contains a 5 and begins with a 9, so the first character is uppercase H. The length of `val` is 7, so the second character is 8. |

<br>

Write String method `getCheckDigits(String val)` which returns correct Check Digits for `val`
<br>

**Precondition:** `val` is a string with length greater than 0. It does not contain Check Digits.<br>
**Postcondition** `getCheckDigits` returns a string representing the correct Check Digits for `val`.
<br><br>
### Part B
The boolean method `isValid` is intended to determine whether `test` is valid, using the Check Digits.<br>

The table shows some examples of method calls.
| **`test`** | **Method Call** |  **Return Value**  | **Explaination** |
| -------- | ------- | ------- | ------- |
|  | `getCheckDigits("259")` | `h3` | The correct Check Digits of "259" are "h3" |
| `"259B6"` | `isValid("259B6")` | `false` | The correct Check Digits of "259" are "h3" but the Check Digits in `test` are "B6" |
| `"259h3"` | `isValid("259h3")` | `true` | The correct Check Digits of "259" are "h3" but the Check Digits in `test` are "h3" |

<br>

Write the `isValid` method. You must use `getCheckDigit` appropriately to recieve credit. Assume that `getCheckDigit` works as intended, regardless of what you wrote for Part A.
<br>

**Precondition:** `test` is a string with length at least 3. The two rightmost characters are Check Digits.<br>
**Postcondition:** `isValid` returns `true` if `test` is valid, and `false` otherwise.
