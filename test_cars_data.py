import csv
import allure

@allure.feature('Cars Data')
@allure.story('CSV Reading')
@allure.title('Test number of cars in CSV')
@allure.severity(allure.severity_level.CRITICAL)

def test_cars_data():
    with allure.step("Open auti.csv"):
        with open("Data/auti.csv") as f:
            reader = csv.reader(f)
            cars = list(reader)
    
    with allure.step("Calculate number of cars"):
        cars_num = len(cars) - 1
        allure.attach(str(cars_num), name="Broj auta", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Check number of cars"):
        assert cars_num==3
