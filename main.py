import tweepy

auth = tweepy.OAuthHandler("YLG67nLGZeGtVshL0AxuM23VK", "AF9caoD2orVEctqK9DtwBOfAV38x8xWWPLT47maCQEtKXni2VU")
auth.set_access_token("96074027-nK3nGK6nCeHrlewnxkkQdbMLMcwzR3rWoMvMK1Yw7", "muqrcTqarEu8S8z2JS4ztBGU0b601a9eyrQiqUYdGbCRy")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    tweets = api.user_timeline(screen_name='ariesonly', count=2)
    # Assuming you have retrieved the tweets and stored them in the 'tweets' variable
    for tweet in tweets:
        print(tweet.text)
except Exception as e:
    print(f"An error occurred: {str(e)}")
