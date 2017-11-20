#Suppose you are going to test the form to create a new gmail account :
#Add the feature file and the scenarios for your testing, in your steps verify that arguments received for each field
#are specific (e.g. Birthday Year only numbers, etc, etc)
  Feature: Create a new gmail account
  Scenario: Create a new account for gmail with valid data
    Given A register form page is loaded
    When User fill the FirstName field with Dennis
      And User fill the LastName field with Gamboa
      And User fill the Username field with Dgamboa
      And User fill the Password field with password
      And User fill the Confirm your password field with password
      And User select May option on Birthday select box
      And User fill the Day field with 16
      And User fill the Year field with 1989
      And User select Male option on Gender select box
      And User select Bolivia option on Mobile phone select box
      And User fill the Phone filed with 75992625
      And User fill the Email Address field with example@gmail.com
    Then all data is validated
