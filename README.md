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