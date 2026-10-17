import pytest
from selenium import webdriver

def test_smoke():
    # Khoi dong Chrome
    driver = webdriver.Chrome()
    
    try:
        # Mo trang web "The internet"
        driver.get("https://the-internet.herokuapp.com/")
        
        # Lay tieu de cua trang web
        actual_title = driver.title
        print(f"\nTiêu đề thực tế của trang là: '{actual_title}'")
        
        # So sanh tieu de thuc te voi tieu de mong muon
        if actual_title != "The Internet":
            pytest.fail(f"Thất bại! Tiêu đề thực tế là: '{actual_title}'")
        
    finally:
        # Dong trinh duyet
        driver.quit()
        