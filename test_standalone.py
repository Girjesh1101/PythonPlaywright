import time

from playwright.sync_api import Playwright, expect

def test_standalone(playwright: Playwright):

    username = "prem@yopmail.com"
    password = "Automation@2026"
    event_name = "World Tech Summit"

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://eventhub.rahulshettyacademy.com/login")
    expect(page).to_have_title("EventHub — Discover & Book Events")

    #login
    page.get_by_placeholder("you@email.com").fill(username)
    page.locator("#password").fill(password)
    page.get_by_role("button",name="Sign In").click()
    expect(page.locator("#user-email-display")).to_have_text(username)

    #book an event
    page.get_by_role("button", name="Events").click()
    expect(page.locator("[data-testid='event-card']")).to_have_count(3)
    event = page.locator(".p-4").filter(has_text=event_name)
    event.get_by_role("link",name="Book Now").click()

    #verify event and book event
    expect(page.get_by_text(event_name)).to_be_visible()
    page.get_by_placeholder("Your full name").fill("Automation tester")
    page.get_by_placeholder("you@email.com").fill("prem@yopmail.com")
    page.get_by_placeholder("+91 98765 43210").fill("9820123456")

    totalAmt = page.locator("div.bg-indigo-50 span[class='text-indigo-700']").text_content()
    print(totalAmt.replace("$",""))

    page.get_by_role("button",name="Confirm Booking").click()
    # expect(page.locator('body')).to_have_text("Booking Confirmed!")

    #click on view
    page.get_by_role("link",name="View My Bookings").click()

    print(page.locator("#booking-id").text_content())
    expect(page.locator(".mb-1")).to_have_text(event_name)

    page.get_by_role("link",name="View Details").click()
    expect(page.locator(".text-indigo-700")).to_have_text(totalAmt)
    expect(page.locator(""))

    time.sleep(3)
