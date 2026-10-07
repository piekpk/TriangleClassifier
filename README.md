# TriangleClassifier
module 6 triangle classifier assignment
### Copilot Review Log

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
| :--- | :--- | :--- | :--- |
| `test_invalid_negative_sides` | Yes | Kept | Correctly asserted "Invalid" for 0 and negative inputs. |
| `test_degenerate_boundary` | Yes | Kept | Correctly identified that 2+2=4 should return "Invalid". |
| `test_equilateral` | Yes | Kept | Standard test case was accurate. |
| `test_right_integer` | Yes | Kept | Correctly asserted "Right Scalene" for 3, 4, 5. |
| `test_right_non_integer` | Yes | Edited | Copilot asserted with `==` for the floating-point calculation of `5 * math.sqrt(2)`; changed logic to ensure it relies on the `math.isclose` implementation in the main function. |




"We run a stained-glass studio. Customers enter three side lengths and we tell them the shape and whether it’s buildable. If it’s not a valid triangle, show a message, don’t crash. Also flag right-angle pieces — they need reinforced corners. It has to be correct every time; a wrong answer means a ruined pane."


Invalid Input Handling: Given inputs that cannot form a valid triangle, the application must return the string "Invalid" without causing a system crash.

Right Angle Flagging: Given side lengths that form a 90-degree angle, the application must return a string containing the word "Right" so the shop knows to apply reinforced corners.

Accurate Shape Identification: Given valid side lengths, the application must correctly identify and return the base shape (e.g., "Isosceles", "Equilateral", "Scalene") to ensure the pane is built correctly.

