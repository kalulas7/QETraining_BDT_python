#Suppose you create a feature file for a customer search
#1. Add an scenario outline to simulate a search of a total priced for a list clients

#You should send the name of the client
#The ID of the client
#The Total priced of purchase

#On behind you should create a module with a dictionary containing the list of
#clients and the ID and another dictionary with the ID of the client and the Total_priced, to perform
#the comparison between this values and the expected sent in the feature file.

#2. Add a normal scenario to simulate the search of a client and verify that
#exists into the client list(using the first has created before).
  Feature: Customer search
    Scenario Outline: Search of a total priced for a list clients
      Given A <USER> and <ID> to search
      When I want to search by <AMOUNT>
      Then I get the <USER> and the <AMOUNT>

      Examples:
      | ID | USER     | AMOUNT |
      | 1  | Dennis   | 500    |
      | 2  | Carlos   | 600    |
      | 3  | Marcelo  | 700    |
      | 4  | Carla    | 800    |
      | 5  | Pamela   | 900    |
