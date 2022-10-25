Feature: To test Search feature

Scenario: User search for keyword
  Given Open Browser
  When Send "dress" to "SEARCH_BAR" in "search" by "ID"
  And Click "SEARCH_BTN" in "search" by "NAME"

