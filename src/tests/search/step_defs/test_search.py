from tests.women.step_defs.test_women import *

scenarios('../features')


@when(parsers.parse('Send "{text}" to "{element}" in "{page}" by "{locator}"'))
def text_to_field(browser,text, element, page, locator):
    resource = ResourceManager(ResourceManager.get_resource_path(page))
    selector = resource.get_resource(element)
    element = browser.driver.find_element(locators_list[locator], selector)
    element.clear()
    element.send_keys(text)

