Feature: To test Search feature

Scenario: User login with valid creds
  Given Open Browser
  When Send "dress" to "SEARCH_BAR" in "my_second_module" by "ID"
  And Click "SEARCH_BTN" in "my_second_module" by "NAME"

