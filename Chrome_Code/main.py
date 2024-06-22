
# Hi sir this is Rohith H and just graduated from PES University in 2024
# Now i am demonstrating the first test use case that is Functional_UI_Testing and this is for the chrome browser
# The urls and the resolutions are given below


from screenshot_taker import take_screenshot


def main():
    urls = [
        'https://www.getcalley.com/',
        'https://www.getcalley.com/calley-call-from-browser/',
        'https://www.getcalley.com/calley-pro-features/',
        'https://www.getcalley.com/best-auto-dialer-app/',
        'https://www.getcalley.com/how-calley-auto-dialer-app-works/'
    ]

    resolutions = [
        (1920, 1080),
        (1366, 768),
        (1536, 864),
        (360, 640),
        (414, 896),
        (375, 667)
    ]
    #
    for idx, url in enumerate(urls, start=1):  #it will start the index from 1 which helps in saving screenshots
        for width, height in resolutions:
            take_screenshot(url, 'chrome', width, height, idx)


if __name__ == "__main__":
    main()

# the process is the same for all the browsers urls and everything
# as u can see the images can be seen saved and process for all of them is the same
# We will wait till the first set of resolutions are over that is these and we will wait for the first url
# see Now all the Desktop version are over and now the mobile versions come in that is these three
# and u will see that the image/ screenshot that will be saved will be saved in the different directory called mobile
# AS u can see there is no mobile directory and u can see that it will be created and get stored there
# Ya u can see this below
# The same goes for all the reason it is taking this long is because it will start only after the page gets loaded
# where i live i have some bad internet connection so it is taking some time sorry for that
# The next url got started and saved
# Now the internet got stable and see it is working quite fast now

# See it is now working on url 3 that is that
# Thank u

