from selenium import webdriver
from behave import fixture, use_fixture

@fixture
def setup_driver(context):
    # Defina o caminho para o chromedriver
    chromedriver_path = './chromedriver'

    # Inicialize o driver do Chrome
    driver = webdriver.Chrome(executable_path=chromedriver_path)

    context.driver = driver
    yield context.driver  # Isso permite que o driver seja usado nos passos do teste
    driver.quit()

def before_all(context):
    # Use o fixture para configurar o driver antes de todos os testes
    use_fixture(setup_driver, context)
