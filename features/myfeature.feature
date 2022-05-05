Feature: Login to Website

  Background: Common steps
    Given The chrome browser is launched
    When Open the trackify website


  Scenario: Test the logo is present in the homepage
    Then verify the logo is present in the webiste
    And Close the browser

#  Scenario: Test the email feild is present and enabled
#    Then verify the presence of email field
#    And close the browser
