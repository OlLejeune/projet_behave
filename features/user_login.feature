Feature: User Login
    in order to access personal account features
    As a user
    I want to log in to the system

    Scenario: User login
        Given the login page is displayed
        When a user logs in with username "existinguser" and password "password123"
        Then the user should be redirected to the homepage
        And the user data should be present in the database
        