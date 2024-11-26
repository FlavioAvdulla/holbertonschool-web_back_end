# ES6 Data Manipulation

This repository contains several JavaScript tasks focused on ES6 data manipulation features. Each task is implemented in a separate JavaScript file.

## Table of Contents

1. Basic List of Objects
2. More Mapping
3. Filter
4. Reduce
5. Combine
6. Typed Arrays
7. Set Data Structure
8. More Set Data Structure
9. Clean Set
10. Map Data Structure
11. More Map Data Structure

## Basic List of Objects

Create a function named `getListStudents` that returns an array of objects.

Each object should have three attributes: id (Number), firstName (String), and location (String).

The array contains the following students in order:
- Guillaume, id: 1, in San Francisco
- James, id: 2, in Columbia
- Serena, id: 5, in San Francisco

- **File:** [0-get_list_students.js](0-get_list_students.js)

## More Mapping

Create a function `getListStudentIds` that returns an array of ids from a list of objects.

- **Function Argument:** An array of objects in the same format as `getListStudents` from the previous task.
- **Behavior:** Returns an empty array if the argument is not an array.
- **Requirement:** Use the `map` function on the array.

- **File:** [1-get_list_student_ids.js](1-get_list_student_ids.js)

## Filter

Create a function `getStudentsByLocation` that returns an array of objects who are located in a specific city.

- **Function Arguments:** A list of students (from `getListStudents`) and a city (string).
- **Requirement:** Use the `filter` function on the array.

- **File:** [2-get_students_by_loc.js](2-get_students_by_loc.js)

## Reduce

Create a function `getStudentIdsSum` that returns the sum of all the student ids.

- **Function Argument:** A list of students (from `getListStudents`).
- **Requirement:** Use the `reduce` function on the array.

- **File:** [3-get_ids_sum.js](3-get_ids_sum.js)

## Combine

Create a function `updateStudentGradeByCity` that returns an array of students for a specific city with their new grade.

- **Function Arguments:** 
  - A list of students (from `getListStudents`)
  - A city (String)
  - New grades (Array of "grade" objects with format `{ studentId: 31, grade: 78 }`)
- **Behavior:** If a student doesn’t have a grade in `newGrades`, the final grade should be `N/A`.
- **Requirement:** Use `filter` and `map` combined.

- **File:** [4-update_grade_by_city.js](4-update_grade_by_city.js)

## Typed Arrays

Create a function named `createInt8TypedArray` that returns a new ArrayBuffer with an Int8 value at a specific position.

- **Function Arguments:** 
  - `length` (Number)
  - `position` (Number)
  - `value` (Number)
- **Behavior:** If adding the value is not possible, the error `Position outside range` should be thrown.

- **File:** [5-typed_arrays.js](5-typed_arrays.js)

## Set Data Structure

Create a function named `setFromArray` that returns a Set from an array.

- **Function Argument:** An array (of any kind of element).

- **File:** [6-set.js](6-set.js)

## More Set Data Structure

Create a function named `hasValuesFromArray` that returns a boolean if all the elements in the array exist within the set.

- **Function Arguments:** 
  - A set (Set)
  - An array (Array)

- **File:** [7-has_array_values.js](7-has_array_values.js)

## Clean Set

Create a function named `cleanSet` that returns a string of all the set values that start with a specific string (`startString`).

- **Function Arguments:** 
  - A set (Set)
  - A startString (String)
- **Behavior:** When a value starts with `startString`, you only append the rest of the string. The string contains all the values of the set separated by `-`.

- **File:** [8-clean_set.js](8-clean_set.js)

## Map Data Structure

Create a function named `groceriesList` that returns a map of groceries with the following items (name, quantity):

- Apples, 10
- Tomatoes, 10
- Pasta, 1
- Rice, 1
- Banana, 5

- **File:** [9-groceries_list.js](9-groceries_list.js)

## More Map Data Structure

Create a function named `updateUniqueItems` that returns an updated map for all items with an initial quantity of 1.

- **Function Argument:** A map similar to the one created in the previous task.
- **Behavior:** For each entry of the map where the quantity is 1, update the quantity to 100. If updating the quantity is not possible (argument is not a map), the error `Cannot process` should be thrown.

- **File:** [10-update_uniq_items.js](10-update_uniq_items.js)
