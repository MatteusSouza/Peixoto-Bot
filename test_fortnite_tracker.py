from fortnite_tracker import getPower_ranking
from time import sleep


def z(time, message): #sleep
    if message == "":
        print("\nsleep...")
    print(message)
    sleep(time)


def test_validation(username, platform, region):
    pr = getPower_ranking(username, platform, region)

    val = (pr['validation']['platform'] and pr['validation']['region']) is True
    print(f"\nValidation accepted : "
          f"{val}")

    print(f"The platform is correct: {pr['validation']['platform'] is True}")
    print(f"The region is correct: {pr['validation']['region'] is True}")


def test_getPower_ranking(username, platform, region) -> None:
    pr = getPower_ranking(username, platform, region)

    if pr['validation']['platform'] & \
            pr['validation']['platform'] is True:
        print("\nValidation Accepted")

        if pr['status_code'] == 200:
            print("\nThe player was found.\n")

            ex = pr['response_info']
            print('Region:', ex['region'])
            print('Username:', ex['name'])
            print('Platform:', ex['platform'])
            print('Points:', ex['points'])
            print('Cash Price Acquired:', ex['cashPrize'])
            print('Event Played in:', ex['events'])
            print('Rank in Region:', ex['rank'])
            print('Win Percentage in Tournaments:', ex['percentile'])


        else:
            print("\nCould not find the Power ranking for that user. Most likely the user has no Power Ranking.")

    else:
        print("Validation was rejected")


def runTest():
    print("\33[0:33m")
    z(3, "Validation Test\n")
    test_validation(".;95;a.1;", ".", "br")
    test_validation(".;95;a.1;", "pc", ".")
    test_validation(".;95;a.1;", "pc", "br")

    print("\33[0:34m")
    z(3, "\nRequisition Test")

    z(3, "\nTest with valid username")
    test_getPower_ranking("C9 blackoutz", "pc", "br")

    z(3, "\nTest with invalid username")
    test_getPower_ranking(".;95;a.1;", "pc", "br")


runTest()
