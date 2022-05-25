from pydoc import cli
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time
import smtplib, ssl

def quick_survey_ihop(survey_code, check_number, email):
    survey_code 
    check_number

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.myihopfeedback.com/usa")
    click_here = driver.find_element_by_link_text("click here.")
    click_here.click()

    survey = driver.find_element_by_class_name("coupon-length-13 ")
    check = driver.find_element_by_class_name("coupon-length-12 ")
    survey.send_keys(survey_code)
    check.send_keys(check_number)
    # start = driver.find_element_by_class_name("NextButton")
    start = driver.find_element_by_xpath('//*[@id="NextButton"]')
    driver.execute_script("arguments[0].click();", start)
    
    
    highly_satisfied = driver.find_element_by_class_name("radioSimpleInput")
    highly_satisfied.click()
    next_button = driver.find_element_by_id("NextButton")

    next_button.click()
    dine_in = driver.find_element_by_xpath("//label[contains( text(), 'Dine In')]")
    dine_in.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    first_item_on_list = driver.find_element_by_class_name("radioSimpleInput")
    first_item_on_list.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    first_item_on_list_on_second_page = driver.find_element_by_class_name("radioSimpleInput")
    first_item_on_list_on_second_page.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    first_item_on_list_on_third_page = driver.find_element_by_class_name("radioSimpleInput")
    first_item_on_list_on_third_page.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    first_item_on_list_on_fourth_page = driver.find_element_by_class_name("radioSimpleInput")
    first_item_on_list_on_fourth_page.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    problem_with_experience = driver.find_element_by_xpath("//*[@id='FNSR000015']/td[2]")
    problem_with_experience.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    return_to_this_ihop = driver.find_element_by_xpath("//*[@id='FNSR000072']/td[1]/span")
    return_to_this_ihop.click()
    return_to_this_ihop2 = driver.find_element_by_xpath("//*[@id='FNSR000074']/td[1]/span")
    return_to_this_ihop2.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    past_60_days = driver.find_element_by_class_name("radioSimpleInput")
    past_60_days.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    first_visit = driver.find_element_by_xpath("//*[@id='FNSR000079']/div/div/div[2]/span/span")
    first_visit.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    reason_for_visit_ = driver.find_element_by_xpath("//*[@id='FNSR000081']/div/div/div[6]/label")
    reason_for_visit_.click()
    next_button = driver.find_element_by_id("NextButton")
    next_button.click()
    get_validation_code = driver.find_element_by_class_name("ValCode").text
    print("This is your code for free pancakes at ihop: ", get_validation_code)

    port = 465
    password = "Tacos1284$"
    context = ssl.create_default_context()
    sender_email = "dr.jcampbell235@gmail.com"
    receiver_email = email
    message = f"""\
    Subject: Hi there

    {get_validation_code}
    This message is sent from Python."""

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("dr.jcampbell235@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)




