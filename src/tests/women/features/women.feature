Feature: To test women feature

Scenario: User explore women page
  Given Open Browser
  When Click "WOMEN_BTN" in "women" by "CSS"
  Then Check page title is "My Store"

