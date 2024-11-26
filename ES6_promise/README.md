# ES6 Promises Tasks

## Table of Contents
1. [Keep every promise you make and only make promises you can keep](#task-0)
2. [Don't make a promise...if you know you can't keep it](#task-1)
3. [Catch me if you can!](#task-2)
4. [Handle multiple successful promises](#task-3)
5. [Simple promise](#task-4)
6. [Reject the promises](#task-5)
7. [Handle multiple promises](#task-6)
8. [Load balancer](#task-7)
9. [Throw an error](#task-8)
10. [Throw error / try catch](#task-9)

## Tasks

### Task 0: Keep every promise you make and only make promises you can keep
Return a Promise using this prototype function `getResponseFromAPI()`.
- **File**: [0-promise.js](0-promise.js)

### Task 1: Don't make a promise...if you know you can't keep it
Using the prototype below, return a promise. The parameter is a boolean.
- **Prototype**: `getFullResponseFromAPI(success)`
- **File**: [1-promise.js](1-promise.js)

### Task 2: Catch me if you can!
Using the function prototype below `function handleResponseFromAPI(promise)`, append three handlers to the function:
1. When the Promise resolves, return an object with the following attributes: `status: 200`, `body: success`
2. When the Promise rejects, return an empty `Error` object
3. For every resolution, log `Got a response from the API` to the console
- **File**: [2-then.js](2-then.js)

### Task 3: Handle multiple successful promises
In this file, import `uploadPhoto` and `createUser` from `utils.js`. Knowing that the functions in `utils.js` return promises, use the prototype below to collectively resolve all promises and log `body firstName lastName` to the console.
- **Prototype**: `function handleProfileSignup()`
- In the event of an error, log `Signup system offline` to the console.
- **File**: [3-all.js](3-all.js)

### Task 4: Simple promise
Using the following prototype `function signUpUser(firstName, lastName) { }`, return a resolved promise with this object: `{ firstName: value, lastName: value }`
- **File**: [4-user-promise.js](4-user-promise.js)

### Task 5: Reject the promises
Write and export a function named `uploadPhoto` that should accept one argument `fileName` (string). The function should return a Promise rejecting with an `Error` and the string `$fileName cannot be processed`
- **Prototype**: `export default function uploadPhoto(filename) { }`
- **File**: [5-photo-reject.js](5-photo-reject.js)

### Task 6: Handle multiple promises
Import `signUpUser` from `4-user-promise.js` and `uploadPhoto` from `5-photo-reject.js`. Write and export a function named `handleProfileSignup` that should accept three arguments: `firstName` (string), `lastName` (string), and `fileName` (string). The function should call the two other functions. When the promises are all settled, it should return an array with the following structure: `[ { status: status_of_the_promise, value: value or error returned by the Promise }, ... ]`
- **File**: [6-final-user.js](6-final-user.js)

### Task 7: Load balancer
Write and export a function named `loadBalancer` that should accept two arguments `chinaDownload` (Promise) and `USDownload` (Promise). The function should return the value returned by the promise that resolved the first.
- **Prototype**: `export default function loadBalancer(chinaDownload, USDownload) { }`
- **File**: [7-load_balancer.js](7-load_balancer.js)

### Task 8: Throw an error
Write a function named `divideFunction` that will accept two arguments: `numerator` (Number) and `denominator` (Number). When the denominator argument is equal to 0, the function should throw a new error with the message `cannot divide by 0`. Otherwise, it should return the numerator divided by the denominator.
- **Prototype**: `export default function divideFunction(numerator, denominator) { }`
- **File**: [8-try.js](8-try.js)

### Task 9: Throw error / try catch
Write a function named `guardrail` that will accept one argument `mathFunction` (Function). This function should create and return an array named `queue`. When the `mathFunction` function is executed, the value returned by the function should be appended to the queue. If this function throws an error, the error message should be appended to the queue. In every case, the message `Guardrail was processed` should be added to the queue.
- **Example**: `[ 1000, 'Guardrail was processed' ]`
- **File**: [9-try.js](9-try.js)

