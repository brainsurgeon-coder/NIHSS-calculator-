# This is a software to calculate NIHSS score in stroke patients
print("*".center(80, '*'))
print()
print("Welcome to the NIHSS score calculator  - copyright Dr Hrishikesh Sarkar")
print()
print("Enter level of consciousness: \nAlert - 0  \nDrowsy - 1  \nStupurous - 2 \nUnconscious - 3")
loc1 = int(input())
print()
print("Enter LOC question score (months/age): \nBoth correct - 0 \nOne correct - 1 \nBoth incorrect - 2")
loc2 = int(input())
print()
print("Enter LOC commands score: \nBoth correct - 0 \nOne correct - 1 \nBoth incorrect - 2")
loc3 = int(input())
print()
print("Enter gaze score: \nNormal - 0 \nMinor - 1 \nForced Deviation - 2")
gaze = int(input())
print()
print("Enter visual field score: \nNormal - 0 \nPartial hemi - 1 \nComplete hemi - 2")
vision = int(input())
print()
print("Enter facial palsy score: \nNone - 0 \nMinor - 1 \nPartial - 2 \nComplete - 3")
face = int(input())
print()
print("Enter motor score for right hand: \nNo drift - 0 \nDrift - 1 \nCant resist gravity - 2 \nNo effect against gravity - 3 \nNo movement - 4")
motorRH = int(input())
print()
print("Enter motor score for right leg: \nNo drift - 0 \nDrift - 1 \nCant resist gravity - 2 \nNo effect against gravity - 3 \nNo movement - 4")
motorRL = int(input())
print()
print("Enter motor score for left hand:\nNo drift - 0 \nDrift - 1 \nCant resist gravity - 2 \nNo effect against gravity - 3 \nNo movement - 4")
motorLH = int(input())
print()
print("Enter motor score for left leg:\nNo drift - 0 \nDrift - 1 \nCant resist gravity - 2 \nNo effect against gravity - 3 \nNo movement - 4 ")
motorLL = int(input())
print()
print("Enter score for limb ataxia: \nNone - 0  \nPresent in one limb - 1 \nPresent in two limbs - 2")
atax = int(input())
print()
print("Enter sensation score: \nNormal - 0 \nPartial - 1 \nSevere - 2")
sense = int(input())
print()
print("Enter best language score: \nNormal - 0 \nSevere - 1 \nGobal - 2 ")
lang = int(input())
print()
print("Enter dysarthria score: \nNormal - 0 \nMild - 1 \nSevere - 2 \nIntubated - 3")
dysar = int(input())
print()
print("Enter extinction and attention score: \nNil - 0 \nMild - 1 \nSevere - 2") 
atten = int(input())
print()
print("Thank you for entering details!".center(20, '*'))
print()

NIHSSscore = loc1 + loc2 + loc3 + gaze + vision + face + motorRH + motorRL + motorLH+ motorLL + atax + sense + lang + dysar + atten

print("Can you guess the NIHSS score of this patient?")
guess = int(input())

if guess == NIHSSscore:
    print("You are pretty good!!. You guessed right!!")
else:
    print("Your guess was incorrect.")
    
print()         
print("The NIHSS score of this patient is " + str(NIHSSscore))

print()
if NIHSSscore == 0:
    print("This patient does not have any stroke.")
if NIHSSscore <= 4:
    print("This patient has a minor stroke.")
if NIHSSscore >=5 and NIHSSscore <=15:
    print("This patient has moderate stroke")
if NIHSSscore >=16 and NIHSSscore <= 20:
    print("This patient has moderate to severe stroke")
if NIHSSscore >= 21:
    print("This patient has a severe stroke")

print()

print("- Copyright Dr Hrishikesh Sarkar".center(30))
print()
print("*".center(80, '*'))

