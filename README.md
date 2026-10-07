# TriangleClassifier
module 6 triangle classifier assignment
### Copilot Review Log

| Test | Copilot-suggested? | Kept / edited / rejected | Why |

| `test_invalid_negative_sides` | Yes | Kept | Correctly asserted "Invalid" for 0 and negative inputs. |
| `test_degenerate_boundary` | Yes | Kept | Correctly identified that 2+2=4 should return "Invalid". |
| `test_equilateral` | Yes | Kept | Standard test case was accurate. |
| `test_right_integer` | Yes | Kept | Correctly asserted "Right Scalene" for 3, 4, 5. |
| `test_right_non_integer` | Yes | Edited | Copilot asserted with `==` for the floating-point calculation of `5 * math.sqrt(2)`; changed logic to ensure it relies on the `math.isclose` implementation in the main function. |




"We run a stained-glass studio. Customers enter three side lengths and we tell them the shape and whether it’s buildable. If it’s not a valid triangle, show a message, don’t crash. Also flag right-angle pieces — they need reinforced corners. It has to be correct every time; a wrong answer means a ruined pane."


Acceptance Criteria

1 Invalid Input Handling: Given inputs that cannot form a valid triangle, the application must return the string "Invalid" without causing a system crash.

2 Right Angle Flagging: Given side lengths that form a 90-degree angle, the application must return a string containing the word "Right" so the shop knows to apply reinforced corners.

3 Accurate Shape Identification: Given valid side lengths, the application must correctly identify and return the base shape (e.g., "Isosceles", "Equilateral", "Scalene") to ensure the pane is built correctly.



How to Run the Tests
To run the test suite, ensure you have `pytest` installed (`pip install -r requirements.txt`), then execute the following command in the terminal:
`pytest test_triangle.py test_acceptance.py`


Equivalence Classes and Boundaries
Equivalence Classes:
1 Valid triangles: Scalene (all sides different), Isosceles (two sides equal), Equilateral (all sides equal).
2 Right triangles: Satisfy the Pythagorean theorem.
3 Invalid triangles: Fail the triangle inequality theorem.

Boundaries:
1 Zeros and negative numbers (side $\le$ 0).
2 Degenerate cases where the sum of two sides equals the third (e.g., 2 + 2 = 4).
3 Floating-point precision limits for right-angled triangles with non-integer sides.

Math Explanation
An equilateral triangle has three identical interior angles of 60 degrees. Because it lacks a 90-degree angle, it can never satisfy the Pythagorean theorem and therefore can never be a right triangle.


AI-Use Disclosure
 Used gemini for help with triangle.py
GitHub Copilot was used to autocomplete the unit tests in `test_triangle.py`.
 I verified each suggestion against the assignment specification, specifically catching and rejecting Copilot's attempt to use strict equality (`==`) for floating-point right triangle checks.
No AI tools were used to generate the acceptance criteria or acceptance test.