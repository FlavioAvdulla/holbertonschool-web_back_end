# ES6 classes

This repository contains several JavaScript tasks focused on advanced JavaScript features. Each task is implemented in a separate JavaScript file.

## Table of Contents

1. [You Used to Attend a Place Like This](#you-used-to-attend-a-place-like-this)
2. [Let's Make Some Classrooms](#lets-make-some-classrooms)
3. [A Course, Getters, and Setters](#a-course-getters-and-setters)
4. [Methods, Static Methods, Computed Method Names..... MONEY](#methods-static-methods-computed-method-names-money)
5. [Pricing](#pricing)
6. [A Building](#a-building)
7. [Inheritance](#inheritance)
8. [Airport](#airport)
9. [Primitive - Holberton Class](#primitive-holberton-class)
10. [Hoisting](#hoisting)
11. [Vroom](#vroom)

## You Used to Attend a Place Like This

Implement a class named `ClassRoom`.

- **Prototype:** `export default class ClassRoom`
- **Attributes:**
  - `maxStudentsSize` (Number)
- **File:** [0-classroom.js](0-classroom.js)

## Let's Make Some Classrooms

Import the `ClassRoom` class from `0-classroom.js`.

- **Function:** `initializeRooms`
- **Objective:** Return an array of 3 `ClassRoom` objects with the sizes 19, 20, and 34.
- **File:** [1-make_classrooms.js](1-make_classrooms.js)

## A Course, Getters, and Setters

Implement a class named `HolbertonCourse`.

- **Attributes:**
  - `name` (String)
  - `length` (Number)
  - `students` (Array of Strings)
- **Objective:** Verify the types of attributes during object creation and use getters and setters.
- **File:** [2-hbtn_course.js](2-hbtn_course.js)

## Methods, Static Methods, Computed Method Names..... MONEY

Implement a class named `Currency`.

- **Attributes:**
  - `code` (String)
  - `name` (String)
- **Objective:** Use getters and setters and implement a method `displayFullCurrency`.
- **File:** [3-currency.js](3-currency.js)

## Pricing

Import the `Currency` class from `3-currency.js`.

- **Class:** `Pricing`
- **Attributes:**
  - `amount` (Number)
  - `currency` (Currency)
- **Objective:** Use getters and setters, implement `displayFullPrice` method, and a static method `convertPrice`.
- **File:** [4-pricing.js](4-pricing.js)

## A Building

Implement a class named `Building`.

- **Attributes:**
  - `sqft` (Number)
- **Objective:** Use getters and create an abstract class with `evacuationWarningMessage` method.
- **File:** [5-building.js](5-building.js)

## Inheritance

Import `Building` from `5-building.js`.

- **Class:** `SkyHighBuilding`
- **Attributes:**
  - `sqft` (Number)
  - `floors` (Number)
- **Objective:** Extend `Building` and override `evacuationWarningMessage`.
- **File:** [6-sky_high.js](6-sky_high.js)

## Airport

Implement a class named `Airport`.

- **Attributes:**
  - `name` (String)
  - `code` (String)
- **Objective:** Return the airport code as the default string description.
- **File:** [7-airport.js](7-airport.js)

## Primitive - Holberton Class

Implement a class named `HolbertonClass`.

- **Attributes:**
  - `size` (Number)
  - `location` (String)
- **Objective:** Cast class to a number and string.
- **File:** [8-hbtn_class.js](8-hbtn_class.js)

## Hoisting

Fix the code to work properly with class declarations and object instantiations.

- **File:** [9-hoisting.js](9-hoisting.js)

## Vroom

Implement a class named `Car`.

- **Attributes:**
  - `brand` (String)
  - `motor` (String)
  - `color` (String)
- **Objective:** Add a method `cloneCar` to return a new object of the class.
- **Hint:** Use Symbols in ES6.
- **File:** [10-car.js](10-car.js)
