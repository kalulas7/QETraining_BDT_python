Feature: test zipcode
  Scenario: test validations
    Given only numbers zipcode: 452630
      And letters or underscore: Brasil_SaoPaulo
      And numbers with thousands separator: 1.5