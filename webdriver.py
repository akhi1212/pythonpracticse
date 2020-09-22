from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

#browser initiating
#browser = webdriver.Firefox(executable_path="G:/geckodriver/geckodriver.exe")
browser = webdriver.Chrome('G:/chrome_latestexe/chromedriver.exe')
#to open the application
browser.get('https://stage.mylendistry.com/login.html')
browser.maximize_window()
time.sleep(5)
elem_bttnClick = browser.find_element_by_xpath("//a[@onclick='newCustomer()']")
elem_bttnClick.click()
time.sleep(10)
elem_firstname = browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@formcontrolname='firstName']")
elem_firstname.send_keys("Marisol L")
time.sleep(3)
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@formcontrolname='lastName']").send_keys("test")
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@formcontrolname='email']").send_keys("testakash100131@yopmail.com")
time.sleep(3)
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@formcontrolname='confirmEmailAddressCtrl']").send_keys("testakash100131@yopmail.com")
time.sleep(3)
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@formcontrolname='phoneNo']").send_keys("9999999999")
time.sleep(3)
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@formcontrolname='confirmPhoneNo']").send_keys("9999999999")
time.sleep(3)
##placeholder="Business Name"
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@formcontrolname='corporateName']").send_keys("Jackson Services")
time.sleep(3)
##formcontrolname="zipcode"
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@formcontrolname='zipcode']").send_keys("65488")
time.sleep(3)
browser.find_element_by_xpath("//*[contains(@class,'mat-select-trigger')]").click()
time.sleep(10)
browser.find_element_by_xpath("//*[@id='mat-option-5']/span").click()
time.sleep(5)
browser.find_element_by_xpath("//*[contains(text(),'Next')]").click()
time.sleep(10)
icon_wait = WebDriverWait(browser, 30).until(ec.visibility_of_element_located((By.XPATH,"//*[contains(@id,'mat-expansion-panel-header-0')]")))
icon_wait.click()
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@placeholder='Owner Title']").send_keys("Mrs.")
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@placeholder='SSN Number']").send_keys("000-00-0001")
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@placeholder='Date of Birth (mm/dd/yyyy)']").send_keys("6/12/1991")
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@placeholder='Owner Percentage']").send_keys("50")
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@placeholder='Owner Primary Residence']").send_keys(" 	")
time.sleep(5)
browser.find_element_by_xpath("//div[@class='mat-input-infix mat-form-field-infix']/input[@placeholder='Owner City']").send_keys("NewYork")
##placeholder="Owner City"
time.sleep(5)
browser.find_element_by_xpath("//mat-select[@placeholder='State']").click()
##//*[@id="cdk-accordion-child-0"]/div/div[3]/mat-form-field[6]/div/div[1]/div  //*[@id="mat-option-31"]/span
time.sleep(3)
browser.find_element_by_xpath("//*[@id='mat-option-31']/span[text()='Missouri']").click()
time.sleep(2)
browser.find_element_by_xpath("//input[@id='consent-check-box-id0']").click()
time.sleep(2)
browser.find_element_by_xpath("//*[contains(@id,'personalContinue')]/span").click()
time.sleep(10)
use_funding = WebDriverWait(browser, 30).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='cdk-step-content-0-2']/div/div[1]/mat-card[4]/div/div[2]")))
use_funding.click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='cdk-step-content-0-2']/div/div[2]/button[@class='btn-deafult btn-secondary mat-button']/span[@class='mat-button-wrapper']").click()
customer_base = WebDriverWait(browser, 30).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='cdk-step-content-0-3']/div/div[1]/mat-card[2]")))
customer_base.click()
time.sleep(5)
browser.find_element_by_xpath("//*[@id='cdk-step-content-0-3']/div/div[2]/button[@class='btn-deafult btn-secondary mat-button']/span").click()
business_do = WebDriverWait(browser, 30).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='cdk-step-content-0-4']/div/div[1]/mat-card[2]")))
business_do.click()
time.sleep(5)
browser.find_element_by_xpath("//*[@id='cdk-step-content-0-4']/div/div[2]/button[@class='btn-deafult btn-secondary mat-button']").click()
type_bussiness = WebDriverWait(browser, 30).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='cdk-step-content-0-5']/div/div[1]/mat-card[3]")))
type_bussiness.click()
time.sleep(5)
browser.find_element_by_xpath("//*[@id='cdk-step-content-0-5']/div/div[2]/button[@class='btn-deafult btn-secondary mat-button']").click()
tell_more =  WebDriverWait(browser, 30).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='cdk-step-content-0-6']/div/div[1]/mat-card[2]")))
tell_more.click()
time.sleep(5)
browser.find_element_by_xpath("//*[@id='cdk-step-content-0-6']/div/div[2]/button[@class='btn-deafult btn-secondary mat-button']/span[@class='mat-button-wrapper']").click()
time.sleep(5)



##//*[@id="mat-expansion-panel-header-0"] placeholder="SSN Number" placeholder="Owner Percentage" //div[@class='mat-select-value']
##//div[@class='mat-input-infix mat-form-field-infix']/input[@placeholder='Owner Title']
##formcontrolname="lastName" 
##//*[@id="mat-option-5"]/span[text()='Dev OPS'] //*[@id="personalContinue"]/span
##placeholder="Date of Birth (mm/dd/yyyy)"