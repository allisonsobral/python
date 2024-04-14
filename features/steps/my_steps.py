import time
from behave import *
from features.elements.login import LoginPage


@given('launch chrome browser')
def launchbrowser(context):
    driver = context.driver  # Acessa o driver a partir do contexto
    loginPage = LoginPage(driver)

    driver.get("http://facebook.com")
    time.sleep(2)
    loginPage.insertEmail('test@com.com')
    loginPage.insertPassword('123456')

    loginPage.waitLoginButtonToBeDisplayed()

    texto_do_botao = loginPage.getLoginButtonText()
    print("Texto no botão de login:", texto_do_botao)

    loginPage.clickLogin()
    time.sleep(2)


@when('do the login')
def openHomePage(context):
    driver = context.driver  # Acessa o driver a partir do contexto
    driver.get("http://google.com")
    time.sleep(10)

@then('Verify that the logo is present on the page')
def verifyLogo(context):
    context.driver.find_element_by_xpath('//*[@id="password"]')
