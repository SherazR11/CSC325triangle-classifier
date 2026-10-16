# Triangle Classifier

A small Python project that classifies a triangle from its three side lengths. It identifies equilateral, isosceles, and scalene triangles, marks right triangles, and rejects side lengths that cannot form a valid triangle.

## Classification Rules

| Result | Rule | Example |
| --- | --- | --- |
| Equilateral | All three sides are equal. | `(5, 5, 5)` |
| Isosceles | Exactly two sides are equal. | `(5, 5, 8)` |
| Scalene | All three sides are different. | `(3, 4, 6)` |
| Right | The squares of the two shorter sides sum to the square of the longest side. The result is prefixed with `Right`. | `(3, 4, 5)` returns `Right Scalene` |
| Invalid | A side is zero or negative, or the triangle inequality is not satisfied. | `(1, 1, 2)` |

A valid triangle requires the sum of any two sides to be greater than the remaining side. An equilateral triangle cannot be right-angled: its angles are all 60 degrees.

## Usage

Import `classify_triangle` from `triangle.py` and pass the three side lengths:

```python
from triangle import classify_triangle

print(classify_triangle(3, 4, 5))  # Right Scalene
print(classify_triangle(2, 2, 2))  # Equilateral
print(classify_triangle(2, 3, 5))  # Invalid
```

## Run the Tests

Python and pytest are required. Install pytest if it is not already available:

```sh
python -m pip install pytest
```

From the project directory, run the unit and acceptance tests with:

```sh
python -m pytest -v
```

## Equivalence Classes and Boundaries

- **Equilateral:** `(5, 5, 5)`.
- **Isosceles:** `(5, 5, 8)`.
- **Scalene:** `(3, 4, 6)`.
- **Right triangle:** `(3, 4, 5)`.
- **Zero or negative side:** Invalid, for example `(0, 1, 1)` or `(-1, 1, 1)`.
- **Degenerate boundary:** `(1, 1, 2)` is invalid because two sides sum to the third side.
- **Floating-point boundary:** `(5, 5, 5 * sqrt(2))` tests a right isosceles triangle with a non-integer hypotenuse.

## Acceptance Criteria

1. Valid triangles are classified as equilateral, isosceles, or scalene according to their side lengths.
2. Invalid side lengths, including zero, negative, and degenerate cases, return `Invalid` rather than crashing.
3. Valid right triangles are prefixed with `Right` so the stained-glass studio can identify pieces requiring reinforced corners.

The acceptance test in [`test_acceptance.py`](test_acceptance.py) calls `classify_triangle()` and checks representative examples against these requirements.

## Copilot Review Log
The following unit tests in `test_triangle.py` were drafted with GitHub Copilot and reviewed against the assignment requirements:

| Test | Decision | Review note |
| --- | --- | --- |
| `test_3_4_5_triangle` | Kept | Checks a right scalene triangle. |
| `test_equilateral_triangle` | Kept | Checks three equal sides. |
| `test_isosceles_triangle` | Kept | Checks exactly two equal sides with a valid non-right triangle. |
| `test_scalene_triangle` | Edited | Uses `(3, 4, 6)` so it tests a non-right scalene triangle instead of repeating the `(3, 4, 5)` case. |
| `test_invalid_triangle` | Kept | Checks a zero-length side. |
| `test_invalid_triangle_two_sides_equal_third` | Kept | Checks the degenerate boundary where two sides equal the third side. |
| `test_right_isosceles_triangle_non_integer_hypotenuse` | Edited | Uses `5 * math.sqrt(2)` to test a right isosceles triangle with a non-integer hypotenuse. I checked that the implementation uses `math.isclose()` with a tolerance rather than relying on exact floating-point equality with `==`. |
| `test_invalid_triangle_negative_side` | Kept | Checks a negative side length. |

## AI-Use Disclosure

GitHub Copilot was used to draft unit tests in `test_triangle.py`. I reviewed its suggestions against the assignment requirements and edited the scalene and non-integer right-triangle tests. ChatGPT was used for debugging assistance, and help organizing the project as well as better create the README. I ran the test suite with pytest to verify the results. The acceptance test in `test_acceptance.py` was written without Copilot.