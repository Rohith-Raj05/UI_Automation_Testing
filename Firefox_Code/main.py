

from Functional_UI_Testing.Firefox_Code.screenshot_taker import screenshot_taker


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


    for idx, url in enumerate(urls, start=1):  # Start the index from 1
        for width, height in resolutions:
            screenshot_taker(url, 'firefox', width, height, idx)

if __name__ == "__main__":
    main()


# Hi sir This is Rohith H just graduated from PES University in 2024

# In continuation to the previous video of Functional_UI_Testing on Chrome
# Now i have created this automation function for the Firefox okay lets see now

# One more thing i have used headless mode for chrome which doesn't load the chrome and doesn't show us the interface but works in background
# For this i have not used because i wanted to have some difference between it and wanted to show that it really works on firefox
# okay lets Begin!!
# There is no folder named firefox over there
# lets run

# It takes some time as it will start once after the page is loaded
# so we wait
# it is saved
# it started for second one and also it has saved
# it is running sorry i made mistake i have missed the terminal section sorry i can't show it

# sorry for the delay as the internet is very slow here it is quite hard
# the process is same as the chrome

# the first url is done next is the second url as u can see here
# I am Really sorry for this extra time i don't have some stable internet sorry

# sorry it is already half an hour so please bear with me internet is slow
# only reason i am recording is because in the video u said it has to be recorded sorry once again
# Just three more sorry :(
# Really really sorry :(

# And one more thing i have a windows laptop as u can see i  can't use safari so i won't be able to demo in that and perform test in that
# And once agin sorry for that and this is the last resolution screenshot
# Thank you for bearing with me and i got all the ss i will attach it to github