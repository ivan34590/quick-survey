from pydoc import cli
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
import time
import smtplib, ssl

def quick_survey_mcdonalds(survey_code, email):
    survey_code = str(survey_code)
    cn1 = survey_code[0:5]
    cn2 = survey_code[5:10]
    cn3 = survey_code[10:15]
    cn4 = survey_code[15:20]
    cn5 = survey_code[20:25]
    cn6 = survey_code[25:]
    cn_list = ['_', cn1,cn2, cn3, cn4, cn5, cn6]
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.mcdvoice.com/?AspxAutoDetectCookieSupport=1")

    for i in range(1,7):
        cn_ = 'CN' + str(i)
        cn_input = driver.find_element_by_name(cn_)
        cn_input.send_keys(cn_list[i])

    start_button = driver.find_element_by_name('NextButton')
    start_button.click()

    kiosk = driver.find_element_by_id('textR000455.2')
    kiosk.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    visit = driver.find_element_by_id('textR004000.3')
    visit.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    overall_satisfaction = driver.find_element_by_xpath('//*[@id="FNSR001000"]/td[1]/label')
    overall_satisfaction.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    are_you_a_mcdonalds_rewards_member = driver.find_element_by_xpath('//*[@id="FNSR000444"]/td[2]/label')
    are_you_a_mcdonalds_rewards_member.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    ratings = driver.find_elements_by_class_name('radioSimpleInput')
    for x in range(len(ratings)):
        if x % 5 == 0:
            
            rating = ratings[x]
            rating.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    ratings = driver.find_elements_by_class_name('radioSimpleInput')
    for x in range(len(ratings)):
        if x % 5 == 0:
          
            rating = ratings[x]
            rating.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    what_did_you_order = driver.find_elements_by_class_name('checkboxSimpleInput')
    for random_choice in range(1,16):
        my_random_choice = random.choice(what_did_you_order)
        my_random_choice.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    quality_of_food = driver.find_elements_by_class_name('radioSimpleInput')
    for quality_choice in range(len(quality_of_food)):
        if quality_choice % 5 == 0:
            my_quality_choice = quality_of_food[quality_choice]
            my_quality_choice.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    did_you_have_any_problems = driver.find_element_by_xpath('//*[@id="FNSR016000"]/td[2]/label')
    did_you_have_any_problems.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()


    likely_to_return = driver.find_elements_by_class_name('radioSimpleInput')
    print(likely_to_return)

    highly_likely1 = likely_to_return[0]
    highly_likely2 = likely_to_return[5]

    highly_likely1.click()
    highly_likely2.click()

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    textarea = driver.find_element_by_id('S081000')
    textarea.send_keys('I highly enjoyed my meal. It tasted good. And it was cheap. I would recommend mcdonalds to everyone I know.')

    next_button = driver.find_element_by_class_name('NextButton')
    next_button.click()

    checker = driver.find_elements_by_id('textR000329')
    if len(checker) > 0:
        did_you_purchase_anything_from_the_dollar_menu = driver.find_element_by_xpath('//*[@id="FNSR000329"]/td[2]/label')
        did_you_purchase_anything_from_the_dollar_menu.click()
        next_button = driver.find_element_by_class_name('NextButton')
        next_button.click()

        how_many_times_did_you_vist_mcdonalds_this_month = driver.find_element_by_id('textR020000.2')
        how_many_times_did_you_vist_mcdonalds_this_month.click()

        next_button = driver.find_element_by_class_name('NextButton')
        next_button.click()
        
        favorite_fast_food_restaurant = driver.find_element_by_id('textR000387.4')
        favorite_fast_food_restaurant.click()

        next_button = driver.find_element_by_class_name('NextButton')
        next_button.click()

        mcdonalds_is_a_brand_i_trust = driver.find_element_by_xpath('//*[@id="FNSR000482"]/td[1]/label')
        mcdonalds_is_a_brand_i_trust.click()

        next_button = driver.find_element_by_class_name('NextButton')
        next_button.click()
        
        # next_button = driver.find_element_by_class_name('NextButton')
        # next_button.click()

        validation_code = driver.find_element_by_class_name('ValCode').text
    else:
        how_many_times_did_you_vist_mcdonalds_this_month = driver.find_element_by_id('textR020000.2')
        how_many_times_did_you_vist_mcdonalds_this_month.click()

        next_button = driver.find_element_by_class_name('NextButton')
        next_button.click()

        did_you_purchase_anything_from_the_dollar_menu = driver.find_element_by_xpath('//*[@id="FNSR000329"]/td[2]/label')
        did_you_purchase_anything_from_the_dollar_menu.click()
        next_button = driver.find_element_by_class_name('NextButton')
        next_button.click()

        favorite_fast_food_restaurant = driver.find_element_by_id('textR000387.4')
        favorite_fast_food_restaurant.click()

        next_button = driver.find_element_by_class_name('NextButton')
        next_button.click()

        mcdonalds_is_a_brand_i_trust = driver.find_element_by_xpath('//*[@id="FNSR000482"]/td[1]/label')
        mcdonalds_is_a_brand_i_trust.click()

        next_button = driver.find_element_by_class_name('NextButton')
        next_button.click()

        validation_code = driver.find_element_by_class_name('ValCode').text




       




    # did_you_purchase_anything_from_the_dollar_menu = driver.find_element_by_xpath('//*[@id="FNSR000329"]/td[2]/label')
    # did_you_purchase_anything_from_the_dollar_menu.click()

    # next_button = driver.find_element_by_class_name('NextButton')
    # next_button.click()

    # how_many_times_did_you_vist_mcdonalds_this_month = driver.find_element_by_id('textR020000.2')
    # how_many_times_did_you_vist_mcdonalds_this_month.click()

    # next_button = driver.find_element_by_class_name('NextButton')
    # next_button.click()

    # favorite_fast_food_restaurant = driver.find_element_by_id('textR000387.4')
    # favorite_fast_food_restaurant.click()

    # next_button = driver.find_element_by_class_name('NextButton')
    # next_button.click()

    # mcdonalds_is_a_brand_i_trust = driver.find_element_by_xpath('//*[@id="FNSR000482"]/td[1]/label')
    # mcdonalds_is_a_brand_i_trust.click()

    # next_button = driver.find_element_by_class_name('NextButton')
    # next_button.click()
    
    # # next_button = driver.find_element_by_class_name('NextButton')
    # # next_button.click()

    # validation_code = driver.find_element_by_class_name('ValCode').text

    port = 465
    password = "Tacos1284$"
    context = ssl.create_default_context()
    sender_email = "dr.jcampbell235@gmail.com"
    receiver_email = email
    message = f"""\
    Subject: Hi there

    {validation_code}
    This message is sent from Python."""

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("dr.jcampbell235@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)