Feature: To test login feature

Scenario: User login with valid creds
  Given Open Browser
  When Click "Women" in "my_bdd_project" by "CSS"
  Then Check page title is "My Store"

