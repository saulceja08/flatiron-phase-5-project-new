# Project Requirements Checklist 

## Back-End
- [ ] Flask/Python API
  - [ ] SQALCHEMY
  - [ ] Models
    - [ ] 4 models
      - [ ] TBD
      - [ ] TBD
      - [ ] TBD
      - [ ] User
        - [ ] VALIDATIONS AND CONSTRAINTS
          - [ ] Email Column
            - [ ] NOT NULLABLE
            - [ ] UNIQUE
            - [ ] REGEX to match email patters
          - [ ] Phone Number Column
            - [ ] NOT NULLABLE
            - [ ] UNIQUE
            - [ ] REGEX to match email patters
    - [ ] 1 many to many relationship
    - [ ] 1 model has all CRUD actions
      - [ ] Follows REST routes
      - [ ] CREATE
        - [ ] GET /resources/new
        - [ ] POST /resources/new
      - [ ] READ
        - [ ] GET /resources (index or show all)
        - [ ] GET /resources/<parameter> (get 1)
        - [ ] GET /resources/<id / name parameter> (get 1)
          - [ ] GET /resources/<filter parameter> (get some)
      - [ ] UPDATE
        - [ ] PATCH /resources
      - [ ] DELETE
        - [ ] DELETE /resources
  - [ ] User can do at least one or some of all CRUD actions on a resource 
  - [ ] User Authorization
    - [ ] Validations and Constraints
      - [ ] Email looks email
      - [ ] Phone number is in format of phone number (multi factor auth)
      - [ ] Strong Password 
        - [ ] 8+ cahrs
        - [ ] symbol
        - [ ] number
        - [ ] upper-case
        - [ ] lower-case
      - [ ] password and password confirmation (visibile)
    - [ ] bcrypt
    - [ ] password hashing
      - [ ] Note: don't store plain text in password
    - [ ] ROUTES
      - [ ] GET & POST/register
        - [ ] upon success
          - [ ] create cookie with email
          - [ ] redirect to /login
      - [ ] GET & POST/login
        - [ ] create session
        - [ ] redirect to /dashboard
      - [ ] GET & POST/logout
        - [ ] upon success
          - [ ] redirect to home page /
          - [ ] delete auth session

## Front-End
- [ ] React Frontend
  - [ ] 3 client-side Routes
    - [ ] with React Router
      - [ ] /sign-up
        - [ ] fetch GET .com/api/v1/sign-up
        - [ ] fetch POST .com/api/v1/sign-up
      - [ ] /login
              - [ ] fetch GET .com/api/v1/login
              - [ ] fetch POST .com/api/v1/login
  - [ ] Components
    - [ ] Nav Bar
  - [ ] User Authorization
    - [ ] Register form
      - [ ] Validation
        - [ ] email regex and required
        - [ ] phone regex and required
        - [ ] strong password confirmation
      - [ ] Formik Controlled Form
      - [ ] Error handling
    - [ ] Login Form
      - [ ] email regex and required
      - [ ] password matches registered
    - [ ] Logged in views
      - [ ] dashboard
    - [ ] Validations and Contraints
      - [ ] Validations on forms
        - [ ] Use Formik library
          - [ ] use correct input type
          - [ ] check input is right data type (string/number(int))
          - [ ] string / number format validation
          - [ ] use regex for correct data types
          - [ ] correct error handling
            - [ ] for individual inputs
            - [ ] for entire form
